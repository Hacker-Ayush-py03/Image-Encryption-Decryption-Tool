# Image Encryption and Decryption Tool
=====================================
## Introduction
- This tool provides a simple and secure way to encrypt and decrypt images using a password-based approach. The tool uses a combination of encryption algorithms to ensure the confidentiality and integrity of the images.
## Features
- Encrypts images using a password-based approach
- Decrypts encrypted images using the same password
- Supports various image formats (e.g., JPEG, PNG, BMP)
- Easy to use command-line interface
## Usage
### Encryption
- To encrypt an image, use the following command:
  ```bash
  python3 img_encryption_tool.py <encrypt> <input_image> <output_image> <key>
  ```
### Decryption
To Decrypt an encrypted image, use the foolowing command:
 ```bash
python3 img_encryption_tool.py <decrypt> <encrypted_image> <output_image> <key>
```
## Requirements
- Python 3.x...
- Python Imaging Library
```bash
 pip install PIL
```
- Cryptography Library
- ```bash
  pip install cryptography
  ```
## Installation
1. Clone the repository:
 ```bash
git clone https://github.com/DinooBose/img-encryption-decryption-tool
```
2. Install the requirements
3. Run the tool:
```bash
python3 img_encryption_tool.py
```
4. Key size range: 35 to 255 for strong encryption.
   
## Note
- Make sure to keep the password secure to prevent unauthorized access to the encrypted images.
- The tool uses a combination of encryption algorithms to ensure the confidentiality and integrity of the images. However, it is still important to use a secure password and keep the encrypted images safe.
