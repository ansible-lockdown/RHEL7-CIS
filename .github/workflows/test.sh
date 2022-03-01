RHEL7=$(grep -c RHEL7 OS.tfvars)
if [ `echo $?` != 0 ]; then
   exit 0
fi
    
  
