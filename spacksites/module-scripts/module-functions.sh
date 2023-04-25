# functions for using the modulefiles created with spacksites
# these functions expect:
# (1) the module files are located in sibiling directories, below a root
# (2) that it is wished to present each directory of modulefiles as a separate section in module avail
# (3) the tcl modules prorgam has been initialised 

# further, the convention in spacksites is to locate modulefiles with these settings 
# in the spack environment definition files - of which there will be one per module avail section:
#   modules:
#     default:
#       roots:
#         tcl: $spack/../modules/<module section>/
# where $spack (= $SPACK_ROOT) is the root of the spack site in question
# thus, in this convention, the prarameter spacksites_modules_root = $spack/../modules 

# this file contains bash functions, so the file should be sourced before they are used 

# requires 1 parameter: $1 = path the to root of the sibling directories containing the module files 
function spacksites_use_modules () {
    if [ "$#" -ne 1 ]; then
        echo "ERROR: function spacsites_use_modules () takes exactly 1 argument, which is " >&2
        echo "       the path the to root of the sibling directories containing the module files." >&2
        return 1
    fi
    local spacksites_modules_root = $1
    if [ ! -d ""]
        echo "ERROR: the supplied path (to root of the sibling directories containing " >&2
        echo "       the module files) does not exist." >&2
        return 1
    fi 
    for section_dir in $spacksites_modules_root/*/ ; do
        module use $spacksites_modules_root/$section_dir
    done
    return 0
}

# requires 1 parameter: $1 = path the to root of the sibling directories containing the module files 
function spacksites_unuse_modules () {
    if [ "$#" -ne 1 ]; then
        echo "ERROR: function spacsites_use_modules () takes exactly 1 argument, which is " >&2
        echo "       the path the to root of the sibling directories containing the module files." >&2
        return 1
    fi
    local spacksites_modules_root = $1
    if [ ! -d ""]
        echo "ERROR: the supplied path (to root of the sibling directories containing " >&2
        echo "       the module files) does not exist." >&2
        return 1
    fi 
    for section_dir in $spacksites_modules_root/*/ ; do
        module unuse $spacksites_modules_root/$section_dir
    done
    return 0
}

# requires 1 parameter: $1 = path the to root of the sibling directories containing the module files 
function spacksites_generate_use_modules () {
    if [ "$#" -ne 1 ]; then
        echo "# ERROR: function spacsites_use_modules () takes exactly 1 argument, which is " >&2
        echo "#        the path the to root of the sibling directories containing the module files." >&2
        return 1
    fi
    local spacksites_modules_root = $1
    if [ ! -d "$spacksites_modules_root"]
        echo "# ERROR: the supplied path (to root of the sibling directories containing " >&2
        echo "#        the module files) does not exist." >&2
        return 1
    fi 
    for section_dir in $spacksites_modules_root/*/ ; do
        echo "module use $spacksites_modules_root/$section_dir"
    done
    return 0
}

# requires 1 parameter: $1 = path the to root of the sibling directories containing the module files 
function spacksites_generate_unuse_modules () {
    if [ "$#" -ne 1 ]; then
        echo "# ERROR: function spacsites_use_modules () takes exactly 1 argument, which is " >&2
        echo "#        the path the to root of the sibling directories containing the module files." >&2
        return 1
    fi
    local spacksites_modules_root = $1
    if [ ! -d "$spacksites_modules_root"]
        echo "# ERROR: the supplied path (to root of the sibling directories containing " >&2
        echo "#        the module files) does not exist." >&2
        return 1
    fi 
    for section_dir in $spacksites_modules_root/*/ ; do
        echo "module unuse $spacksites_modules_root/$section_dir"
    done
    return 0
}
