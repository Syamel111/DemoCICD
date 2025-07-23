terraform {
  backend "s3" {
    bucket         = "my2025-terraform-bucket"
    key            = "resume-api.tfstate"
    region         = "ap-southeast-1"
    dynamodb_table = "terraform-lock"
    encrypt        = true
  }
}

