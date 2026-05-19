# Copyright 2013-2026 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# UCL: from PR https://github.com/pjpbyrne/spack-packages/tree/39b0b17fc02456f2832b8569cc1e87df964b7639/repos/spack_repo/builtin/packages/castep, commented out compiler match checks
import glob
import math
import os
import re

#from spack_repo.builtin.build_systems.cmake import CMakePackage, generator

from spack.package import *


class Castep(CMakePackage):
    """
    CASTEP is a leading code for calculating the
    properties of materials from first principles.
    Using density functional theory, it can simulate
    a wide range of properties of materials
    proprieties including energetics, structure at
    the atomic level, vibrational properties,
    electronic response properties etc.
    """

    homepage = "http://castep.org"
    url = f"file://{os.getcwd()}/CASTEP-25.12.tar.gz"
    manual_download = True

    maintainers("pjpbyrne")

    # Versions
    version("26.11", sha256="cd38ec9e87fd92b91fe7910179acad6486ee57935832846959151ec406fb5fb6")
    version("25.12", sha256="e21177bfe4cb3f3d098b666c90771e3da2826503b002b8e325e3ca1e230cfc7d")
    version("25.11", sha256="af6851a973ef83bbd725f6f33ff7616dd9d589bd75cf74cd106b13c3369167f6")
    version("24.1", sha256="97d77a4f3ce3f5c5b87e812f15a2c2cb23918acd7034c91a872b6d66ea0f7dbb")
    version("23.1", sha256="7fba0450d3fd71586c8498ce51975bbdde923759ab298a656409280c29bf45b5")

    # Builder Depdencies
    generator("ninja", "make", default="make")

    with when("generator=make"):
        depends_on("cmake@3.25:", type="build")
        depends_on("gmake@4.2:", type="build", when="generator=make")

    with when("generator=ninja"):
        depends_on("ninja", type="build")
        depends_on("cmake@3.27.9:", type="build")

    # List of the main variant options
    variant(
        "build_type",
        default="fast",
        description="CASTEP build type",
        values=("debug", "intermediate", "fast"),
    )
    variant("mpi", description="Build with MPI parallelism", default=True)
    variant("libxc", description="Build with libXC support", default=False)
    variant("openmp", description="Use OpenMP threading", default=True)
    variant(
        "grimmed3",
        description="Compile with support for Grimme D3 dispersion scheme",
        default=True,
    )
    variant(
        "grimmed4",
        description="Compile with support for Grimme D4 dispersion scheme",
        default=True,
    )
    variant("dlmg", description="Compile with support for open boundary conditions", default=True)
    variant("tools", default=True, description="Build the executable auxilliary programs")
    variant("utilities", default=True, description="Build the third-party scripts and utilities")

    # Depedencies
    depends_on("c", type="build")
    depends_on("fortran", type="build")
    depends_on("awk@3:", type="build")
    depends_on("perl", type=("build", "run"))
    depends_on("lapack")
    depends_on("blas")
    depends_on("fftw-api@3")

    extends("python", type=("build", "run"))
    depends_on("py-pip", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-setuptools", type=("build", "run"), when="@:24")

    # Ensure mpi has been compiled with fortran support...
    with when("+mpi"):
        depends_on("mpi", type=("build", "link", "run"))
    #    depends_on("mpich+fortran", when="%mpich")
    #    depends_on("openmpi+fortran", when="%openmpi")

    # To use FFT mkl option only allowed when also using mkl as lapack/blas
    #requires(
    #    "%lapack=intel-oneapi-mkl",
    #    when="%fftw-api=intel-oneapi-mkl",
    #    msg="MKL must be used as the BLAS/LAPACK library to use it for FFTs",
    #)

    # Block older compiler versions that are not supported (and explicitly do not work)
    conflicts("%oneapi", when="@:23", msg="Intel LLVM requires CASTEP 24 or newer")
    conflicts("%llvm", when="@:25", msg="LLVM(Flang) requires CASTEP 26 or newer")

    # Fortran dependencies must be compiled with the same compiler
    sub_packages = {
        "mpi": ["openmpi", "mpich"],
        "blas": ["openblas", "flexiblas"],
        "lapack": ["openblas", "flexiblas"],
        "fftw-api": ["fftw"],
    }

    #for compiler in ["gcc", "llvm", "intel", "oneapi"]:
    #    for virtual_package, package_providers in sub_packages.items():
    #        for actual_package in package_providers:
    #            depends_on(
    #                f"{actual_package}%fortran={compiler}",
    #                when=f"%fortran={compiler} %{virtual_package}={actual_package}",
    #            )

    # Special rules for mkl
    #requires("%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%lapack=intel-oneapi-mkl")
    #requires(
    #    "%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%fftw-api=intel-oneapi-mkl"
    #)
    #requires("%fortran=intel", "%fortran=oneapi", "%fortran=gcc", when="%mpi=intel-oneapi-mpi")

    # Fix some issues with the build time test and utility python scripts with python 3.13
    patch("Replace_pipes_with_shex_in_testcode.patch", when="@:24 %python@3.13:")
    patch(
        "Fix-castepconv-strings-with-invalid-escape-character.patch", when="@:26.11 %python@3.13:"
    )

    # Patch to fix broken wrapper script that doesnt pass arguments in 26.11
    patch("Fixed-arguments-not-being-passed-to-python-scripts.patch", when="@=26.11")

    # Patches to correct python script installation directory
    patch("Fix_python_install_25.patch", when="@25")
    patch("Fix_python_install_24.patch", when="@24")
    patch("Fix_python_install_23.patch", when="@23")

    @property
    def build_targets(self):
        """Generate targets for castep build stage"""
        targetlist = ["castep"]
        if self.spec.satisfies("+tools"):
            targetlist.append("tools")
        if self.spec.satisfies("+utilities"):
            targetlist.append("utilities")
        return targetlist

    def cmake_args(self):
        """
        Generate cmake arguments for castep configure stage.
        lapack/blas/fft names are translated into their internal variants.
        """

        # Internal names for blas libraries
        castep_math_libs = {
            "openblas": "OpenBLAS",
            "intel-oneapi-mkl": "Intel",
            "atlas": "ATLAS",
            "flexiblas": "FlexiBLAS",
            "libflame": "FLAME",
            "amdlibflame": "FLAME",
            "nvhpc": "NVHPC",
            "cray-libsci": "SciLib",
            "blis": "BLIS",
            "amdblix": "BLIS",
            "essl": "ESSL",
        }

        # Internal name for fft libraries
        castep_fft_libs = {"intel-oneapi-mkl": "mkl", "fftw": "fftw3"}

        args = [
            "-DBUILD={0}".format(self.spec.variants["build_type"].value),
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_LIBXC", "libxc"),
            self.define_from_variant("WITH_OpenMP", "openmp"),
            self.define_from_variant("WITH_GRIMMED3", "grimmed3"),
            self.define_from_variant("WITH_GRIMMED4", "grimmed4"),
            self.define_from_variant("WITH_DLMG", "dlmg"),
            self.define("WITH_MACE", False),  # Seems to be broken
        ]

        # Specify lapack/blas and fftw precisely if known
        mathlib = castep_math_libs.get(self.spec["blas"].name, None)
        if mathlib:
            args.append(self.define("MATHLIBS", mathlib))

        fftlib = castep_fft_libs.get(self.spec["fftw-api"].name, None)
        if fftlib:
            args.append(self.define("FFT", fftlib))

        return args

    @property
    def castep_exe(self):
        """Get the main executable filename"""
        if self.spec.satisfies("+mpi"):
            return "castep.mpi"
        else:
            return "castep.serial"

    @property
    def sanity_check_is_file(self):
        """List of files to check on a completed install"""
        # Main castep executable
        bin_files = [self.castep_exe]

        # Fortran tool check
        if self.spec.satisfies("+tools"):
            bin_files.append("phonon_kpoints")

        if self.spec.satisfies("+utilities"):
            # Python script check
            bin_files.append("cif2cell")

            # Perl script check
            bin_files.append("dos.pl")

        return [join_path("bin", f) for f in bin_files]

    #################################################
    # Tests that are run at build/installation time #
    #################################################

    def check(self) -> None:
        """Run the check-quick target."""
        with working_dir(self.build_directory):
            if self.generator == "Unix Makefiles":
                self._if_make_target_execute("check-quick")
            elif self.generator == "Ninja":
                self._if_ninja_target_execute("check-quick")

    @run_after("install")
    @on_package_attributes(run_tests=True)
    def test_castep_executable(self):
        """Test that the executable launches and returns a version number"""
        spec_version = re.compile(r"CASTEP version: " + str(self.spec.version))
        castep = Executable(join_path(self.prefix.bin, self.castep_exe))
        output = castep("-v", output=str)
        check_outputs(spec_version, output)

    @run_after("install")
    def prepare_postinstal_tests(self):
        """Store a simple test of basic castep functionality"""
        cache_extra_test_sources(self, join_path("Test", "Electronic", "Si2-den"))

    ############################################
    # Tests that can be run at some later time #
    ############################################

    def test_castep_si2(self):
        """
        Run a simple Si2 test case and verify the total energy matches that from the benchmark
        """
        test_dir = join_path(
            self.test_suite.current_test_cache_dir, "Test", "Electronic", "Si2-den"
        )
        energy_re = re.compile(r"Final energy =\s+(\S+)\s+eV")
        seedname = "Si2-den-NCP"

        # Quick calculation only converges to 1e-6 so 100x that should always be safe
        relative_tolerance = 1e-4

        def get_energy_from_file(filename: str) -> float:
            with open(filename) as f:
                for line in f:
                    m = re.search(energy_re, line)
                    if m:
                        return float(m.group(1))
            raise KeyError(f"Total energy not found in {filename}")

        with working_dir(test_dir):
            # Get reference data
            bench_file = glob.glob("benchmark*param")[0]
            benchmark_energy = get_energy_from_file(bench_file)

            # Get castep data
            castep = which(self.castep_exe, required=True)
            castep(seedname)
            castep_file = f"{seedname}.castep"
            castep_energy = get_energy_from_file(castep_file)

            assert math.isclose(castep_energy, benchmark_energy, rel_tol=relative_tolerance), (
                f"Expected {benchmark_energy} eV, got {castep_energy} eV.\n"
                f"Output file: {join_path(test_dir, castep_file)}"
            )

    def test_elastics_wrapper(self):
        """Check that the python script elastics.py installed correctly"""
        if self.spec.satisfies("+utilities"):
            elastics = Executable(join_path(self.prefix.bin, "elastics.py"))
            elastics("-h")
        else:
            raise SkipTest("Test only available with utilities installed.")

    def test_castepconv_wrapper(self):
        """
        Check that the python script wrapper installed correctly and
        passes arguments for castepconv.py
        """
        if self.spec.satisfies("+utilities"):
            castepconv = Executable(join_path(self.prefix.bin, "castepconv.py"))
            castepconv("-h")
        else:
            raise SkipTest("Test only available with utilities installed.")

    # Utility functions
