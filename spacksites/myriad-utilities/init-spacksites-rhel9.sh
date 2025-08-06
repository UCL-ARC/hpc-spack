# source this - it sets up shell environment variable
# this is to use the installation of hpc spack on Myriad as user ccspapp


if [[ "$USER" == "ccspapp" ]]; then

    TOP_DIR="$(dirname "$(dirname "$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )")")"
    cd "${TOP_DIR}"
    alias sps="${TOP_DIR}/spacksites/spacksites"
    pip install --user pyyaml
    echo "An alias has been set:"
    echo "       $(alias sps)"
    echo "This will disappear if you use 'bash' to get another shell, e.g. prior to entering a particular spack site."
    echo "A dependency, pyyaml, of spacksites has been installed"
    echo "Do an 'sps list' to test."

else

    echo "This script expects that you are using the installation of spack for user ccspapp"
    echo "You are not logged in as such - so this script has done nothing"

fi
