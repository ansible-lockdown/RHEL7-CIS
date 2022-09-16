resource "aws_vpc" "Main" {
  cidr_block = var.main_vpc_cidr
  instance_tenancy = "default"
  tags       = { 
    Environment = "${var.environment}"
    Name = "${var.namespace}-VPC"
    }
}

resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.Main.id
  tags = {
    Environment = "${var.environment}"
    Name = "${var.namespace}-IGW"
  }
}

resource "aws_subnet" "publicsubnets" {
  vpc_id =  aws_vpc.Main.id
  cidr_block = var.public_subnets
  availability_zone = var.availability_zone
  tags = {
    Environment = "${var.environment}"
    Name = "${var.namespace}-pubsub"
  }
}

resource "aws_subnet" "Main" {
  vpc_id =  aws_vpc.Main.id
  availability_zone = var.availability_zone
  cidr_block = var.private_subnets
  tags = {
    Environment = "${var.environment}"
    Name = "${var.namespace}-prvsub"
  }
}

resource "aws_route_table" "PublicRT" {
   vpc_id =  aws_vpc.Main.id
   route {
   cidr_block = "0.0.0.0/0"
   gateway_id = aws_internet_gateway.IGW.id
   }
   tags = {
    Environment = "${var.environment}"
    Name = "${var.namespace}-publicRT"
  }
}

resource "aws_route_table_association" "rt_associate_public" {
  subnet_id = aws_subnet.Main.id
  route_table_id = aws_route_table.PublicRT.id
}
