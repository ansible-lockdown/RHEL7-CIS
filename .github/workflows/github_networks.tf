resource "aws_vpc" "Main" {
  cidr_block = var.main_vpc_cidr
  tags = var.instance_tags
}

resource "aws_internet_gateway" "IGW" {
  vpc_id = aws_vpc.Main.id
  tags = {
    Name      = "${var.namespace}-IGW"
  }
}
