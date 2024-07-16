# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Castep(MakefilePackage):
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

    version(
        "23.1.1", sha256="8d922c641c99fc6e4f5b4f7f2478abab897065850e454fb4968154ddbb566388",
        url=f"file://{os.getcwd()}/castep-23.1.1.tar.bz2"
    
    )
    version("21.11", sha256="d909936a51dd3dff7a0847c2597175b05c8d0018d5afe416737499408914728f")
    version(
        "20.1", sha256="fa0f615ed1992ebf583ed3a2a4596085c2ebd59530271e70cc3a36789ba8180b",
        url=f"file://{os.getcwd()}/castep-20.1.tar.xz"
    )
    version(
        "19.1.1.rc2", sha256="1fce21dc604774e11b5194d5f30df8a0510afddc16daf3f8b9bbb3f62748f86a"
    )

    variant("mpi", default=True, description="Enable MPI build")
    #variant("xml", default=False, description="Enable CML, link against FoX libraries")
    variant("grimmed3", default=False, description="Enable Grimme DFT+D library")

    variant("grimmed4", default=False, when="@23:", description="Enable Grimme D4 library")

    variant(
        "libxc", default=False, when="@23:",
        description="Enable libxc library of additional XC functionals"
    )

    depends_on("rsync", type="build")
    depends_on("blas")
    depends_on("lapack")
    depends_on("fftw-api")
    depends_on("perl", type=("build", "run"))
    depends_on("mpi", type=("build", "link", "run"), when="+mpi")
    depends_on("libxc", type=("build", "link", "run"), when="+libxc")

    # don't have a FoX package atm, only C++ fox-toolkit
    #depends_on("fox-fortran", type=("build", "link", "run"), when="+xml")

    parallel = True

    # dl_mg is 2.0.3 for 20.1, 21.11; then 3.0.0 for 23.1.
    # There is a base linux_x86_64_gfortran.mk and a gfortran9.0.mk for 19, then a 
    # gfortran10.mk for 20.1 onwards.
    def edit(self, spec, prefix):
        if spec.satisfies("%gcc"):
            if self.spec.satisfies("@19:21"):
                dlmakefile = FileFilter("LibSource/dl_mg-2.0.3/platforms/castep.inc")
            elif self.spec.satisfies("@23:"):
                dlmakefile = FileFilter("LibSource/dl_mg-3.0.0/platforms/castep.inc")

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

        if "+grimmed4" in spec:
            targetlist.append("GRIMMED4=compile")

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
                    if self.spec.satisfies("@20:"):
                        targetlist.append("ARCH=linux_x86_64_gfortran")
                    else:
                        targetlist.append("ARCH=linux_x86_64_gfortran9.0")
                if spec.satisfies("%intel"):
                    if self.spec.satisfies("@20:"):
                        targetlist.append("ARCH=linux_x86_64_ifort")
                    else:
                        targetlist.append("ARCH=linux_x86_64_ifort19")

        return targetlist

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        make("install", "install-tools", *self.build_targets, "INSTALL_DIR={0}".format(prefix.bin))
