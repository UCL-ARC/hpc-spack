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