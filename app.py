from flask import Flask, render_template, request, redirect, url_for
import boto3
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
S3_BUCKET = "my-file-share-bucket2135"
S3_REGION = "eu-north-1"  # e.g., us-east-1

# Create S3 client (uses IAM role permissions)
s3 = boto3.client('s3', region_name=S3_REGION)

@app.route('/')
def index():
    # Fetch list of files in the S3 bucket
    files = s3.list_objects_v2(Bucket=S3_BUCKET)
    file_names = []
    
    if 'Contents' in files:
        file_names = [file['Key'] for file in files['Contents']]
    
    return render_template('index.html', files=file_names, S3_BUCKET=S3_BUCKET, S3_REGION=S3_REGION)

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        s3.upload_fileobj(file, S3_BUCKET, filename)
        return redirect(url_for('index'))  # Redirect back to index to refresh the list of files
    return 'No file selected!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
