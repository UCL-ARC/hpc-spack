# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

#from spack_repo.builtin.build_systems.generic import Package

from spack.package import *


class Mrtrix3(Package):
    """MRtrix provides a set of tools to perform various advanced diffusion MRI
    analyses, including constrained spherical deconvolution (CSD),
    probabilistic tractography, track-density imaging, and apparent fibre
    density."""

    homepage = "https://www.mrtrix.org/"
    url = "wget https://github.com/MRtrix3/mrtrix3/archive/refs/tags/3.0.8.tar.gz"
    git = "https://github.com/MRtrix3/mrtrix3.git"

    license("MPL-2.0")

    version(
        "3.0.8",
        sha256="v9c694934781c287c51a0d35ad5d7687b529e5c04e3b2ac0985599b0c48644721",
        preferred=True,
    )

    depends_on("cxx", type="build")  # generated

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    #depends_on("glu")
    depends_on("qt@4.7:")
    depends_on("harfbuzz@9.0.0")
    # MRTrix <= 3.0.3 can't build with eigen >= 3.4 due to conflicting declarations
    depends_on("eigen@3.3", when="@3.0.3")
    depends_on("eigen@3.4:", when="@3.0.4:")
    depends_on("zlib-api")
    depends_on("libtiff")
    depends_on("fftw")

    patch("fix_includes.patch", when="@3.0.3:3.0.4")

    conflicts("%gcc@7:", when="@2017-09-25")  # MRtrix3/mrtrix3#1041

    def install(self, spec, prefix):
        configure = Executable("./configure")
        build = Executable("./build")
        configure()
        build()
        install_tree(".", prefix)

    def setup_run_environment(self, env) -> None:
        env.prepend_path("PATH", self.prefix)
