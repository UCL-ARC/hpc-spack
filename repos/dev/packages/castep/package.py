# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Castep(CMakePackage, MakefilePackage):
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
    url = f"file://{os.getcwd()}/CASTEP-21.11.tar.gz"
    manual_download = True

    
    version("24.1", sha256="97d77a4f3ce3f5c5b87e812f15a2c2cb23918acd7034c91a872b6d66ea0f7dbb")
    version("23.1", sha256="7fba0450d3fd71586c8498ce51975bbdde923759ab298a656409280c29bf45b5")
    version("21.11", sha256="d909936a51dd3dff7a0847c2597175b05c8d0018d5afe416737499408914728f")
    version(
        "20.1", sha256="fa0f615ed1992ebf583ed3a2a4596085c2ebd59530271e70cc3a36789ba8180b",
        url=f"file://{os.getcwd()}/castep-20.1.tar.xz"
    )
    version(
        "19.1.1.rc2", sha256="1fce21dc604774e11b5194d5f30df8a0510afddc16daf3f8b9bbb3f62748f86a"
    )

    variant("mpi", default=True, description="Enable MPI build")
    #variant("foxcml", default=False, description="Enable CML, link against FoX libraries")
    variant("grimmed3", default=True, description="Enable Grimme DFT+D library")

    variant("grimmed4", default=True, when="@23:", description="Enable Grimme D4 library")
    variant("dlmg", default=True, description="Enable DLMG Functionality functionals")

    variant(
        "libxc", default=False, when="@23:",
        description="Enable libxc library of additional XC functionals"
    )

    variant("openmp", default=True, when="build_system=cmake", description="Enable OpenMP"),

    # Patch available alongside source, manual download
    patch(
        f"file://{os.getcwd()}/Castep_23.1_build_fixes.diff.gz",
        sha256="a7860dc6677955d9bc877859666c4e8aa59635723968661674283a3939d7a66b",
        archive_sha256="5f31daf4733f8ee906cba0ff092e317b9cbaa100666533b2dce39f1f829646c2",
        when="@23.1",
    )

    # Patches the cmake install step for libxc's mod files.
    patch("castep_cmake_libxc523.patch", when="@24")
    patch("castep_cmake_libxc522.patch", when="@23")

    build_system(
        conditional("cmake", when="@23:"),
        conditional("makefile", when="@:0.22"),
        default="cmake",
    )

    with when("build_system=cmake"):
        depends_on("cmake@3.18:", type="build")

    depends_on("rsync", type="build")
    #depends_on("fortran", type="build")
    #depends_on("c", type="build") # for Utility
    depends_on("blas")
    depends_on("lapack")
    depends_on("fftw-api")
    depends_on("perl", type=("build", "run"))
    depends_on("python@3", type=("build", "run"))
    depends_on("mpi", type=("build", "link", "run"), when="+mpi")

    # castep strongly prefers to build libxc itself - would also need -DEXTERNAL_LIBXC_LIBRARY=ON
    # or make equivalent and ensure it can find the include files.
    #depends_on("libxc@5.2", type=("build", "link", "run"), when="+libxc")

    # don't have a FoX CML package atm, only C++ fox-toolkit
    #depends_on("foxcml", type=("build", "link", "run"), when="+foxcml")

    parallel = True


class CMakeBuilder(spack.build_systems.cmake.CMakeBuilder):

    # Is ok with default subdir build but requires -B to be set.
    def cmake_args(self):
        args = [
            "-B .",
            self.define_from_variant("WITH_MPI", "mpi"),
            self.define_from_variant("WITH_LIBXC", "libxc"),
            self.define_from_variant("WITH_OpenMP", "openmp"),
            #self.define_from_variant("WITH_FOXCML", "foxcml"),
            #self.define_from_variant("WITH_QUIP", "quip"),
            self.define_from_variant("WITH_GRIMMED3", "grimmed3"),
            self.define_from_variant("WITH_GRIMMED4", "grimmed4"),
            self.define_from_variant("WITH_DLMG", "dlmg"),
        ]
        return args


