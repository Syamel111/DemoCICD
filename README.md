# 🛠️ Serverless Resume API with Terraform (Week 1 Project)

This project showcases a production-ready **serverless resume API** built entirely with **Terraform**, using AWS Lambda, API Gateway, Secrets Manager, and GitHub Actions for CI/CD.

## 🚀 Features

- **AWS Lambda**: Handles HTTP requests to serve your resume content.
- **API Gateway**: Public REST API for Lambda trigger.
- **Secrets Manager**: Securely stores sensitive resume data (e.g., contact info).
- **Terraform**: Infrastructure as Code — manages full deployment and teardown.
- **CI/CD**: GitHub Actions automates Terraform `plan` and `apply` on push.
- **Remote State Backend**:
  - S3 for `.tfstate`
  - DynamoDB for state locking

## 🧪 Highlights

- ✅ Secure infrastructure (least privilege IAM, no hardcoded secrets)
- ✅ Automated deployment pipeline (GitHub Actions)
- ✅ Remote state & locking using S3 and DynamoDB
- ✅ Clean destroy with `terraform destroy` to avoid idle charges
- ✅ Debugged real-world issues (lock mismatch, GitHub token errors, state desync)

## 📁 Tech Stack

- **Terraform**
- **AWS** (Lambda, API Gateway, Secrets Manager, IAM, S3, DynamoDB)
- **GitHub Actions** for CI/CD
- **Shell + Curl** for local API testing

## 🧠 Lessons Learned

- Built full stack IaC from scratch
- Resolved Terraform state errors with S3 + DynamoDB backend
- Integrated GitHub CI/CD for IaC deployment
- Practiced cost optimization and security best practices

## 🧹 Clean-up

To prevent AWS charges:
```bash
terraform destroy
````

Also remember to manually delete the **S3 bucket** and **DynamoDB table** if they were created outside Terraform.

## 📎 Repository Structure

```bash
.
├── main.tf
├── backend.tf
├── variables.tf
├── outputs.tf
├── lambda/
│   └── main.py
├── secrets.tf
├── .github/
│   └── workflows/
│       └── deploy.yml
```

## 📌 Status

✅ **Completed** Week 1 of Cloud DevOps journey
💡 Prepared for next steps: Monitoring, Secrets Rotation, IAM least privilege enforcement

---
