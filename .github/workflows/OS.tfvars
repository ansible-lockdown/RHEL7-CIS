#Ami  centos 7.11
ami_id        = "ami-00e87074e52e6c9f9"
ami_os        = "centos7"
ami_username  = "centos"
ami_user_home = "/home/centos"
instance_tags = {
  Name        = "RHEL7-CIS"
  Environment = "lockdown_github_repo_workflow"
}
