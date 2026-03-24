# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# UCL: added oneapi and intel compiler arch files to edit(), readd 5.x and vaspsol
#      Assumes no attempt to build less than 6.3.0 with cuda, nvhpc
import os

from spack_repo.builtin.build_systems.cuda import CudaPackage
from spack_repo.builtin.build_systems.makefile import MakefilePackage

from spack.package import *


class Vasp(MakefilePackage, CudaPackage):
    """
    The Vienna Ab initio Simulation Package (VASP)
    is a computer program for atomic scale materials modelling,
    e.g. electronic structure calculations
    and quantum-mechanical molecular dynamics, from first principles.
    """

    homepage = "https://vasp.at"
    url = "file://{0}/vasp.5.4.4.pl2.tgz".format(os.getcwd())
    maintainers("snehring")
    manual_download = True

    version("6.5.1", sha256="a53fd9dd2a66472a4aa30074dbda44634fc663ea2628377fc01d870e37136f61")
    version("6.5.0", sha256="7836f0fd2387a6768be578f1177e795dc625f36f19015e31cab0e81154a24196")
    version("6.4.3", sha256="fe30e773f2a3e909b5e0baa9654032dfbdeff7ec157bc348cee7681a7b6c24f4")
    version("6.4.2", sha256="b704637f7384673f91adfbc803edc5cc7fe736d9623453461f7cdc29b123410e")
    version("6.3.2", sha256="f7595221b0f9236a324ea8afe170637a578cdd5a837cc7679e7f7812f6edf25a")
    version("6.3.1", sha256="113db53c4346287c89982f52887a65d12d246e38de7ccd024e44499c4774dc66")
    version("6.3.0", sha256="adcf83bdfd98061016baae31616b54329563aa2739573f069dd9df19c2071ad3")
    version(
        "5.4.4.pl2",
        sha256="98f75fd75399a23d76d060a6155f4416b340a1704f256a00146f89024035bc8e",
    )
    version(
        "5.4.4",
        sha256="5bd2449462386f01e575f9adf629c08cb03a13142806ffb6a71309ca4431cfb3",
    )

    resource(
        name="vaspsol",
        git="https://github.com/henniggroup/VASPsol.git",
        tag="V1.0",
        when="+vaspsol",
    )

    variant("openmp", default=False, when="@6:", description="Enable openmp build")

    variant("scalapack", default=False, when="@:5", description="Enables build with SCALAPACK")

    variant("cuda", default=False, description="Enables running on Nvidia GPUs")
    variant("fftlib", default=True, when="+openmp", description="Enables fftlib build")

    variant(
        "vaspsol",
        default=False,
        when="@:6.2",
        description="Enable VASPsol implicit solvation model\n"
        "https://github.com/henniggroup/VASPsol",
    )
    variant("shmem", default=True, description="Enable use_shmem build flag")
    variant("hdf5", default=False, when="@6.2:", description="Enabled HDF5 support")
    variant("libbeef", default=False, description="Enable Libbeef support")
    variant("libxc", default=False, description="Enable Libxc support")
    variant("wannier90", default=False, description="Enable wannier90 support")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build")

    depends_on("rsync", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("fftw-api")
    depends_on("fftw+openmp", when="+openmp ^[virtuals=fftw-api] fftw")
    depends_on("amdfftw+openmp", when="+openmp ^[virtuals=fftw-api] amdfftw")
    depends_on("amdblis threads=openmp", when="+openmp ^[virtuals=blas] amdblis")
    depends_on("openblas threads=openmp", when="+openmp ^[virtuals=blas] openblas")
    depends_on("mpi", type=("build", "link", "run"))
    # fortran oddness requires the below
    depends_on("openmpi%aocc", when="%aocc ^[virtuals=mpi] openmpi")
    depends_on("openmpi%gcc", when="%gcc ^[virtuals=mpi] openmpi")
    depends_on("scalapack", when="+scalapack")
    depends_on("scalapack", when="@6:")
    depends_on("nccl", when="+cuda")
    depends_on("hdf5+fortran+mpi", when="+hdf5")
    depends_on("libbeef", when="+libbeef")
    depends_on("libxc~fhc+fortran", when="+libxc")
    depends_on("wannier90", when="+wannier90")
    # at the very least the nvhpc mpi seems required
    requires("^nvhpc+mpi+lapack+blas", when="%nvhpc")

    conflicts(
        "%gcc@:8", msg="GFortran before 9.x does not support all features needed to build VASP"
    )
    conflicts("+vaspsol", when="+cuda", msg="+vaspsol only available for CPU")
    requires("%nvhpc", when="+cuda", msg="vasp requires nvhpc to build the openacc build")
    # the mpi compiler wrappers in nvhpc assume nvhpc is the underlying compiler, seemingly
    conflicts("^[virtuals=mpi] nvhpc", when="%gcc", msg="nvhpc mpi requires nvhpc compiler")
    conflicts("^[virtuals=mpi] nvhpc", when="%aocc", msg="nvhpc mpi requires nvhpc compiler")
    conflicts("cuda_arch=none", when="+cuda", msg="CUDA arch required when building openacc port")

    def edit(self, spec, prefix):
        cpp_options = [
            "-DMPI",
            "-DMPI_BLOCK=8000",
            "-Duse_collective",
            "-DCACHE_SIZE=4000",
            "-Davoidalloc",
            "-Duse_bse_te",
            "-Dtbdyn",
            "-Dfock_dblbuf",
        ]
        objects_lib = ["linpack_double.o"]
        llibs = list(self.compiler.stdcxx_libs)
        cflags = ["-fPIC", "-DAAD_"]
        fflags = ["-w"]
        incs = [spec["fftw-api"].headers.include_flags]

        if self.spec.satisfies("@6:"):
            cpp_options.append("-Dvasp6")

        llibs.extend([spec["blas"].libs.ld_flags, spec["lapack"].libs.ld_flags])

        fc = [spec["mpi"].mpifc]
        fcl = [spec["mpi"].mpifc]

        include_prefix = ""
        omp_flag = "-fopenmp"

        if spec.satisfies("+shmem"):
            cpp_options.append("-Duse_shmem")
            objects_lib.append("getshmem.o")

        if spec.satisfies("@:6.2"):
            include_prefix = "linux_"
        include_string = f"makefile.include.{include_prefix}"

        # gcc
        if spec.satisfies("%gcc"):
            include_string += "gnu"
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            make_include = join_path("arch", include_string)

        # intel-oneapi 2024.0 ono - use oneapi arch file
        elif spec.satisfies("@6.3.0: %oneapi@2024.0:"):
            include_string += "oneapi"
            # does not pick up MKL's include/fftw otherwise
            incs.append(join_path(spec["fftw-api"].headers.include_flags, "fftw"))
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            make_include = join_path("arch", include_string)

        # intel-oneapi 2023 and earlier - use intel arch file
        elif spec.satisfies("%oneapi@:2023.2.4"):
            include_string += "intel"
            # does not pick up MKL's include/fftw otherwise
            incs.append(join_path(spec["fftw-api"].headers.include_flags, "fftw"))
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            make_include = join_path("arch", include_string)

        # intel classic or older vasp with oneapi
        elif spec.satisfies("%intel") or spec.satisfies("@:6.2 %oneapi"):
            include_string += "intel"
            # does not pick up MKL's include/fftw otherwise
            incs.append(join_path(spec["fftw-api"].headers.include_flags, "fftw"))
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            make_include = join_path("arch", include_string)
            # where icc and icpc no longer exist
            if spec.satisfies("@:6.2 %oneapi@2024.0:"):
                # not compatible with c++17
                filter_file("icc", spack_cc, make_include)
                filter_file("icpc", spack_cxx + " -std=c++14", make_include)
                llibs.extend(["-Lparser", "-lparser"])

        # nvhpc
        elif spec.satisfies("%nvhpc"):
            qd_root = join_path(
                spec["nvhpc"].prefix,
                f"Linux_{spec['nvhpc'].target.family.name}",
                str(spec["nvhpc"].version.dotted),
                "compilers",
                "extras",
                "qd",
            )
            nvroot = join_path(spec["nvhpc"].prefix, f"Linux_{spec['nvhpc'].target.family.name}")
            cpp_options.extend(['-DHOST=\\"LinuxNV\\"', "-Dqd_emulate"])

            fflags.extend(["-Mnoupcase", "-Mbackslash", "-Mlarge_arrays"])
            incs.append(f"-I{join_path(qd_root, 'include', 'qd')}")
            llibs.extend([f"-L{join_path(qd_root, 'lib')}", "-lqdmod", "-lqd"])

            include_string += "nvhpc"
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            if spec.satisfies("+cuda"):
                include_string += "_acc"
            make_include = join_path("arch", include_string)
            omp_flag = "-mp"
            filter_file(r"^QD[ \t]*\??=.*$", f"QD = {qd_root}", make_include)
            filter_file("NVROOT[ \t]*=.*$", f"NVROOT = {nvroot}", make_include)
        # aocc
        elif spec.satisfies("%aocc"):
            cpp_options.extend(['-DHOST=\\"LinuxAMD\\"', "-Dshmem_bcast_buffer", "-DNGZhalf"])
            fflags.extend(["-fno-fortran-main", "-Mbackslash", "-ffunc-args-alias"])
            if spec.satisfies("^amdfftw@4.0:"):
                cpp_options.extend(["-Dfftw_cache_plans", "-Duse_fftw_plan_effort"])
            if spec.satisfies("+openmp"):
                if spec.satisfies("@6.3.2:"):
                    include_string += "aocc_ompi_aocl_omp"
                elif spec.satisfies("@=6.3.0"):
                    include_string += "gnu_ompi_aocl_omp"
                else:
                    include_string += "gnu_omp"
            else:
                if spec.satisfies("@6.3.2:"):
                    include_string += "aocc_ompi_aocl"
                elif spec.satisfies("@=6.3.0"):
                    include_string += "gnu_ompi_aocl"
                else:
                    include_string += "gnu"
            make_include = join_path("arch", include_string)
            filter_file("^CC_LIB[ ]{0,}=.*$", f"CC_LIB={spack_cc}", make_include)
            if spec.satisfies("@6:6.3.0"):
                filter_file("gcc", f"{spack_fc} -Mfree", make_include, string=True)
                filter_file(
                    "-fallow-argument-mismatch", " -fno-fortran-main", make_include, string=True
                )
        # fj
        elif spec.satisfies("@6.4.3: target=a64fx %fj"):
            include_string += "fujitsu_a64fx"
            omp_flag = "-Kopenmp"
            fc.extend(["simd_nouse_multiple_structures", "-X03"])
            fcl.append("simd_nouse_multiple_structures")
            cpp_options.append('-DHOST=\\"FJ-A64FX\\"')
            fflags.append("-Koptmsg=2")
            llibs.extend(["-SSL2BLAMP", "-SCALAPACK"])
            if spec.satisfies("+openmp"):
                include_string += "_omp"
            make_include = join_path("arch", include_string)

        else:
            if spec.satisfies("+openmp"):
                make_include = join_path("arch", f"{include_string}{spec.compiler.name}_omp")
                # if the above doesn't work, fallback to gnu
                if not os.path.exists(make_include):
                    make_include = join_path("arch", f"{include_string}.gnu_omp")
            else:
                make_include = join_path(
                    "arch", f"{include_string}{include_prefix}" + spec.compiler.name
                )
                if not os.path.exists(make_include):
                    make_include = join_path("arch", f"{include_string}.gnu")
            cpp_options.append('-DHOST=\\"LinuxGNU\\"')

        if spec.satisfies("+openmp"):
            cpp_options.extend(["-Dsysv", "-D_OPENMP"])
            llibs.extend(["-ldl", spec["fftw-api:openmp"].libs.ld_flags])
            fc.append(omp_flag)
            fcl.append(omp_flag)
        else:
            llibs.append(spec["fftw-api"].libs.ld_flags)

        if spec.satisfies("^scalapack"):
            cpp_options.append("-DscaLAPACK")
            if spec.satisfies("%nvhpc"):
                llibs.append("-Mscalapack")
            else:
                llibs.append(spec["scalapack"].libs.ld_flags)

        if spec.satisfies("+cuda"):
            # openacc
            if spec.satisfies("@6.5.0:"):
                cpp_options.extend(["-DACC_OFFLOAD", "-DNVCUDA", "-DUSENCCL"])
            else:
                cpp_options.extend(["-D_OPENACC", "-DUSENCCL"])
            llibs.extend(["-cudalib=cublas,cusolver,cufft,nccl", "-cuda"])
            fc.append("-acc")
            fcl.append("-acc")
            cuda_flags = [f"cuda{str(spec['cuda'].version.dotted[0:2])}", "rdc"]
            for f in spec.variants["cuda_arch"].value:
                cuda_flags.append(f"cc{f}")
            fc.append(f"-gpu={','.join(cuda_flags)}")
            fcl.append(f"-gpu={','.join(cuda_flags)}")
            fcl.extend(list(self.compiler.stdcxx_libs))
            cc = [spec["mpi"].mpicc, "-acc"]
            if spec.satisfies("+openmp"):
                cc.append(omp_flag)
            filter_file("^CC[ \t]*=.*$", f"CC = {' '.join(cc)}", make_include)

        if spec.satisfies("+vaspsol"):
            cpp_options.append("-Dsol_compat")
            copy("VASPsol/src/solvation.F", "src/")

        if spec.satisfies("+hdf5"):
            cpp_options.append("-DVASP_HDF5")
            llibs.append(spec["hdf5:fortran"].libs.ld_flags)
            incs.append(spec["hdf5"].headers.include_flags)

        if spec.satisfies("+libbeef"):
            cpp_options.append("-Dlibbeef")
            llibs.append(spec["libbeef"].libs.ld_flags)

        if spec.satisfies("+libxc"):
            cpp_options.append("-DUSELIBXC")
            llibs.append(spec["libxc:fortran"].libs.ld_flags)
            incs.append(spec["libxc"].headers.include_flags)

        if spec.satisfies("+wannier90"):
            cpp_options.append("-DVASP2WANNIER90")
            llibs.append(spec["wannier90"].libs.ld_flags)

        if spec.satisfies("%gcc@10:"):
            fflags.append("-fallow-argument-mismatch")

        filter_file(r"^VASP_TARGET_CPU[ ]{0,}\?=.*", "", make_include)

        if spec.satisfies("@:5"):
            filter_file("-DscaLAPACK.*$\n", "", make_include)

        if spec.satisfies("+fftlib"):
            cxxftlib = (
                f"CXX_FFTLIB = {spack_cxx} {omp_flag}"
                f" -DFFTLIB_THREADSAFE{' '.join(list(self.compiler.stdcxx_libs))}"
            )
            filter_file("^#FCL[ ]{0,}=fftlib.o", "FCL += fftlib/fftlib.o", make_include)
            filter_file("^#CXX_FFTLIB.*$", cxxftlib, make_include)
            filter_file(
                "^#INCS_FFTLIB.*$",
                f"INCS_FFTLIB = -I./include {spec['fftw-api'].headers.include_flags}",
                make_include,
            )
            filter_file(r"#LIBS[ \t]*\+=.*$", "LIBS = fftlib", make_include)
            llibs.append("-ldl")
            fcl.append(join_path("fftlib", "fftlib.o"))

        # clean multiline CPP options at begining of file
        filter_file(r"^[ \t]+(-D[a-zA-Z0-9_=]+[ ]*)+[ ]*\\*$", "", make_include)
        # replace relevant variables in the makefile.include
        filter_file("^FFLAGS[ \t]*=.*$", f"FFLAGS = {' '.join(fflags)}", make_include)
        filter_file(r"^FFLAGS[ \t]*\+=.*$", "", make_include)
        filter_file(
            "^CPP_OPTIONS[ \t]*=.*$", f"CPP_OPTIONS = {' '.join(cpp_options)}", make_include
        )
        filter_file(r"^INCS[ \t]*\+?=.*$", f"INCS = {' '.join(incs)}", make_include)
        filter_file(r"^LLIBS[ \t]*\+?=.*$", f"LLIBS = {' '.join(llibs)}", make_include)
        filter_file(r"^LLIBS[ \t]*\+=[ ]*-.*$", "", make_include)
        filter_file("^CFLAGS[ \t]*=.*$", f"CFLAGS = {' '.join(cflags)}", make_include)
        filter_file(
            "^OBJECTS_LIB[ \t]*=.*$", f"OBJECTS_LIB = {' '.join(objects_lib)}", make_include
        )
        filter_file("^FC[ \t]*=.*$", f"FC = {' '.join(fc)}", make_include)
        filter_file("^FCL[ \t]*=.*$", f"FCL = {' '.join(fcl)}", make_include)

        os.rename(make_include, "makefile.include")

    def setup_build_environment(self, env: EnvironmentModifications) -> None:
        if self.spec.satisfies("+cuda %nvhpc"):
            env.set("NVHPC_CUDA_HOME", self.spec["cuda"].prefix)

    def build(self, spec, prefix):
        # 5.x does not build successfully in parallel
        if spec.satisfies("@:5"):
            make("DEPS=1", "std", "gam", "ncl", parallel = False)
        else:
            make("DEPS=1, all")

    def install(self, spec, prefix):
        install_tree("bin/", prefix.bin)