class MakefileBuilder(spack.build_systems.makefile.MakefileBuilder):

    # dl_mg is 2.0.3 for 20.1, 21.11; then 3.0.0 for 23.1.
    # There is a base linux_x86_64_gfortran.mk and a gfortran9.0.mk for 19, then a 
    # gfortran10.mk for 20.1 onwards.
    def edit(self, spec, prefix):
        if spec.satisfies("%gcc"):
            if self.spec.satisfies("@19:21"):
                dlmakefile = FileFilter("LibSource/dl_mg-2.0.3/platforms/castep.inc")
            #elif self.spec.satisfies("@23:"):
            #    dlmakefile = FileFilter("LibSource/dl_mg-3.0.0/platforms/castep.inc")

            if self.spec.satisfies("@20:"):
                if spec.satisfies("%gcc@10:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran10.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
                    platfile.filter(r"^\s*FFLAGS_E\s*=.*", "FFLAGS_E = -fallow-argument-mismatch ")
            elif self.spec.satisfies("@19"):
                if spec.satisfies("%gcc@9:"):
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran9.0.mk")
                else:
                    platfile = FileFilter("obj/platforms/linux_x86_64_gfortran.mk")
                dlmakefile.filter(r"MPIFLAGS = -DMPI", "MPIFLAGS = -fallow-argument-mismatch -DMPI")
                platfile.filter(r"^\s*FFLAGS_E\s*=.*", "FFLAGS_E = -fallow-argument-mismatch ")

            platfile.filter(r"^\s*OPT_CPU\s*=.*", "OPT_CPU = ")

        elif spec.satisfies("%intel"):
            if self.spec.satisfies("@20:"):
                platfile = FileFilter("obj/platforms/linux_x86_64_ifort.mk")
            else:
                platfile = FileFilter("obj/platforms/linux_x86_64_ifort19.mk")
            platfile.filter(r"^\s*OPT_CPU\s*=.*", "OPT_CPU = ")

    @property
    def build_targets(self):
        spec = self.spec
        targetlist = [f"PWD={self.stage.source_path}"]

        if "+mpi" in spec:
            targetlist.append("COMMS_ARCH=mpi")

        # "system" for existing libxc, "compile" to build own
        if "+libxc" in spec:
            targetlist.append("LIBXC=system")

        if "+grimmed3" in spec:
            targetlist.append("GRIMMED3=compile")
        else:
            targetlist.append("GRIMMED3=none")

        if "+grimmed4" in spec:
            targetlist.append("GRIMMED4=compile")
        else:
            targetlist.append("GRIMMED4=none")

        if "+dlmg" in spec:
            targetlist.append("DL_MG=compile")
        else:
            targetlist.append("DL_MG=none")

        targetlist.append(f"FFTLIBDIR={spec['fftw-api'].prefix.lib}")
        targetlist.append(f"MATHLIBDIR={spec['blas'].prefix.lib}")

        if "^mkl" in spec:
            targetlist.append("FFT=mkl")
            if self.spec.satisfies("@20:"):
                targetlist.append("MATHLIBS=mkl")
            else:
                targetlist.append("MATHLIBS=mkl10")
        else:
            targetlist.append("FFT=fftw3")
            targetlist.append("MATHLIBS=openblas")

        if spec.satisfies("target=x86_64:"):
            if spec.satisfies("platform=linux"):
                if spec.satisfies("%gcc"):
                    if self.spec.satisfies("@20:") and spec.satisfies("%gcc@10:"):
                        targetlist.append("ARCH=linux_x86_64_gfortran10")
                    elif self.spec.satisfies("@19") and spec.satisfies("%gcc@9:"):
                        targetlist.append("ARCH=linux_x86_64_gfortran9.0")
                    else:
                        targetlist.append("ARCH=linux_x86_64_gfortran")
                if spec.satisfies("%intel"):
                    if self.spec.satisfies("@20:"):
                        targetlist.append("ARCH=linux_x86_64_ifort")
                    else:
                        targetlist.append("ARCH=linux_x86_64_ifort19")

        return targetlist

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make("install", "install-tools", *self.build_targets, "INSTALL_DIR={0}".format(prefix.bin))
