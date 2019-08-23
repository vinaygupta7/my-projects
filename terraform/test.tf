resource "aws_security_group" "web-node" {
  name = "web-node"
  description = "Web Security Group"
  ingress {
    from_port = 8080
    to_port = 8080
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web-node" {
  ami = "ami-009110a2bf8d7dd0a"
  instance_type = "t2.micro"
  security_groups = ["${aws_security_group.web-node.name}"]

  user_data = <<-EOF
              #!/bin/bash
              echo "Hello Vinay, From Terraform  World" > index.html
              nohup busybox httpd -f -p 8080 &
              EOF

  tags = {
    Name = "terraform-dev"
  }

}
