# A build of huge.yaml - a post mortem

spacksites/spack-env-templates/dev1/build/huge.yaml

was built with batch job 

spacksites/cluster_jobscript_examples/myriad_huge_set.qsub

but with 

# Array job
#$ -t 1-5
#$ -tc 1  <- 1 concurrent job

so that will cause a resart of the spack build jobs if they lock up

## Result logs generated were 
(where .proc#n means one of the 4 concurrent spack build processes in that instance of the array job)

-rw-r--r--   1 ccspapp ccsp  22518 Apr  5 17:36 install.oe127492.1.proc2
-rw-r--r--   1 ccspapp ccsp  16197 Apr  5 17:36 install.oe127492.1.proc3
-rw-r--r--   1 ccspapp ccsp  15314 Apr  5 17:37 install.oe127492.1.proc4
-rw-r--r--   1 ccspapp ccsp  11372 Apr  5 17:38 install.oe127492.1.proc1
-rw-r--r--   1 ccspapp ccsp  12365 Apr  5 19:57 install.oe127492.2.proc1
-rw-r--r--   1 ccspapp ccsp  15928 Apr  5 19:57 install.oe127492.2.proc3
-rw-r--r--   1 ccspapp ccsp  16012 Apr  5 19:57 install.oe127492.2.proc2
-rw-r--r--   1 ccspapp ccsp  37481 Apr  5 20:03 install.oe127492.2.proc4
-rw-r--r--   1 ccspapp ccsp      0 Apr  6 08:06 install.oe127492.3.proc4
-rw-r--r--   1 ccspapp ccsp      0 Apr  6 08:06 install.oe127492.3.proc1
-rw-r--r--   1 ccspapp ccsp  13073 Apr  6 08:06 install.oe127492.3.proc3
-rw-r--r--   1 ccspapp ccsp  25782 Apr  6 08:07 install.oe127492.3.proc2
-rw-r--r--   1 ccspapp ccsp   6536 Apr  6 20:13 install.oe127492.4.proc3
-rw-r--r--   1 ccspapp ccsp  15868 Apr  6 20:13 install.oe127492.4.proc2
-rw-r--r--   1 ccspapp ccsp  13076 Apr  6 20:13 install.oe127492.4.proc1
-rw-r--r--   1 ccspapp ccsp  25638 Apr  6 20:14 install.oe127492.4.proc4
-rw-r--r--   1 ccspapp ccsp      0 Apr  7 08:24 install.oe127492.5.proc3
-rw-r--r--   1 ccspapp ccsp      0 Apr  7 08:24 install.oe127492.5.proc1
drwxr-xr-x   7 ccspapp ccsp   4096 Apr  7 08:24 .
-rw-r--r--   1 ccspapp ccsp  13790 Apr  7 08:25 install.oe127492.5.proc4
-rw-r--r--   1 ccspapp ccsp  26329 Apr  7 08:25 install.oe127492.5.proc2

### array job #1
#### spack proc #1
==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
similar for gzip libdflate
built: intel-mkl

#### spack proc #2
==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
similar for htslib, 
build failed: gzip
==> Warning: Skipping build of libdeflate-1.10-nogn6axhbi7bo4ojfcoplxlc2dqlipb6 since gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg failed
similar for libdeflate, htslib, bfctools
built: libbsd, libxml2-2.10.1

#### spack proc #3 
==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
similar for gzip, libdeflate, htslib
built: diffutils, libxml2-2.7.8

#### spack proc #4
built: libunistring, bdw-gc
==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
similar for gzip

### array job #2
#### spack proc #1
build failed gzip

### spack proc #2 
built clustal-omega

### spack proc #3
built swig
==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
similar for gzip, hstlib, bcftools
==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
similar for cpmd
built: bzip2, m4, libidn2 and several more
failed: nano


so grep for:
==> Error
==> Warning
==> Installing
Successfully installed with __spack_path_placeholder__ removed below:
(This was the second build run)

[ccspapp@login13 hpc-spack]$ grep "Successfully installed\|==> Error\|==> Warning\|==> Installing"   install.oe127492*
install.oe127492.1.proc1:==> Installing environment hugeset
install.oe127492.1.proc1:==> Installing intel-mkl-2020.4.304-o5otrpw4hvbqxdsdodyyjq37p7j5qsid
install.oe127492.1.proc1:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.1.proc1:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.1.proc1:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.1.proc1:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.1.proc1:==> intel-mkl: Successfully installed intel-mkl-2020.4.304-o5otrpw4hvbqxdsdodyyjq37p7j5qsid
install.oe127492.1.proc2:==> Installing environment hugeset
install.oe127492.1.proc2:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe127492.1.proc2:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.1.proc2:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.1.proc2:==> Error: ProcessError: Command exited with status 2:
install.oe127492.1.proc2:==> Installing libbsd-0.11.5-lgut7zsokq3bpbqolfdwnfhprwtxnua3
install.oe127492.1.proc2:==> Warning: Skipping build of libdeflate-1.10-nogn6axhbi7bo4ojfcoplxlc2dqlipb6 since gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg failed
install.oe127492.1.proc2:==> Warning: Skipping build of htslib-1.14-lo5icmlwefk5wqxi3od62a44iuhwdvey since libdeflate-1.10-nogn6axhbi7bo4ojfcoplxlc2dqlipb6 failed
install.oe127492.1.proc2:==> Warning: Skipping build of bcftools-1.14-ve3t4kitjapu5olbvrzu6vidirjm5lga since htslib-1.14-lo5icmlwefk5wqxi3od62a44iuhwdvey failed
install.oe127492.1.proc2:==> libbsd: Successfully installed libbsd-0.11.5-lgut7zsokq3bpbqolfdwnfhprwtxnua3
install.oe127492.1.proc2:==> Installing libxml2-2.10.1-ce3gndhsf7gcyjtxnqajcuo6iyzbhhqr
install.oe127492.1.proc2:==> libxml2: Successfully installed libxml2-2.10.1-ce3gndhsf7gcyjtxnqajcuo6iyzbhhqr
install.oe127492.1.proc3:==> Installing environment hugeset
install.oe127492.1.proc3:==> Installing diffutils-3.8-gudy4fya4gliqa5q56qknhlpciaroxkl
install.oe127492.1.proc3:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.1.proc3:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.1.proc3:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.1.proc3:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.1.proc3:==> diffutils: Successfully installed diffutils-3.8-gudy4fya4gliqa5q56qknhlpciaroxkl
install.oe127492.1.proc3:==> Installing libxml2-2.7.8-wmug5zxn4tefiijsuateza2zxjhyiddo
install.oe127492.1.proc3:==> libxml2: Successfully installed libxml2-2.7.8-wmug5zxn4tefiijsuateza2zxjhyiddo
install.oe127492.1.proc4:==> Installing environment hugeset
install.oe127492.1.proc4:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe127492.1.proc4:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.1.proc4:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.1.proc4:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe127492.1.proc4:==> Installing libunistring-0.9.10-wfraxml4a63aoskz54hubgyxgrakaxnx
install.oe127492.1.proc4:==> libunistring: Successfully installed libunistring-0.9.10-wfraxml4a63aoskz54hubgyxgrakaxnx
install.oe127492.1.proc4:==> Installing bdw-gc-8.2.2-bagnutguy2fawuiibtu3gjy56o4wyg3z
install.oe127492.1.proc4:==> bdw-gc: Successfully installed bdw-gc-8.2.2-bagnutguy2fawuiibtu3gjy56o4wyg3z
install.oe127492.2.proc1:==> Installing environment hugeset
install.oe127492.2.proc1:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe127492.2.proc1:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.2.proc1:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.2.proc1:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.2.proc1:==> Error: ProcessError: Command exited with status 2:
install.oe127492.2.proc2:==> Installing environment hugeset
install.oe127492.2.proc2:==> Installing clustal-omega-1.2.4-snaqrtzfxt525n24kiocp2nqybrgukjc
install.oe127492.2.proc2:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.2.proc2:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.2.proc2:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.2.proc2:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.2.proc2:==> clustal-omega: Successfully installed clustal-omega-1.2.4-snaqrtzfxt525n24kiocp2nqybrgukjc
install.oe127492.2.proc3:==> Installing environment hugeset
install.oe127492.2.proc3:==> Installing swig-4.0.2-cmwiaz4zoxumgxrtljvv3jthbamqgr3p
install.oe127492.2.proc3:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.2.proc3:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.2.proc3:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.2.proc3:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.2.proc3:==> swig: Successfully installed swig-4.0.2-cmwiaz4zoxumgxrtljvv3jthbamqgr3p
install.oe127492.2.proc4:==> Installing environment hugeset
install.oe127492.2.proc4:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe127492.2.proc4:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.2.proc4:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.2.proc4:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.2.proc4:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.2.proc4:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe127492.2.proc4:==> Installing figtree-1.4.3-2vixhgwh3iynoaddhhpkrcfmjeywcfsc
install.oe127492.2.proc4:==> figtree: Successfully installed figtree-1.4.3-2vixhgwh3iynoaddhhpkrcfmjeywcfsc
install.oe127492.2.proc4:==> Installing cpmd-4.3-zh4lewbullxy2sxxpg6fauptkcoz3bsq
install.oe127492.2.proc4:==> Error: FetchError: Manual download is required for cpmd. Refer to https://www.cpmd.org/wordpress/ for download instructions.
install.oe127492.2.proc4:==> Installing bzip2-1.0.8-736nksuyccgp2kz546wxmbslvssfccir
install.oe127492.2.proc4:==> bzip2: Successfully installed bzip2-1.0.8-736nksuyccgp2kz546wxmbslvssfccir
install.oe127492.2.proc4:==> Installing m4-1.4.19-fdinnm2yevwrmnirwn6sowgrye6kqibf
install.oe127492.2.proc4:==> m4: Successfully installed m4-1.4.19-fdinnm2yevwrmnirwn6sowgrye6kqibf
install.oe127492.2.proc4:==> Installing libidn2-2.3.0-ckajz35vuygq3yuhfsqfyjbuwbeh2qap
install.oe127492.2.proc4:==> libidn2: Successfully installed libidn2-2.3.0-ckajz35vuygq3yuhfsqfyjbuwbeh2qap
install.oe127492.2.proc4:==> Installing nano-6.3-oemulaw4hmjbqwoijhbd3d6z4qmkldw5
install.oe127492.2.proc4:==> Error: ProcessError: Command exited with status 2:
install.oe127492.2.proc4:==> Installing libedit-3.1-20210216-p3kq3x63wacjb2vxtznzlejo7kzen7ve
install.oe127492.2.proc4:==> libedit: Successfully installed libedit-3.1-20210216-p3kq3x63wacjb2vxtznzlejo7kzen7ve
install.oe127492.2.proc4:==> Installing vim-9.0.0045-75ld2wtssjcsx46wofoob2mu5hfiwcwu
install.oe127492.2.proc4:==> vim: Successfully installed vim-9.0.0045-75ld2wtssjcsx46wofoob2mu5hfiwcwu
install.oe127492.2.proc4:==> Installing tcsh-6.24.00-krwxdooqyioq67bn4a4cbmj443h2zyrj
install.oe127492.2.proc4:==> tcsh: Successfully installed tcsh-6.24.00-krwxdooqyioq67bn4a4cbmj443h2zyrj
install.oe127492.2.proc4:==> Installing readline-8.1.2-c4x6t77euyaahv4jftgehinns7plm2ib
install.oe127492.2.proc4:==> readline: Successfully installed readline-8.1.2-c4x6t77euyaahv4jftgehinns7plm2ib
install.oe127492.2.proc4:==> Installing pixman-0.40.0-77lcba3krdi4g3mdpml3yxhz2gw2sf2a
install.oe127492.2.proc4:==> pixman: Successfully installed pixman-0.40.0-77lcba3krdi4g3mdpml3yxhz2gw2sf2a
install.oe127492.2.proc4:==> Installing libxau-1.0.8-xahjurignvxjp67z7udw3wl7bniz22m3
install.oe127492.2.proc4:==> libxau: Successfully installed libxau-1.0.8-xahjurignvxjp67z7udw3wl7bniz22m3
install.oe127492.2.proc4:==> Installing libfontenc-1.1.3-eqmzxtfbsyppzbrzdcwwyj5vjkpvu3wp
install.oe127492.2.proc4:==> libfontenc: Successfully installed libfontenc-1.1.3-eqmzxtfbsyppzbrzdcwwyj5vjkpvu3wp
install.oe127492.2.proc4:==> Installing libice-1.0.9-kzlev7hqiljsdh3qmvrtgunh2sdldonr
install.oe127492.2.proc4:==> libice: Successfully installed libice-1.0.9-kzlev7hqiljsdh3qmvrtgunh2sdldonr
install.oe127492.2.proc4:==> Installing libxdmcp-1.1.2-biduajv4njciswgmdvjm2g7iafpp5rca
install.oe127492.2.proc4:==> libxdmcp: Successfully installed libxdmcp-1.1.2-biduajv4njciswgmdvjm2g7iafpp5rca
install.oe127492.2.proc4:==> Installing expat-2.4.8-r7ibi7ee64mtxqraglhle3cm6jxsj3tz
install.oe127492.2.proc4:==> expat: Successfully installed expat-2.4.8-r7ibi7ee64mtxqraglhle3cm6jxsj3tz
install.oe127492.2.proc4:==> Installing libxslt-1.1.26-djgng3cw3phnr4s6ywcfpho5tcm2dnra
install.oe127492.2.proc4:==> libxslt: Successfully installed libxslt-1.1.26-djgng3cw3phnr4s6ywcfpho5tcm2dnra
install.oe127492.3.proc2:==> Installing environment hugeset
install.oe127492.3.proc2:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe127492.3.proc2:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.3.proc2:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.3.proc2:==> Warning: Unable to remove failure marking for cpmd (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq'
install.oe127492.3.proc2:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe127492.3.proc2:==> Installing cpmd-4.3-zh4lewbullxy2sxxpg6fauptkcoz3bsq
install.oe127492.3.proc2:==> Error: FetchError: Manual download is required for cpmd. Refer to https://www.cpmd.org/wordpress/ for download instructions.
install.oe127492.3.proc2:==> Installing nano-6.3-oemulaw4hmjbqwoijhbd3d6z4qmkldw5
install.oe127492.3.proc2:==> Error: ProcessError: Command exited with status 2:
install.oe127492.3.proc3:==> Installing environment hugeset
install.oe127492.3.proc3:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe127492.3.proc3:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.3.proc3:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.3.proc3:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.3.proc3:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.3.proc3:==> Error: ProcessError: Command exited with status 2:
install.oe127492.4.proc1:==> Installing environment hugeset
install.oe127492.4.proc1:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe127492.4.proc1:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.4.proc1:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.4.proc1:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.4.proc1:==> Warning: Unable to remove failure marking for cpmd (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq'
install.oe127492.4.proc1:==> Error: ProcessError: Command exited with status 2:
install.oe127492.4.proc2:==> Installing environment hugeset
install.oe127492.4.proc2:==> Installing cpmd-4.3-zh4lewbullxy2sxxpg6fauptkcoz3bsq
install.oe127492.4.proc2:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.4.proc2:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.4.proc2:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.4.proc2:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.4.proc2:==> Error: FetchError: Manual download is required for cpmd. Refer to https://www.cpmd.org/wordpress/ for download instructions.
install.oe127492.4.proc3:==> Installing environment hugeset
install.oe127492.4.proc3:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe127492.4.proc3:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.4.proc3:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.4.proc3:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.4.proc3:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.4.proc3:==> Warning: Unable to remove failure marking for cpmd (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq'
install.oe127492.4.proc3:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe127492.4.proc4:==> Installing environment hugeset
install.oe127492.4.proc4:==> Installing nano-6.3-oemulaw4hmjbqwoijhbd3d6z4qmkldw5
install.oe127492.4.proc4:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.4.proc4:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.4.proc4:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.4.proc4:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.4.proc4:==> Warning: Unable to remove failure marking for cpmd (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq'
install.oe127492.4.proc4:==> Error: ProcessError: Command exited with status 2:
install.oe127492.5.proc2:==> Installing environment hugeset
install.oe127492.5.proc2:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe127492.5.proc2:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.5.proc2:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.5.proc2:==> Warning: Unable to remove failure marking for libdeflate (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/libdeflate-nogn6axhbi7bo4ojfcoplxlc2dqlipb6'
install.oe127492.5.proc2:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.5.proc2:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe127492.5.proc2:==> Installing cpmd-4.3-zh4lewbullxy2sxxpg6fauptkcoz3bsq
install.oe127492.5.proc2:==> Error: FetchError: Manual download is required for cpmd. Refer to https://www.cpmd.org/wordpress/ for download instructions.
install.oe127492.5.proc2:==> Installing nano-6.3-oemulaw4hmjbqwoijhbd3d6z4qmkldw5
install.oe127492.5.proc2:==> Error: ProcessError: Command exited with status 2:
install.oe127492.5.proc4:==> Installing environment hugeset
install.oe127492.5.proc4:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe127492.5.proc4:==> Warning: Unable to remove failure marking for adf (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/adf-bjnvyz7l4orj46qw2glj63ghwvdiekoc'
install.oe127492.5.proc4:==> Warning: Unable to remove failure marking for gzip (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/gzip-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg'
install.oe127492.5.proc4:==> Warning: Unable to remove failure marking for htslib (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/htslib-lo5icmlwefk5wqxi3od62a44iuhwdvey'
install.oe127492.5.proc4:==> Warning: Unable to remove failure marking for bcftools (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/bcftools-ve3t4kitjapu5olbvrzu6vidirjm5lga'
install.oe127492.5.proc4:==> Warning: Unable to remove failure marking for cpmd (/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq): [Errno 2] No such file or directory: '/lustre/shared/ucl/apps/spack-test/batch-site-huge/spack/opt/spack////////.spack-db/failures/cpmd-zh4lewbullxy2sxxpg6fauptkcoz3bsq'
install.oe127492.5.proc4:==> Error: ProcessError: Command exited with status 2:


The first run:
[ccspapp@login13 hpc-spack]$ grep "Successfully installed\|==> Error\|==> Warning\|==> Installing"   install.oe125375*
install.oe125375.1.proc1:==> Installing environment hugeset
install.oe125375.1.proc1:==> Installing zlib-1.2.13-55wkgq5qbcqqjwxqnukhnhfcrzk7qvmf
install.oe125375.1.proc1:==> zlib: Successfully installed zlib-1.2.13-55wkgq5qbcqqjwxqnukhnhfcrzk7qvmf
install.oe125375.1.proc1:==> Installing sparsehash-2.0.4-sn2suqthjbm2q4t7rwmrnnu6xz7visuo
install.oe125375.1.proc1:==> sparsehash: Successfully installed sparsehash-2.0.4-sn2suqthjbm2q4t7rwmrnnu6xz7visuo
install.oe125375.1.proc1:==> Installing utf8cpp-2.3.4-lhyr6n42xfsgfm5eqri355rkwhetig6q
install.oe125375.1.proc1:==> utf8cpp: Successfully installed utf8cpp-2.3.4-lhyr6n42xfsgfm5eqri355rkwhetig6q
install.oe125375.1.proc1:==> Installing fasta-36.3.8h_2020-05-04-4uipkk654xvrh2ntrmgybfy7q4bbxxl2
install.oe125375.1.proc1:==> fasta: Successfully installed fasta-36.3.8h_2020-05-04-4uipkk654xvrh2ntrmgybfy7q4bbxxl2
install.oe125375.1.proc1:==> Installing libpng-1.6.37-edx2ivixbmw534gzqzxtot5vxrgjxeuh
install.oe125375.1.proc1:==> libpng: Successfully installed libpng-1.6.37-edx2ivixbmw534gzqzxtot5vxrgjxeuh
install.oe125375.1.proc1:==> Installing bowtie-1.3.0-hsd4vryjqkwck5liqhazot3ggebm7vgz
install.oe125375.1.proc1:==> bowtie: Successfully installed bowtie-1.3.0-hsd4vryjqkwck5liqhazot3ggebm7vgz
install.oe125375.1.proc1:==> Installing pigz-2.7-6ucu3otrqbtblgaf2lfxfya4d2bsfam2
install.oe125375.1.proc1:==> pigz: Successfully installed pigz-2.7-6ucu3otrqbtblgaf2lfxfya4d2bsfam2
install.oe125375.1.proc2:==> Installing environment hugeset
install.oe125375.1.proc2:==> Installing util-macros-1.19.3-dmnhcaycfgauikh42jbteh65lz7czdk6
install.oe125375.1.proc2:==> util-macros: Successfully installed util-macros-1.19.3-dmnhcaycfgauikh42jbteh65lz7czdk6
install.oe125375.1.proc2:==> Installing cufflinks-2.2.1-2v5mgbtebp4fwujdfxi3fmdfkrs4ract
install.oe125375.1.proc2:==> cufflinks: Successfully installed cufflinks-2.2.1-2v5mgbtebp4fwujdfxi3fmdfkrs4ract
install.oe125375.1.proc2:==> Installing openjdk-11.0.17_8-6grmdz3txnuw4zvysjls52jts5wfwp3w
install.oe125375.1.proc2:==> openjdk: Successfully installed openjdk-11.0.17_8-6grmdz3txnuw4zvysjls52jts5wfwp3w
install.oe125375.1.proc2:==> Installing libpthread-stubs-0.4-og4eg5ah6f4jhulg5koyht7vlymfn75z
install.oe125375.1.proc2:==> libpthread-stubs: Successfully installed libpthread-stubs-0.4-og4eg5ah6f4jhulg5koyht7vlymfn75z
install.oe125375.1.proc2:==> Installing gperf-3.1-w7gcptzfsvokzvtjcil7bbxbwmtvih7k
install.oe125375.1.proc2:==> gperf: Successfully installed gperf-3.1-w7gcptzfsvokzvtjcil7bbxbwmtvih7k
install.oe125375.1.proc3:==> Installing environment hugeset
install.oe125375.1.proc3:==> Installing ca-certificates-mozilla-2022-10-11-hy3es4xldn2hs644rudrplhjj2n54qfy
install.oe125375.1.proc3:==> ca-certificates-mozilla: Successfully installed ca-certificates-mozilla-2022-10-11-hy3es4xldn2hs644rudrplhjj2n54qfy
install.oe125375.1.proc3:==> Installing libsigsegv-2.13-7qgsv4bvgwrutjtqzdm6iqorz4gfen6x
install.oe125375.1.proc3:==> libsigsegv: Successfully installed libsigsegv-2.13-7qgsv4bvgwrutjtqzdm6iqorz4gfen6x
install.oe125375.1.proc4:==> Installing environment hugeset
install.oe125375.1.proc4:==> Installing libmd-1.0.4-cappetd5k45nf5gtwm2ycpkoj4zgglmz
install.oe125375.1.proc4:==> libmd: Successfully installed libmd-1.0.4-cappetd5k45nf5gtwm2ycpkoj4zgglmz
install.oe125375.2.proc1:==> Installing environment hugeset
install.oe125375.2.proc1:==> Installing libffi-3.4.2-7xrzeeqpvdrc7z66uqgg36jiyyltkiau
install.oe125375.2.proc1:==> libffi: Successfully installed libffi-3.4.2-7xrzeeqpvdrc7z66uqgg36jiyyltkiau
install.oe125375.2.proc2:==> Installing environment hugeset
install.oe125375.2.proc2:==> Installing xz-5.2.7-f2tybd3dmyz5mz5kzmr46wfb5cu222fs
install.oe125375.2.proc2:==> xz: Successfully installed xz-5.2.7-f2tybd3dmyz5mz5kzmr46wfb5cu222fs
install.oe125375.2.proc3:==> Installing environment hugeset
install.oe125375.2.proc3:==> Installing zstd-1.5.2-dokxxsk4qauv3lgjxz3tcc23rjzngwlh
install.oe125375.2.proc3:==> zstd: Successfully installed zstd-1.5.2-dokxxsk4qauv3lgjxz3tcc23rjzngwlh
install.oe125375.2.proc4:==> Installing environment hugeset
install.oe125375.2.proc4:==> Installing adf-2017.113-bjnvyz7l4orj46qw2glj63ghwvdiekoc
install.oe125375.2.proc4:==> Error: FetchError: Manual download is required for adf. Refer to https://www.scm.com/product/adf/ for download instructions.
install.oe125375.2.proc4:==> Installing datamash-1.3-hjll4hwrxvkjgkyvvptniamm45lwkx3u
install.oe125375.2.proc4:==> datamash: Successfully installed datamash-1.3-hjll4hwrxvkjgkyvvptniamm45lwkx3u
install.oe125375.3.proc1:==> Installing environment hugeset
install.oe125375.3.proc1:==> Installing nasm-2.15.05-hde72f3mgjvxfg5t5u74raje4n757ycp
install.oe125375.3.proc1:==> nasm: Successfully installed nasm-2.15.05-hde72f3mgjvxfg5t5u74raje4n757ycp
install.oe125375.3.proc1:==> Installing yasm-1.3.0-w33ul5r632fvqg2kyrdj455hwx7lhvgb
install.oe125375.3.proc1:==> yasm: Successfully installed yasm-1.3.0-w33ul5r632fvqg2kyrdj455hwx7lhvgb
install.oe125375.3.proc1:==> Installing lz4-1.9.4-df6kv563yzljiwtrfayrfyjew2ushntn
install.oe125375.3.proc1:==> lz4: Successfully installed lz4-1.9.4-df6kv563yzljiwtrfayrfyjew2ushntn
install.oe125375.3.proc2:==> Installing environment hugeset
install.oe125375.3.proc2:==> Installing findutils-4.9.0-fiioswqla27yefsolmw6lvctixtkkom6
install.oe125375.3.proc2:==> findutils: Successfully installed findutils-4.9.0-fiioswqla27yefsolmw6lvctixtkkom6
install.oe125375.3.proc3:==> Installing environment hugeset
install.oe125375.3.proc3:==> Installing libatomic-ops-7.6.14-y2oz5vfmk2xq646znx5p4ytkwlz3rc7w
install.oe125375.3.proc3:==> libatomic-ops: Successfully installed libatomic-ops-7.6.14-y2oz5vfmk2xq646znx5p4ytkwlz3rc7w
install.oe125375.3.proc3:==> Installing pcre2-10.39-cuyv5q2w4z5le3umgetdqltbtfgm6zwm
install.oe125375.3.proc3:==> pcre2: Successfully installed pcre2-10.39-cuyv5q2w4z5le3umgetdqltbtfgm6zwm
install.oe125375.3.proc3:==> Installing libcerf-1.3-eetmibb6ydwjnngelxsynzzaqqruiz6i
install.oe125375.3.proc3:==> libcerf: Successfully installed libcerf-1.3-eetmibb6ydwjnngelxsynzzaqqruiz6i
install.oe125375.3.proc3:==> Installing libfabric-1.16.1-b274spnawi4zwz63ygxa2np57edwwc2s
install.oe125375.3.proc3:==> libfabric: Successfully installed libfabric-1.16.1-b274spnawi4zwz63ygxa2np57edwwc2s
install.oe125375.3.proc4:==> Installing environment hugeset
install.oe125375.3.proc4:==> Installing gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg
install.oe125375.3.proc4:==> Error: ProcessError: Command exited with status 2:
install.oe125375.3.proc4:==> Installing libunwind-1.6.2-oo5nxgvnhlvvb5ss3u7lp45w2pvljyre
install.oe125375.3.proc4:==> Warning: Skipping build of libdeflate-1.10-nogn6axhbi7bo4ojfcoplxlc2dqlipb6 since gzip-1.12-ppgmuu4rivxoqlstzw4k7wmvjx7szbeg failed
install.oe125375.3.proc4:==> Warning: Skipping build of htslib-1.14-lo5icmlwefk5wqxi3od62a44iuhwdvey since libdeflate-1.10-nogn6axhbi7bo4ojfcoplxlc2dqlipb6 failed
install.oe125375.3.proc4:==> Warning: Skipping build of bcftools-1.14-ve3t4kitjapu5olbvrzu6vidirjm5lga since htslib-1.14-lo5icmlwefk5wqxi3od62a44iuhwdvey failed
install.oe125375.3.proc4:==> libunwind: Successfully installed libunwind-1.6.2-oo5nxgvnhlvvb5ss3u7lp45w2pvljyre
install.oe125375.3.proc4:==> Installing libwhich-1.1.0-rjvzsgwjhctdvjmt4i244y4nypwsbizq
install.oe125375.3.proc4:==> libwhich: Successfully installed libwhich-1.1.0-rjvzsgwjhctdvjmt4i244y4nypwsbizq
install.oe125375.3.proc4:==> Installing openlibm-0.8.1-6kxnrqgegmpnj3dcnjqpt5tiqxevdb22
install.oe125375.3.proc4:==> openlibm: Successfully installed openlibm-0.8.1-6kxnrqgegmpnj3dcnjqpt5tiqxevdb22
install.oe125375.4.proc1:==> Installing environment hugeset
install.oe125375.4.proc1:==> Installing autoconf-archive-2022.02.11-u23emwws43jz7bb6zsdy2fca5yeawhqz
install.oe125375.4.proc1:==> autoconf-archive: Successfully installed autoconf-archive-2022.02.11-u23emwws43jz7bb6zsdy2fca5yeawhqz
install.oe125375.4.proc1:==> Installing energyplus-9.3.0-63nzrnchzwcdltbgpwocaprpnafziz55
install.oe125375.4.proc1:==> energyplus: Successfully installed energyplus-9.3.0-63nzrnchzwcdltbgpwocaprpnafziz55
install.oe125375.4.proc1:==> Installing ghostscript-fonts-8.11-dpfnbqq6yhq56vtfb5alwvm7eqgy7fvq
install.oe125375.4.proc1:==> ghostscript-fonts: Successfully installed ghostscript-fonts-8.11-dpfnbqq6yhq56vtfb5alwvm7eqgy7fvq
install.oe125375.4.proc1:==> Installing dsfmt-2.2.5-ujpr5ffhthr6352yux2rb2zkwg25cck4
install.oe125375.4.proc1:==> dsfmt: Successfully installed dsfmt-2.2.5-ujpr5ffhthr6352yux2rb2zkwg25cck4
install.oe125375.4.proc1:==> Installing libuv-julia-1.44.2-5pnorhq4amjeod2wwp3tjc2njusc4v27
install.oe125375.4.proc1:==> libuv-julia: Successfully installed libuv-julia-1.44.2-5pnorhq4amjeod2wwp3tjc2njusc4v27
install.oe125375.4.proc2:==> Installing environment hugeset
install.oe125375.4.proc2:==> Installing cuba-4.2.2-y7ajhkrwwjbz5r55elvmrl36dsx2wgsm
install.oe125375.4.proc2:==> cuba: Successfully installed cuba-4.2.2-y7ajhkrwwjbz5r55elvmrl36dsx2wgsm
install.oe125375.4.proc2:==> Installing sed-4.8-rs3sffmiwugzsukcvsa5lu7qpvjkqz7v
install.oe125375.4.proc2:==> sed: Successfully installed sed-4.8-rs3sffmiwugzsukcvsa5lu7qpvjkqz7v
install.oe125375.4.proc3:==> Installing environment hugeset
install.oe125375.4.proc3:==> Installing argtable-2-13-4lax3vm65oyzmi6fto3vlmiy7h5fnx3x
install.oe125375.4.proc3:==> argtable: Successfully installed argtable-2-13-4lax3vm65oyzmi6fto3vlmiy7h5fnx3x
install.oe125375.4.proc3:==> Installing alsa-lib-1.2.3.2-nnfeef7wssbq3brhstul3t3fi33dc7j7
install.oe125375.4.proc3:==> alsa-lib: Successfully installed alsa-lib-1.2.3.2-nnfeef7wssbq3brhstul3t3fi33dc7j7
install.oe125375.4.proc3:==> Installing mbedtls-2.28.0-ihtjs23rbhb3bjhcygosxuhygh7xchxm
install.oe125375.4.proc3:==> mbedtls: Successfully installed mbedtls-2.28.0-ihtjs23rbhb3bjhcygosxuhygh7xchxm
install.oe125375.4.proc3:==> Installing p7zip-16.02-r4jrcc5xwlvhen2xqmqhj24crqts3e2o
install.oe125375.4.proc3:==> p7zip: Successfully installed p7zip-16.02-r4jrcc5xwlvhen2xqmqhj24crqts3e2o
install.oe125375.4.proc4:==> Installing environment hugeset
install.oe125375.4.proc4:==> Installing pcre-8.45-o66via4div6iaq52e2tgslyhz5qascy7
install.oe125375.4.proc4:==> pcre: Successfully installed pcre-8.45-o66via4div6iaq52e2tgslyhz5qascy7
install.oe125375.4.proc4:==> Installing xcb-proto-1.14.1-ugxzyao67pdde5f7tcmvcn6cbhvm77as
install.oe125375.4.proc4:==> xcb-proto: Successfully installed xcb-proto-1.14.1-ugxzyao67pdde5f7tcmvcn6cbhvm77as
install.oe125375.4.proc4:==> Installing libogg-1.3.5-23rccsawokuzjkkk2wwmoklqmwskai3w
install.oe125375.4.proc4:==> libogg: Successfully installed libogg-1.3.5-23rccsawokuzjkkk2wwmoklqmwskai3w
install.oe125375.4.proc4:==> Installing libblastrampoline-5.2.0-m62w4wsqgzrzxvxjkg7o3afumrek6ram
install.oe125375.4.proc4:==> libblastrampoline: Successfully installed libblastrampoline-5.2.0-m62w4wsqgzrzxvxjkg7o3afumrek6ram
install.oe125375.4.proc4:==> Installing patchelf-0.16.1-oq2gjuzkdyxj63ptsgk5rjmubhg3bsqp
install.oe125375.4.proc4:==> patchelf: Successfully installed patchelf-0.16.1-oq2gjuzkdyxj63ptsgk5rjmubhg3bsqp
install.oe125375.5.proc1:==> Installing environment hugeset
install.oe125375.5.proc1:==> Installing pkgconf-1.8.0-d35wfgekek4kpbm5vzpiyty5lpjre26a
install.oe125375.5.proc1:==> pkgconf: Successfully installed pkgconf-1.8.0-d35wfgekek4kpbm5vzpiyty5lpjre26a
install.oe125375.5.proc1:==> Installing gsl-2.7.1-mwifqmyefktypr6vowf57teuk5hr4ntp
install.oe125375.5.proc1:==> gsl: Successfully installed gsl-2.7.1-mwifqmyefktypr6vowf57teuk5hr4ntp
install.oe125375.5.proc1:==> Installing nghttp2-1.47.0-hxnf3zgohh2w5wu5mxxvzf4htlzwb7ws
install.oe125375.5.proc1:==> nghttp2: Successfully installed nghttp2-1.47.0-hxnf3zgohh2w5wu5mxxvzf4htlzwb7ws
install.oe125375.5.proc1:==> Installing util-linux-uuid-2.38.1-gr4i5ovwp22s4ptuqlsnfcmn2le2feb2
install.oe125375.5.proc1:==> util-linux-uuid: Successfully installed util-linux-uuid-2.38.1-gr4i5ovwp22s4ptuqlsnfcmn2le2feb2
install.oe125375.5.proc1:==> Installing ncurses-6.3-a6omag2aqvbqvrp6xgyc2ssmrwlvt32l
install.oe125375.5.proc1:==> ncurses: Successfully installed ncurses-6.3-a6omag2aqvbqvrp6xgyc2ssmrwlvt32l
install.oe125375.5.proc1:==> Installing printproto-1.0.5-l7l6k7dhsgfmeiktowghb2wb5hdtvq2j
install.oe125375.5.proc1:==> printproto: Successfully installed printproto-1.0.5-l7l6k7dhsgfmeiktowghb2wb5hdtvq2j
install.oe125375.5.proc1:==> Installing xbitmaps-1.1.1-ce7boepmzudbm5uoec7mmf75xj3w2op6
install.oe125375.5.proc1:==> xbitmaps: Successfully installed xbitmaps-1.1.1-ce7boepmzudbm5uoec7mmf75xj3w2op6
install.oe125375.5.proc1:==> Installing xproto-7.0.31-zb5sk27ondc6jecotl6mfidyntj4qnts
install.oe125375.5.proc1:==> xproto: Successfully installed xproto-7.0.31-zb5sk27ondc6jecotl6mfidyntj4qnts
install.oe125375.5.proc1:==> Installing inputproto-2.3.2-vvlq4h4f6slcqtsoje7rbhf7rlpmfoec
install.oe125375.5.proc1:==> inputproto: Successfully installed inputproto-2.3.2-vvlq4h4f6slcqtsoje7rbhf7rlpmfoec
install.oe125375.5.proc1:==> Installing compositeproto-0.4.2-zimks2ukbfvbfet5sa4vqbidlbbh5i3w
install.oe125375.5.proc1:==> compositeproto: Successfully installed compositeproto-0.4.2-zimks2ukbfvbfet5sa4vqbidlbbh5i3w
install.oe125375.5.proc1:==> Installing glproto-1.4.17-rijsejtno36tghrlt4l73gkpffqoire6
install.oe125375.5.proc1:==> glproto: Successfully installed glproto-1.4.17-rijsejtno36tghrlt4l73gkpffqoire6
install.oe125375.5.proc1:==> Installing kbproto-1.0.7-u6yy3qp657a7ktaw5j6cmpeihslxdmwy
install.oe125375.5.proc1:==> kbproto: Successfully installed kbproto-1.0.7-u6yy3qp657a7ktaw5j6cmpeihslxdmwy
install.oe125375.5.proc1:==> Installing fontsproto-2.1.3-hcpfs6tllbo2n4ybkojopzjaa4oscyze
install.oe125375.5.proc1:==> fontsproto: Successfully installed fontsproto-2.1.3-hcpfs6tllbo2n4ybkojopzjaa4oscyze
install.oe125375.5.proc1:==> Installing fixesproto-5.0-upmef5bd76jxfp7wahgfjl47qcvis5eg
install.oe125375.5.proc1:==> fixesproto: Successfully installed fixesproto-5.0-upmef5bd76jxfp7wahgfjl47qcvis5eg
install.oe125375.5.proc1:==> Installing randrproto-1.5.0-gglhqvzyowqb75eavlcmc3xh522vbc4k
install.oe125375.5.proc1:==> randrproto: Successfully installed randrproto-1.5.0-gglhqvzyowqb75eavlcmc3xh522vbc4k
install.oe125375.5.proc1:==> Installing xtrans-1.3.5-rrxez7babchyyzuyanwarhjcjq2mmvtx
install.oe125375.5.proc1:==> xtrans: Successfully installed xtrans-1.3.5-rrxez7babchyyzuyanwarhjcjq2mmvtx
install.oe125375.5.proc1:==> Installing xextproto-7.3.0-davos7tlcay5ikaqm67cvgf3j5jnqfd6
install.oe125375.5.proc1:==> xextproto: Successfully installed xextproto-7.3.0-davos7tlcay5ikaqm67cvgf3j5jnqfd6
install.oe125375.5.proc1:==> Installing renderproto-0.11.1-jhwf4ox4lxzxyreq6jagk23a3fourafk
install.oe125375.5.proc1:==> renderproto: Successfully installed renderproto-0.11.1-jhwf4ox4lxzxyreq6jagk23a3fourafk
install.oe125375.5.proc2:==> Installing environment hugeset
install.oe125375.5.proc2:==> Installing cpio-2.13-6w35mt3dtcqtkuy4uaiqpfosgwznq54c
install.oe125375.5.proc2:==> cpio: Successfully installed cpio-2.13-6w35mt3dtcqtkuy4uaiqpfosgwznq54c
install.oe125375.5.proc3:==> Installing environment hugeset
install.oe125375.5.proc3:==> Installing berkeley-db-18.1.40-4yotlfajrensotggot44np7ja5el66c2
install.oe125375.5.proc3:==> berkeley-db: Successfully installed berkeley-db-18.1.40-4yotlfajrensotggot44np7ja5el66c2
install.oe125375.5.proc4:==> Installing environment hugeset
install.oe125375.5.proc4:==> Installing libiconv-1.16-cqbivs7hpfromdqcbtpgpvr7qbx2ivbj
install.oe125375.5.proc4:==> libiconv: Successfully installed libiconv-1.16-cqbivs7hpfromdqcbtpgpvr7qbx2ivbj