import argparse
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken


def generate_key(output_file: Path) -> None:
    key = Fernet.generate_key()
    output_file.write_bytes(key)
    print(f"[+] Key saved to {output_file}")


def load_fernet(key_file: Path) -> Fernet:
    if not key_file.exists():
        raise FileNotFoundError(f"Key file not found: {key_file}")
    key = key_file.read_bytes().strip()
    return Fernet(key)


def encrypt_file(key_file: Path, input_file: Path, output_file: Path) -> None:
    fernet = load_fernet(key_file)
    data = input_file.read_bytes()
    encrypted = fernet.encrypt(data)
    output_file.write_bytes(encrypted)
    print(f"[+] Encrypted file written to {output_file}")


def decrypt_file(key_file: Path, input_file: Path, output_file: Path) -> None:
    fernet = load_fernet(key_file)
    encrypted_data = input_file.read_bytes()
    try:
        decrypted = fernet.decrypt(encrypted_data)
    except InvalidToken as error:
        raise ValueError("Invalid key or corrupted encrypted file") from error
    output_file.write_bytes(decrypted)
    print(f"[+] Decrypted file written to {output_file}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="File Encryption & Decryption System")
    subparsers = parser.add_subparsers(dest="command", required=True)

    key_parser = subparsers.add_parser("generate-key", help="Generate a Fernet key")
    key_parser.add_argument("--out", default="secret.key", help="Output key file")

    enc_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    enc_parser.add_argument("--key", required=True, help="Path to key file")
    enc_parser.add_argument("--in", dest="input_file", required=True, help="Input file path")
    enc_parser.add_argument("--out", required=True, help="Encrypted output file path")

    dec_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    dec_parser.add_argument("--key", required=True, help="Path to key file")
    dec_parser.add_argument("--in", dest="input_file", required=True, help="Encrypted input file path")
    dec_parser.add_argument("--out", required=True, help="Decrypted output file path")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "generate-key":
        generate_key(Path(args.out))
    elif args.command == "encrypt":
        encrypt_file(Path(args.key), Path(args.input_file), Path(args.out))
    elif args.command == "decrypt":
        decrypt_file(Path(args.key), Path(args.input_file), Path(args.out))


if __name__ == "__main__":
    main()
