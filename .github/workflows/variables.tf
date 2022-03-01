// Taken from the OSname.tfvars

variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
  type        = string
}

variable "instance_type" {
  description = "EC2 Instance Type"
  default     = "t3.micro"
  type        = string
}

variable "instance_tags" {
  description = "Tags to set for instances"
  type        = map(string)
}

variable "ami_key_pair_name" {
  description = "Name of key pair in AWS thats used"
  type        = string
}

variable "ami_os" {
  description = "AMI OS Type"
  type        = string
}

variable "ami_id" {
  description = "AMI ID reference"
  type = string
}

variable "ami_username" {
  description = "Username for the ami id"
  type        = string
}

variable "ami_user_home" {
  description = "home dir for the username"
  type        = string
}

variable "namespace" {
  description = "Name used across all tags"
  type        = string
}

// taken from github_vars.tfvars &

variable "main_vpc_cidr" {
  description = "Private cidr block to be used for vpc"
  type        = string
}

variable "public_subnets" {
  description = "public subnet cidr block"
  type        = string
}

variable "private_subnets" {
  description = "private subnet cidr block"
  type        = string
}