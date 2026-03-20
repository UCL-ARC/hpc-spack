# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
import itertools
import os
import re
import sys

import llnl.util.tty as tty

from spack.package import *


def slingshot_network():
    return os.path.exists("/opt/cray/pe") and (
        os.path.exists("/lib64/libcxi.so") or os.path.exists("/usr/lib64/libcxi.so")
    )


#@memoized
#def is_CrayEX():
#    # Credit to upcxx and chapel packages for this hpe-cray-ex detection function
#    if host_platform().name == "linux":
#        target = os.environ.get("CRAYPE_NETWORK_TARGET")
#        if target in ["ofi", "ucx"]:  # normal case
#            return True
#        elif target is None:  # but some systems lack Cray PrgEnv
#            fi_info = which("fi_info")
#            if (
#                fi_info
#                and fi_info("-l", output=str, error=str, fail_on_error=False).find("cxi") >= 0
#            ):
#                return True
#    return False



    version(
        "5.0.6", sha256="bd4183fcbc43477c254799b429df1a6e576c042e74a2d2f8b37d537b2ff98157"
    )  # libmpi.so.40.40.6
    version(
        "5.0.5", sha256="6588d57c0a4bd299a24103f4e196051b29e8b55fbda49e11d5b3d32030a32776"
    )  # libmpi.so.40.40.5
    version(
        "5.0.4", sha256="64526852cdd88b2d30e022087c16ab3e03806c451b10cd691d5c1ac887d8ef9d"
    )  # libmpi.so.40.40.4
    version(
        "5.0.3", sha256="990582f206b3ab32e938aa31bbf07c639368e4405dca196fabe7f0f76eeda90b"
    )  # libmpi.so.40.40.3
    version(
        "5.0.2", sha256="ee46ad8eeee2c3ff70772160bff877cbf38c330a0bc3b3ddc811648b3396698f"
    )  # libmpi.so.40.40.2
    version(
        "5.0.1", sha256="e357043e65fd1b956a47d0dae6156a90cf0e378df759364936c1781f1a25ef80"
    )  # libmpi.so.40.40.1
    version(
        "5.0.0", sha256="9d845ca94bc1aeb445f83d98d238cd08f6ec7ad0f73b0f79ec1668dbfdacd613"
    )  # libmpi.so.40.40.0

    # Still supported
    version(
        "4.1.8", sha256="466f68e3132a1dc02710cc2011fafced8336d98359fa2dae4dddcfd5719f12a9"
    )  # libmpi.so.40.30.8
    version(
        "4.1.7", sha256="54a33cb7ad81ff0976f15a6cc8003c3922f0f3d8ceed14e1813ef3603f22cd34"
    )  # libmpi.so.40.30.7
    version(
        "4.1.6", sha256="f740994485516deb63b5311af122c265179f5328a0d857a567b85db00b11e415"
    )  # libmpi.so.40.30.6
    version(
        "4.1.5", sha256="a640986bc257389dd379886fdae6264c8cfa56bc98b71ce3ae3dfbd8ce61dbe3"
    )  # libmpi.so.40.30.5
    version(
        "4.1.4", sha256="92912e175fd1234368c8730c03f4996fe5942e7479bb1d10059405e7f2b3930d"
    )  # libmpi.so.40.30.4
    version(
        "4.1.3", sha256="3d81d04c54efb55d3871a465ffb098d8d72c1f48ff1cbaf2580eb058567c0a3b"
    )  # libmpi.so.40.30.3
    version(
        "4.1.2", sha256="9b78c7cf7fc32131c5cf43dd2ab9740149d9d87cadb2e2189f02685749a6b527"
    )  # libmpi.so.40.30.2
    version(
        "4.1.1", sha256="e24f7a778bd11a71ad0c14587a7f5b00e68a71aa5623e2157bafee3d44c07cda"
    )  # libmpi.so.40.30.1
    ver
        )  # libmpi.so.40.20.0

        version(
            "3.1.5", sha256="fbf0075b4579685eec8d56d34d4d9c963e6667825548554f5bf308610af72133"
        )  # libmpi.so.40.10.4
        version(
            "3.1.4", sha256="17a69e0054db530c7dc119f75bd07d079efa147cf94bf27e590905864fe379d6"
        )  # libmpi.so.40.10.4
        version(
            "3.1.3", sha256="8be04307c00f51401d3fb9d837321781ea7c79f2a5a4a2e5d4eaedc874087ab6"
        )  # libmpi.so.40.10.3
        version(
            "3.1.2", sha256="c654ed847f34a278c52a15c98add40402b4a90f0c540779f1ae6c489af8a76c5"
        )  # libmpi.so.40.10.2
        version(
            "3.1.1", sha256="3f11b648dd18a8b878d057e9777f2c43bf78297751ad77ae2cef6db0fe80c77c"
        )  # libmpi.so.40.10.1
        version(
            "3.1.0", sha256="b25c044124cc859c0b4e6e825574f9439a51683af1950f6acda1951f5ccdf06c"
        )  # libmpi.so.40.10.0

        version(
            "3.0.4", sha256="2ff4db1d3e1860785295ab95b03a2c0f23420cda7c1ae845c419401508a3c7b5"
        )  # libmpi.so.40.00.5
        version(
            "3.0.3", sha256="fb228e42893fe6a912841a94cd8a0c06c517701ae505b73072409218a12cf066"
        )  # libmpi.so.40.00.4
        version(
            "3.0.2", sha256="d2eea2af48c1076c53cabac0a1f12272d7470729c4e1cb8b9c2ccd1985b2fb06"
        )  # libmpi.so.40.00.2
        version(
            "3.0.1", sha256="663450d1ee7838b03644507e8a76edfb1fba23e601e9e0b5b2a738e54acd785d"
        )  # libmpi.so.40.00.1
        version(
            "3.0.0", sha256="f699bff21db0125d8cccfe79518b77641cd83628725a1e1ed3e45633496a82d7"
        )  # libmpi.so.40.00.0

        version(
            "2.1.5", sha256="b807ccab801f27c3159a5edf29051cd3331d3792648919f9c4cee48e987e7794"
        )  # libmpi.so.20.10.3
        version(
            "2.1.4", sha256="3e03695ca8bd663bc2d89eda343c92bb3d4fc79126b178f5ddcb68a8796b24e2"
        )  # libmpi.so.20.10.3
        version(
            "2.1.3", sha256="285b3e2a69ed670415524474496043ecc61498f2c63feb48575f8469354d79e8"
        )  # libmpi.so.20.10.2
        version(
            "2.1.2", sha256="3cc5804984c5329bdf88ef
            "1.10.1", sha256="7919ecde15962bab2e26d01d5f5f4ead6696bbcacb504b8560f2e3a152bfe492"
        )  # libmpi.so.12.0.1
        version(
            "1.10.0", sha256="26b432ce8dcbad250a9787402f2c999ecb6c25695b00c9c6ee05a306c78b6490"
        )  # libmpi.so.12.0.0

        version(
            "1.8.8", sha256="a28382d1e6a36f4073412dc00836ff2524e42b674da9caf6ca7377baad790b94"
        )  # libmpi.so.1.6.3
        version(
            "1.8.7", sha256="da629e9bd820a379cfafe15f842ee9b628d7451856085ccc23ee75ab3e1b48c7"
        )  # libmpi.so.1.6.2
        version(
            "1.8.6", sha256="b9fe3bdfb86bd42cc53448e17f11278531b989b05ff9513bc88ba1a523f14e87"
        )  # libmpi.so.1.6.1
        version(
            "1.8.5", sha256="4cea06a9eddfa718b09b8240d934b14ca71670c2dc6e6251a585ce948a93fbc4"
        )  # libmpi.so.1.6.0
        version(
            "1.8.4", sha256="23158d916e92c80e2924016b746a93913ba7fae9fff51bf68d5c2a0ae39a2f8a"
        )  # libmpi.so.1.6.0
        version(
            "1.8.3", sha256="2ef02dab61febeb74714ff80d508c00b05defc635b391ed2c8dcc1791fbc88b3"
        )  # libmpi.so.1.6.0
        version(
            "1.8.2", sha256="ab70770faf1bac15ef44301fe2186b02f857646545492dd7331404e364a7d131"
        )  # libmpi.so.1.5.2
        version(
            "1.8.1", sha256="171427ebc007943265f33265ec32e15e786763952e2bfa2eac95e3e192c1e18f"
        )  # libmpi.so.1.5.0
        version(
            "1.8", sha256="35d5db86f49c0c64573b2eaf6d51c94ed8a06a9bb23dda475e602288f05e4ecf"
        )  # libmpi.so.1.5.0

        version(
            "1.7.5", sha256="cb3eef6880537d341d5d098511d390ec853716a6ec94007c03a0d1491b2ac8f2"
        )  # libmpi.so.1.4.0
        version(
            "1.7.4", sha256="ff8e31046c5bacfc6202d67f2479731ccd8542cdd628583ae75874000975f45c"
        )  # libmpi.so.1.3.0
        version(
            "1.7.3", sha256="438d96c178dbf5a1bc92fa1d238a8225d87b64af26ce2a07789faaf312117e45"
        )  # libmpi.so.1.2.0
        version(
            "1.7.2", sha256="82a1c477dcadad2032ab24d9be9e39c1042865965841911f072c49aa3544fd85"
        )  # libmpi.so.1.1.2
        version(
            "1.7.1", sha256="554583008fa34ecdfaca22e46917cc3457
        version(
            "1.4.5", sha256="a3857bc69b7d5258cf7fc1ed1581d9ac69110f5c17976b949cb7ec789aae462d"
        )  # libmpi.so.0.0.4
        version(
            "1.4.4", sha256="9ad125304a89232d5b04da251f463fdbd8dcd997450084ba4227e7f7a095c3ed"
        )  # libmpi.so.0.0.3
        version(
            "1.4.3", sha256="220b72b1c7ee35469ff74b4cfdbec457158ac6894635143a33e9178aa3981015"
        )  # libmpi.so.0.0.2
        version(
            "1.4.2", sha256="19129e3d51860ad0a7497ede11563908ba99c76b3a51a4d0b8801f7e2db6cd80"
        )  # libmpi.so.0.0.2
        version(
            "1.4.1", sha256="d4d71d7c670d710d2d283ea60af50d6c315318a4c35ec576bedfd0f3b7b8c218"
        )  # libmpi.so.0.0.1
        version(
            "1.4", sha256="fa55edef1bd8af256e459d4d9782516c6998b9d4698eda097d5df33ae499858e"
        )  # libmpi.so.0.0.1

        version(
            "1.3.4", sha256="fbfe4b99b0c98f81a4d871d02f874f84ea66efcbb098f6ad84ebd19353b681fc"
        )  # libmpi.so.0.0.1
        version(
            "1.3.3", sha256="e1425853282da9237f5b41330207e54da1dc803a2e19a93dacc3eca1d083e422"
        )  # libmpi.so.0.0.0
        version(
            "1.3.2", sha256="c93ed90962d879a2923bed17171ed9217036ee1279ffab0925ea7eead26105d8"
        )  # libmpi.so.0.0.0
        version(
            "1.3.1", sha256="22d18919ddc5f49d55d7d63e2abfcdac34aa0234427e861e296a630c6c11632c"
        )  # libmpi.so.0.0.0
        version(
            "1.3", sha256="864706d88d28b586a045461a828962c108f5912671071bc3ef0ca187f115e47b"
        )  # libmpi.so.0.0.0

        version(
            "1.2.9", sha256="0eb36abe09ba7bf6f7a70255974e5d0a273f7f32d0e23419862c6dcc986f1dff"
        )  # libmpi.so.0.0.0
        version(
            "1.2.8", sha256="75b286cb3b1bf6528a7e64ee019369e0601b8acb5c3c167a987f755d1e41c95c"
        )  # libmpi.so.0.0.0
        version(
            "1.2.7", sha256="d66c7f0bb11494023451651d0e61afaef9d2199ed9a91ed08f0dedeb51541c36"
        )  # libmpi.so.0.0.0
        version(
            "1.2.6", sha256="e5b27af5a153a257b1562a97bbf7164629161033934558cefd8e1e644a9f73d3"
        )  # libmpi.so.0.0.0

        version(
            "1.0.2", sha256="ccd1074d7dd9566b73812d9882c84e446a8f4c77b6f471d386d3e3b9467767b8"
        )  # libmpi.so.0.0.0
        version(
            "1.0.1", sha256="f801b7c8ea6c485ac0709a628a479aeafa718a205ed6bc0cf2c684bc0cc73253"
        )  # libmpi.so.0.0.0
        version(
            "1.0", sha256="cf75e56852caebe90231d295806ac3441f37dc6d9ad17b1381791ebb78e21564"
        )  # libmpi.so.0.0.0

    depends_on("c", type="build")  # generated
    depends_on("cxx", type="build")  # generated
    depends_on("fortran", type="build")  # generated

    patch("ad_lustre_rwcontig_open_source.patch", when="@1.6.5")
    patch("llnl-platforms.patch", when="@1.6.5")
    patch("configure.patch", when="@1.10.1")
    patch("fix_multidef_pmi_class.patch", when="@2.0.0:2.0.1")
    patch("fix-ucx-1.7.0-api-instability.patch", when="@4.0.0:4.0.2")
    # see issue with gpfs #13313 on https://github.com/open-mpi/ompi and
    # commit https://github.com/open-mpi/ompi/commit/556014c
    patch("fix_fs_gpfs_file_set_info.patch", when="@4.1 +gpfs")

    # Vader Bug: https://github.com/open-mpi/ompi/issues/5375
    # Haven't release fix for 2.1.x
    patch("btl_vader.patch", when="@2.1.3:2.1.5")

    # Fixed in 3.0.3 and 3.1.3
    patch("btl_vader.patch", when="@3.0.1:3.0.2")
    patch("btl_vader.patch", when="@3.1.0:3.1.2")

    # Fix MPI_Sizeof() in the "mpi" Fortran module for compilers that do not
    # support "IGNORE TKR" functionality (e.g. NAG).
    # The issue has been resolved upstream in two steps:
    #   1) https://github.com/open-mpi/ompi/pull/2294
    #   2) https://github.com/open-mpi/ompi/pull/5099
    # The first one was applied starting version v3.0.0 and backported to
    # v1.10. A subset with relevant modifications is applicable starting
    # version 1.8.4.
    patch("use_mpi_tkr_sizeof/step_1.patch", when="@1.8.4:1.10.6,2.0:2")
    # The second patch was applied starting version v4.0.0 and backported to
    # v2.x, v3.0.x, and v3.1.x.
    patch("use_mpi_tkr_sizeof/step_2.patch", when="@1.8.4:2.1.3,3:3.0.1")
    # To fix performance regressions introduced while fixing a bug in older
    # gcc versions on x86_64, Refs. open-mpi/ompi#8603
    patch("opal_assembly_arch.patch", when="@4.0.0:4.0.5,4.1.0")
    # Fix reduce operations for unsigned long integers
    #
        ),  # shared memory transports
        description="List of fabrics that are enabled; 'auto' lets openmpi determine",
    )

    SCHEDULERS = ("alps", "lsf", "tm", "slurm", "sge", "loadleveler")

    variant(
        "schedulers",
        values=disjoint_sets(("auto",), SCHEDULERS).with_non_feature_values("auto", "none"),
        description="List of schedulers for which support is enabled; "
        "'auto' lets openmpi determine",
    )

    # Additional support options
    variant("atomics", default=True, description="Enable built-in atomics")
    variant("java", default=False, when="@1.7.4:", description="Build Java support")
    variant("static", default=False, description="Build static libraries")
    variant("sqlite3", default=False, when="@1.7.3:1", description="Build SQLite3 support")
    variant("vt", default=True, description="Build VampirTrace support")
    variant(
        "thread_multiple",
        default=False,
        when="@1.5.4:2",
        description="Enable MPI_THREAD_MULTIPLE support",
    )
    variant(
        "pmi", default=False, when="@1.5.5:4 schedulers=slurm", description="Enable PMI support"
    )
    variant(
        "wrapper-rpath",
        default=True,
        when="@1.7.4:",
        description="Enable rpath support in the wrappers",
    )
    variant("cxx", default=False, when="@:4", description="Enable deprecated C++ MPI bindings")
    variant(
        "cxx_exceptions",
        default=False,
        when="@:4",
        description="Enable deprecated C++ exception support",
    )
    variant("fortran", default=True, description="Enable Fortran support")
    variant("gpfs", default=False, description="Enable GPFS support")
    variant("lustre", default=False, description="Lustre filesystem library support")
    variant("romio", default=True, when="@:5", description="Enable ROMIO support")
    variant("romio", default=False, when="@5:", description="Enable ROMIO support")
    variant(
        "romio-filesystem
with '-Wl,-commons,use_dylibs' and without
'-Wl,-flat_namespace'.""",
    )

    variant(
        "cray-xpmem",
        default=False,
        when="fabrics=xpmem",
        description="use cray-xpmem instead of xpmem configure flag",
    )

    # Patch to allow two-level namespace on a MacOS platform when building
    # openmpi. Unfortuntately, the openmpi configure command has flat namespace
    # hardwired in. In spack, this only works for openmpi up to versions 4,
    # because for versions 5+ autoreconf is triggered (see below) and this
    # patch needs to be applied (again) AFTER autoreconf ran.
    @when("+two_level_namespace platform=darwin")
    def patch(self):
        filter_file(r"-flat_namespace", "-commons,use_dylibs", "configure")

    provides("mpi@:2.0", when="@:1.2")
    provides("mpi@:2.1", when="@1.3:1.7.2")
    provides("mpi@:2.2", when="@1.7.3:1.7.4")
    provides("mpi@:3.0", when="@1.7.5:1.10.7")
    provides("mpi@:3.1", when="@2.0.0:")

    depends_on("c", type="build")
    depends_on("cxx", type="build")
    depends_on("fortran", type="build", when="+fortran")

    if sys.platform != "darwin":
        depends_on("numactl")

    depends_on("autoconf @2.69:", type="build", when="@5.0.0:,main")
    depends_on("automake @1.13.4:", type="build", when="@5.0.0:,main")
    depends_on("libtool @2.4.2:", type="build", when="@5.0.0:,main")

    depends_on("perl", type="build")
    depends_on("pkgconfig", type="build")
    # Based on https://docs.open-mpi.org/en/v5.0.x/developers/prerequisites.html#flex
    depends_on("flex@2.5.4:", type="build", when="@main")

    depends_on("hwloc@2:", when="@4: ~internal-hwloc")
    # ompi@:3.0.0 doesn't support newer hwloc releases:
    # "configure: error: OMPI does not currently support hwloc v2 API"
    # Future ompi releases may support it, needs to be verified.
    # See #7483 for context.
    depends_on("hwloc@:1", when="@
    # OpenMPI @2: includes a vendored version:
    with when("~internal-pmix"):
        depends_on("pmix", when="@3:")
        depends_on("pmix@3.2:", when="@4:")
        depends_on("pmix@4.2.4:", when="@5:")

        # pmix@4.2.3 contains a breaking change, compat fixed in openmpi@4.1.6
        # See https://www.mail-archive.com/announce@lists.open-mpi.org//msg00158.html
        depends_on("pmix@:4.2.2", when="@:4.1.5")

        # @:4 does not depend on prrte and used orte
#        with when("@5"):

            # When an external PMIx is used, also an external PRRTE should be used
            # https://github.com/open-mpi/ompi/issues/13275#issuecomment-2907903468
#            depends_on("prrte")

            # only prrte knows about schedulers
            # https://github.com/spack/spack-packages/pull/1145#issuecomment-3208378366
#            for scheduler in [s for s in SCHEDULERS if s not in ("loadleveler")] + ["none"]:
#                depends_on(f"prrte schedulers={scheduler}", when=f"schedulers={scheduler}")

    # Libevent is required when *vendored* PMIx is used
    depends_on("libevent@2:", when="~internal-libevent")

    depends_on("openssh", type="run", when="+rsh")

    depends_on("cuda", type=("build", "link", "run"), when="@5: +cuda")
    depends_on("hip", type=("build", "link", "run"), when="@5: +rocm")

    conflicts("+cxx_exceptions", when="%nvhpc", msg="nvc does not ignore -fexceptions, but errors")

    # CUDA support was added in 1.7, and since the variant is part of the
    # parent package we must express as a conflict rather than a conditional
    # variant.
    conflicts("+cuda", when="@:1.6")
    # Same goes with ROCm support added in 5.0
    conflicts("+rocm", when="@:4")
    # PSM2 support was added in 1.10.0
    conflicts("fabrics=psm2", when="@:1.8")
    # MXM support was added in 1.5.4
    conflicts("fabrics=mxm", when="@:1.5.3")
    # libfabric (OFI) support was added in 1.10.0
    conflicts("fabrics=ofi", when="@:1.8")
    # fca support was added in 1.5.0 and removed in 5.0.0
    conflicts("fabrics=fca", when="@:1.4,5:")
    # hcoll support was added in 1.7.3:
    conflicts("fabrics=hco
            # Some of these options we have to find by hoping the
            # configure string is in the ompi_info output. While this
            # is usually true, it's not guaranteed.  For anything that
            # begins with --, we want to use the defaults as provided
            # by the openmpi package in the absense of any other info.

            # atomics
            if re.search(r"--enable-builtin-atomics", output):
                variants.append("+atomics")

            # java
            if version in ver("1.7.4:"):
                match = re.search(r"\bJava bindings: (\S+)", output)
                if match and is_enabled(match.group(1)):
                    variants.append("+java")
                else:
                    variants.append("~java")

            # static
            if re.search(r"--enable-static", output):
                variants.append("+static")
            elif re.search(r"--disable-static", output):
                variants.append("~static")
            elif re.search(r"\bMCA (?:coll|oca|pml): monitoring", output):
                # Built multiple variants of openmpi and ran diff.
                # This seems to be the distinguishing feature.
                variants.append("~static")

            # sqlite
            if version in ver("1.7.3:1"):
                if re.search(r"\bMCA db: sqlite", output):
                    variants.append("+sqlite3")
                else:
                    variants.append("~sqlite3")

            # vt
            if re.search(r"--enable-contrib-no-build=vt", output):
                variants.append("+vt")

            # thread_multiple
            if version in ver("1.5.4:2"):
                match = re.search(r"MPI_THREAD_MULTIPLE: (\S+?),?", output)
                if match and is_enabled(match.group(1)):
                    variants.append("+thread_multiple")
                else:
                    variants.append("~thread_multiple")



            # fabrics
            used_fabrics = []
            for fabric in cls.FABRICS:
                match = re.search(r"\bMCA (?:mtl|btl|pml): %s\b" % fabric, output)
                if match:
                    used_fabrics.append(fabric)
            if used_fabrics:
                variants.append("fabrics=" + ",".join(used_fabrics))
            else:
                variants.append("fabrics=none")

            # schedulers
            used_schedulers = []
            for scheduler in cls.SCHEDULERS:
                match = re.search(r"\bMCA (?:prrte|ras): %s\b" % scheduler, output)
                if match:
                    used_schedulers.append(scheduler)
            if used_schedulers:
                variants.append("schedulers=" + ",".join(used_schedulers))
            else:
                variants.append("schedulers=none")

            # Get the appropriate compiler
            match = re.search(r"\bC compiler absolute: (\S+)", output)
            if match:
                compiler = match.group(1)
                compiler_spec = get_spack_compiler_spec(compiler)
                if compiler_spec:
                    variants.append("%" + str(compiler_spec))
            results.append(" ".join(variants))
        return results

    def url_for_version(self, version):
        url = "https://download.open-mpi.org/release/open-mpi/v{0}/openmpi-{1}.tar.bz2"
        return url.format(version.up_to(2), version)

    @property
    def headers(self):
        hdrs = HeaderList(find(self.prefix.include, "mpi.h", recursive=False))
        if not hdrs:
            hdrs = HeaderList(find(self.prefix, "mpi.h", recursive=True))
        return hdrs or None

    @property
    def libs(self):
        query_parameters = self.spec.last_query.extra_parameters

            "MANDIR",
            "PKGDATADIR",
            "PKGLIBDIR",
            "PKGINCLUDEDIR",
        ]:
            env.unset(f"OPAL_{suffix}")

    def setup_dependent_package(self, module, dependent_spec):
        self.spec.mpicc = join_path(self.prefix.bin, "mpicc")
        self.spec.mpicxx = join_path(self.prefix.bin, self.cxxname)
        # Some derived packages define the "fortran" variant, most don't. Checking on the
        # presence of ~fortran makes us default to add fortran wrappers if the variant is
        # not declared.
        if self.spec.satisfies("~fortran"):
            return
        self.spec.mpifc = join_path(self.prefix.bin, "mpif90")
        self.spec.mpif77 = join_path(self.prefix.bin, "mpif77")

    # Most of the following with_or_without methods might seem redundant
    # because Spack compiler wrapper adds the required -I and -L flags, which
    # is enough for the configure script to find them. However, we also need
    # the flags in Libtool (lib/*.la) and pkg-config (lib/pkgconfig/*.pc).
    # Therefore, we pass the prefixes explicitly.

    def with_or_without_psm2(self, activated):
        if not activated:
            return "--without-psm2"
        return "--with-psm2={0}".format(self.spec["opa-psm2"].prefix)

    def with_or_without_verbs(self, activated):
        # Up through version 1.6, this option was named --with-openib.
        # In version 1.7, it was renamed to be --with-verbs.
        opt = "verbs" if self.spec.satisfies("@1.7:") else "openib"
        if not activated:
            return "--without-{0}".format(opt)
        return "--with-{0}={1}".format(opt, self.spec["rdma-core"].prefix)

    def with_or_without_mxm(self, activated):
        if not activated:
            return "--without-mxm"
        return "--with-mxm={0}".format(self.spec["mxm"].prefix)

    def with_or_without_ucx(self, activated):
        if not activated:
            return "--without-ucx"
        return "--with-ucx={0}".format(self.spec["ucx"].prefix)

    def with_or_witho
        perl("autogen.pl", "--force")
        if spec.satisfies("+two_level_namespace platform=darwin"):
            filter_file(r"-flat_namespace", "-commons,use_dylibs", "configure")

    def configure_args(self):
        spec = self.spec
        config_args = ["--enable-shared", "--disable-silent-rules", "--disable-sphinx"]

        # Work around incompatibility with new apple-clang linker
        # https://github.com/open-mpi/ompi/issues/12427
        if spec.satisfies("@:4.1.6,5.0.0:5.0.3 %apple-clang@15:"):
            config_args.append("--with-wrapper-fcflags=-Wl,-ld_classic")

        config_args.extend(self.enable_or_disable("builtin-atomics", variant="atomics"))

        if spec.satisfies("+pmi"):
            config_args.append(f"--with-pmi={spec['slurm'].prefix}")
        else:
            config_args.extend(self.with_or_without("pmi"))

        config_args.extend(self.enable_or_disable("static"))

        if spec.satisfies("@4.0.0:4.0.2"):
            # uct btl doesn't work with some UCX versions so just disable
            config_args.append("--enable-mca-no-build=btl-uct")

        # Remove ssh/rsh pml
        if spec.satisfies("~rsh"):
            config_args.append("--enable-mca-no-build=plm-rsh")

        # Useful for ssh-based environments
        # For v4 and lower
        if spec.satisfies("+orterunprefix"):
            config_args.append("--enable-orterun-prefix-by-default")

        # Enable IPv6 support
        if spec.satisfies("+ipv6"):
            config_args.append("--enable-ipv6")

        # some scientific packages ignore deprecated/remove symbols. Re-enable
        # them for now, for discussion see
        # https://github.com/open-mpi/ompi/issues/6114#issuecomment-446279495
        if spec.satisfies("@4.0.1:"):
            config_args.append("--enable-mpi1-compatibility")

        # Fabrics
        if "fabrics=auto" not in spec:
            config_args.extend(self.with_or_without("fab

        # Romio
        if spec.satisfies("~romio"):
            config_args.append("--disable-io-romio")

        if not spec.satisfies("romio-filesystem=none"):
            args = "+".join(spec.variants["romio-filesystem"].value)
            config_args.append(f"--with-io-romio-flags=--with-file-system={args}")

        if "+gpfs" in spec:
            config_args.append("--with-gpfs")
        else:
            config_args.append("--with-gpfs=no")

        # SQLite3 support
        config_args.extend(self.with_or_without("sqlite3"))

        # VampirTrace support
        if spec.satisfies("@1.3:1"):
            if "~vt" in spec:
                config_args.append("--enable-contrib-no-build=vt")

        # Multithreading support
        config_args.extend(
            self.enable_or_disable("mpi-thread-multiple", variant="thread_multiple")
        )

        # CUDA support
        # See https://www.open-mpi.org/faq/?category=buildcuda
        if "+cuda" in spec:
            # OpenMPI dynamically loads libcuda.so, requires dlopen
            config_args.append("--enable-dlopen")
            # Searches for header files in DIR/include
            config_args.append("--with-cuda={0}".format(spec["cuda"].prefix))
            if spec.satisfies("@1.7:1.7.2"):
                # This option was removed from later versions
                config_args.append(
                    "--with-cuda-libdir={0}".format(spec["cuda"].libs.directories[0])
                )
            if spec.satisfies("@5.0:"):
                # And then it returned
                config_args.append(
                    "--with-cuda-libdir={0}".format(spec["cuda"].libs.directories[0] + "/stubs")
                )
            if spec.satisfies("@1.7.2"):
                # There was a bug in 1.7.2 when --enable-static is used
                config_args.append("--enable-mca-no-build=pml-bfo")
        elif spec.

        #
        # disable romio for 5.0.0 or newer if using Intel OneAPI owing to a problem
        # building ZE related components of the romio packaged with this release
        #

        #       if spec.satisfies("@5.0.0:") and spec.satisfies("%oneapi"):
        #           config_args.append("--disable-io-romio")

        # https://www.intel.com/content/www/us/en/developer/articles/release-notes/oneapi-c-compiler-release-notes.html :
        # Key Features in Intel C++ Compiler Classic 2021.7
        #
        # The Intel C++ Classic Compiler is deprecated and an additional
        # diagnostic message will be output with each invocation. This
        # diagnostic may impact expected output during compilation. For
        # example, using the compiler to produce preprocessed information
        # (icpc -E) will produce the additional deprecation diagnostic,
        # interfering with the expected preprocessed output.
        #
        # This output can be disabled by using -diag-disable=10441 on
        # Linux/macOS or /Qdiag-disable:10441 on Windows. You can add this
        # option on the command line, configuration file or option setting
        # environment variables.
        if spec.satisfies("%intel@2021.7.0:"):
            config_args.append("CPPFLAGS=-diag-disable=10441")

        config_args += self.enable_or_disable("debug")

        return config_args

    # For v4 and lower
    @run_after("install")
    def delete_mpirun_mpiexec(self):
        # The preferred way to run an application when Slurm is the
        # scheduler is to let Slurm manage process spawning via PMI.
        #
        # Deleting the links to orterun avoids users running their
        # applications via mpirun or mpiexec, and leaves srun as the
        # only sensible choice (orterun is still present, but normal
        # users don't know about that).
        if self.spec.satisfies("~legacylaunchers schedulers=slurm"):
            exe_list = [
                self.prefix.bin.mpirun,
                self.prefix.bin.mpiexec,
                self.prefix.bin.shmemrun,
                self.prefix.bin.oshrun,
            ]
            script_stub = join_pa
        """The working directory for cached test sources."""
        return join_path(self.test_suite.current_test_cache_dir, self.extra_install_tests)

    def test_example(self):
        """Run test examples copied from source at build-time."""
        # Build the copied, cached test examples
        with test_part(
            self,
            "test_example_make",
            purpose="test: building cached test examples",
            work_dir=self._cached_tests_work_dir,
        ):
            make("all")

        # Run basic examples with known, simple-to-verify results
        hello_world = ["Hello, world", "I am", "0 of", "1"]
        ring_out = ["1 processes in ring", "0 exiting"]

        checks = {
            "hello_c": hello_world,
            "hello_cxx": hello_world,
            "hello_mpifh": hello_world,
            "hello_usempi": hello_world,
            "hello_usempif08": hello_world,
            "ring_c": ring_out,
            "ring_cxx": ring_out,
            "ring_mpifh": ring_out,
            "ring_usempi": ring_out,
            "ring_usempif08": ring_out,
        }

        for binary in checks:
            expected = checks[binary]
            with test_part(
                self,
                f"test_example_{binary}",
                purpose="run and check output",
                work_dir=self._cached_tests_work_dir,
            ):
                exe = which(binary)
                if not exe:
                    raise SkipTest(f"{binary} is missing")

                out = exe(output=str.split, error=str.split)
                check_outputs(expected, out)


def get_spack_compiler_spec(compiler):
    spack_compilers = find_compilers([os.path.dirname(compiler)])
    actual_compiler = None
    # check if the compiler actually matches the one we want
    for spack_compiler in spack_compilers:
        if spack_compiler.cc and spack_compiler.cc == compiler:
            actual_compiler = spack_compiler
            break
    return actual_compiler.spec if actual_compiler else None


def is_enabled(text):
    if text in set(["t", "true", "enabled", "yes", "1"]):
        return True
    return False


