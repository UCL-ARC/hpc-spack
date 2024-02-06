# Buildcaches
Are they a good idea, or shoould one use upstream instead. 

## Have posted this on spack slack:
I am interested in using build caches, to share common items between sites, but my first attempt did not go so well:
```
$ spack buildcache create -d /home/james/test-spack-sites/buildcachemirror   --only package gcc@12.2.0
==> Pushing binary packages to file:///home/james/test-spack-sites/buildcachemirror/build_cache
==> Error: 
 /tmp/tmpglzq7j17/gcc-12.2.0-mbdh5toomrjy4yr4ts4awskiio55nmq6/bin/c++ 
contains string
 /home/james/test-spack-sites/t1/spack/opt/spack 
after replacing it in rpaths.
Package should not be relocated.
 Use -a to override.
What is the problem with using -a?
```
I was using spack v19.0. Is there less of a problem with v12.1 or 'latest'?

## Upstreaming sites
Using an upstream site for the compilers would be a quick way to share the compiler, but it does not then become part of the site, so less useful for a stable site? But do we need that for devvelopment? Could just have a site for the compiler


## Attempt at a buildcache was:
need a directory to hold the cache files so:


mkdir /home/james/test-spack-sites/buildcachemirror

in site t1

spack gpg init   # a prerequisite
spack gpg create Jlegg j.legg@ucl.ac.uk

Output was:
gpg: key C97796D57C4C5934 marked as ultimately trusted
gpg: directory '/home/james/test-spack-sites/t1/spack/opt/spack/gpg/openpgp-revocs.d' created
gpg: revocation certificate stored as '/home/james/test-spack-sites/t1/spack/opt/spack/gpg/openpgp-revocs.d/52DF92D2904498B6A0011B80C97796D57C4C5934.rev'

==> Error: 
 /tmp/tmpxfgypfdz/mpfr-4.1.0-j5qgj4oikcyz26427vbbgjvrlj2n4qm6/lib/libmpfr.so.6.1.0 
contains string
 /home/james/test-spack-sites/t1/spack/opt/spack 
after replacing it in rpaths.
Package should not be relocated.
 Use -a to override.

- that's helpful !

so tried: spack buildcache create -d /home/james/test-spack-sites/buildcachemirror   --only package gcc@12.2.0

==> Error: 
 /tmp/tmpglzq7j17/gcc-12.2.0-mbdh5toomrjy4yr4ts4awskiio55nmq6/bin/c++ 
contains string
 /home/james/test-spack-sites/t1/spack/opt/spack 
after replacing it in rpaths.
Package should not be relocated.
 Use -a to override.

 # Fixed problem with filling /tmp on Myriad

 spack buildcache create -d /home/james/test-spack-sites/buildcachemirror -a gcc@12.2.0 worked on WSL

 Trying on Myraid

 spack buildcache create -d /shared/ucl/apps/spack-test/buildcache -a gcc@12.2.0 

 this put sig files at /shared/ucl/apps/spack-test/buildcache/build_cache/ - where are the actual files - try aagain with -f 

 Ah! the actual files are in an dir tree - so follow down linux-rhel7-skylake_avx512/
 - nso they are now creates

 # Importing into site2
- moved to site 2
- site 2 has no spack compiler yet

 spack mirror add buildcache  /shared/ucl/apps/spack-test/buildcache
 spack buildcache update-index -d /shared/ucl/apps/spack-test/buildcache
 spack buildcache list  # now listed the cached specs - gcc12 and its deps.
 spack install gcc@12.2.0 # no chatter for a while !
 it began by buildin libiconv libsigsegv berkley-db - these wre not in the build cache
 pkgconf
 then it said 

