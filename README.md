# File Encryption & Decryption System

A CLI tool that encrypts and decrypts files using `Fernet` from the `cryptography` package. Fernet uses AES in CBC mode with HMAC authentication under the hood, making it suitable for beginner cryptography projects.

## Features

- Generate secure encryption keys
- Encrypt any file into ciphertext
- Decrypt ciphertext back to original content
- Clear CLI commands for key/file operations

## Project Structure

```
file-encryption-decryption-system/
  app.py
  requirements.txt
  README.md
```

## Requirements

- Python 3.10+

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Generate key:

```bash
python app.py generate-key --out secret.key
```

2. Encrypt file:

```bash
python app.py encrypt --key secret.key --in plain.txt --out encrypted.bin
```

3. Decrypt file:

```bash
python app.py decrypt --key secret.key --in encrypted.bin --out recovered.txt
```

## Learning Outcomes

- Practical cryptography workflow
- Secure key handling basics
- CLI design with `argparse`
