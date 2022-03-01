// github_actions variables
// Resourced in github_networks.tf
// Declared in variables.tf
// 

namespace         = "github_actions"

// Matching pair name found in AWS for keypairs PEM key
ami_key_pair_name = "github_actions"
main_vpc_cidr     = "172.22.0.0/24"
public_subnets    = "172.22.0.128/26"
private_subnets   = "172.22.0.192/26"