==> Installing zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut
==> Fetching file:///shared/ucl/apps/spack-test/buildcache/build_cache/linux-rhel7-skylake_avx512-gcc-11.2.1-zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut.spec.json.sig
gpg: keyring `/lustre/shared/ucl/apps/spack-test/site2/spack/opt/spack/gpg/pubring.gpg' created
gpg: Signature made Wed 15 Mar 2023 11:22:57 GMT using RSA key ID 256F7B75
gpg: Can't check signature: No public key
==> Warning: Failed to verify: file:///shared/ucl/apps/spack-test/buildcache/build_cache/linux-rhel7-skylake_avx512-gcc-11.2.1-zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut.spec.json.sig
==> Warning: Skipping build of gcc-12.2.0-ipcge6nrhsqqxbl43o64uizaigcybsrj since zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut failed
==> Warning: Skipping build of perl-5.36.0-22nfjfpse3uobq4wrzisck6qtpzvxrlp since zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut failed
==> Warning: Skipping build of autoconf-2.69-cqrevztstgqvqfb2xlxwdlqpgel2tx64 since perl-5.36.0-22nfjfpse3uobq4wrzisck6qtpzvxrlp failed
==> Warning: Skipping build of gmp-6.2.1-qnxpsdbkxog5r5eku2kxjdpe6c3fn2yl since autoconf-2.69-cqrevztstgqvqfb2xlxwdlqpgel2tx64 failed
==> Warning: Skipping build of gawk-5.1.1-d3va42bp6ldyzcmz6c3uujx5zlwwk52b since gmp-6.2.1-qnxpsdbkxog5r5eku2kxjdpe6c3fn2yl failed
==> Warning: Skipping build of mpc-1.2.1-vmu6q3ibyyo7x3j45zwejv6rq5nbjlsm since gmp-6.2.1-qnxpsdbkxog5r5eku2kxjdpe6c3fn2yl failed
==> Warning: Skipping build of mpfr-4.1.0-v2ry2dzftgi6gik7pgrt66s473ee62bj since gmp-6.2.1-qnxpsdbkxog5r5eku2kxjdpe6c3fn2yl failed
==> Warning: Skipping build of automake-1.16.5-mr4xtaehwdkcowbthqsh6ptcbsdgsi4z since autoconf-2.69-cqrevztstgqvqfb2xlxwdlqpgel2tx64 failed
==> Warning: Skipping build of texinfo-6.5-5n7yhpzvlqochyz7jys5lihvo6udhsxw since perl-5.36.0-22nfjfpse3uobq4wrzisck6qtpzvxrlp failed
==> Error: Failed to install zlib due to NoVerifyException: Spack found new style signed binary packages, but was unable to verify any of them.  Please obtain and trust the correct public key.  If these are public spack binaries, please see the spack docs for locations where keys can be found.

zlib is in the cache

spack continued to build other deps not in the cache:
autoconf-archive zstd diffutils nucrses m4 bzip2 readline libtool gdbm perl textinfo autoconf automake- consider pushing these to the cache



spack buildcache list
==> 6 cached builds.
-- linux-rhel7-skylake_avx512 / gcc@11.2.1 ----------------------
gcc@12.2.0  gmp@6.2.1  mpc@1.2.1  mpfr@4.1.0  zlib@1.2.13  zstd@1.5.2

did it cache run deps and not build deps? Need to add build deps to things to download from cache

DONE rebuild cache items with --unsigned
OR download the keys from the buildcache mirror (there are spack commands) and trust the keys 


DONE - add gcc deps (both kinds) to first_complier.yaml so that they get pulled from the cache.

DONE - add command to link site to another (e.g. buildcache) and to download and trust its keys - if the latter is the step to take (see DONEs above)

## 20 March 2023
tried spack buildcache keys --install --trust  but then gcc install gave 

==> Warning: Failed to verify: file:///shared/ucl/apps/spack-test/buildcache/build_cache/linux-rhel7-skylake_avx512-gcc-11.2.1-zlib-1.2.13-e7tak744ivqyus4hlrptilzxcycrzgut.spec.json.sig

the answer, from spack slack, was spack buildcache update-index --keys <mirror> from the source site
or as Jonathan Ansderson on spack slack said, "on the side with the keys"

now at one point I did:

spack gpg init
spack gpg create Jlegg j.legg@ucl.ac.uk

made pushed some buildcaches with spack buildcache create -a -m buildcache autoconf-archive@2022.02.11 etc 

## made a new site3 to test cache

so created a site with spacksites create site3

spack mirror add buildcache file:///shared/ucl/apps/spack-test/buildcache/  # have done this with a new initial mirrors.yaml file

checked for keys - fetched the keys
spack buildcache keys --install --trust  - did some importing of the keys

did spacksites install-env site3 first_compiler first_compiler.yaml - it installed gcc and its deps from the buildcache

spack find
-- linux-rhel7-skylake_avx512 / gcc@11.2.1 ----------------------
autoconf@2.69                gawk@5.1.1       libtool@2.4.7  pkgconf@1.8.0
autoconf-archive@2022.02.11  gcc@12.2.0       m4@1.4.19      readline@8.1.2
automake@1.16.5              gdbm@1.23        mpc@1.2.1      texinfo@6.5
berkeley-db@18.1.40          gmp@6.2.1        mpfr@4.1.0     zlib@1.2.13
bzip2@1.0.8                  libiconv@1.16    ncurses@6.3    zstd@1.5.2
diffutils@3.8                libsigsegv@2.13  perl@5.36.0

perhaps these should all be in first_compliler.yaml to avoid ambiguity

spack buildcache update-index --keys <mirror>


DONE - add the 2(or3?) commands to link in the buildcache spacksites - mirror add and keys
- need a setting for the path to the buildcache - no, do with mirrors.yaml  DONE

TODO add a spacksites command to push buildcache items to the buildcache 