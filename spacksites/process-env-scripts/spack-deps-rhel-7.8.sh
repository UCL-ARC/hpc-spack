# source this - it is for setting environment variables
# 
#
# A script to set the working environment for spack 
#
# The environment set is for
# (1) Python - spack is written in Python
# (2) a gcc compiler - spack needs a system compiler at least to bootstrap itself
#
# This script is symlinked as spd 
#
# This code was contributed by Owain Kenway

UCL_SCLS="rh-python38 devtoolset-11"

for a in ${UCL_SCLS}
do
   source "/opt/rh/${a}/enable"
done
export X_SCLS="${UCL_SCLS} ${X_SCLS}"

# TODO: wonder about how this would take precedence or be obscurced by pre or post loaded modules  



