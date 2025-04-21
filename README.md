# ☁️ Simplified File-Sharing Web App on AWS

A lightweight Flask-based web app that allows users to upload and download files via a simple web interface. Built as a college Cloud Computing project with [Ahmed Refaat](https://github.com/), this app demonstrates the use of **Amazon EC2**, **S3**, **IAM**, and **VPC**.

---

## 🔧 Features

- 📤 Upload files using a clean web interface  
- 🗂 Store files securely in an Amazon S3 bucket  
- 🔗 Get a direct download link after upload  
- 📃 List uploaded files in the UI  
- 🎨 Styled with basic HTML/CSS  
- 🔐 IAM role securely connects EC2 to S3  
- 🌐 Deployed inside a public subnet in a custom VPC  
- 📃 Listed uploaded files in the UI
---

## 🧱 Technologies Used

| Service      | Purpose                             |
|--------------|-------------------------------------|
| Flask        | Backend framework                   |
| Amazon EC2   | Hosts the web application           |
| Amazon S3    | Stores uploaded files               |
| IAM Role     | Grants secure access to S3 from EC2 |
| Amazon VPC   | Isolates and secures the network    |

---

## 🚀 How to Run

1. **SSH into EC2**  
```bash
ssh -i "your-key.pem" ubuntu@your-ec2-ip
```

2. **Install dependencies**
  ```bash
  sudo apt update -y
  sudo apt install python3-pip -y
  pip3 install flask boto3
  ```

3. **Configure `app.py`**
  ```bash
  S3_BUCKET = "your-bucket-name"
  S3_REGION = "your-region"
  ```
4. **Run the app**
  ```bash
  python3 app.py
  ```
5. **Access the app**
  Visit: `http://<your-ec2-public-ip>`

![app overview](https://github.com/user-attachments/assets/1b51e3e5-cf31-4f35-909e-89fdb1a2f87e)
___


👨‍💻 Made By
- Seif Eldeen

- Ahmed Refaat


