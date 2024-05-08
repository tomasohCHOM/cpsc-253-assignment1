# Import the rsa module - use methods rsa.PrivateKey.load_pkcs1() rsa.decrypt()
import rsa


def decrypt_ciphers(priv_key_file: str, ciphers: list[str]):
    # Decrypt for each cipher filename in ciphers (keep track of indices)
    for i, cipher_file in enumerate(ciphers):
        # Open the private key file path in binary and
        # read its contents into "keydata"
        with open(priv_key_file, "rb") as f:
            keydata = f.read()
        # Load the key in PKCS format and assign it to priv_key
        priv_key = rsa.PrivateKey.load_pkcs1(keydata)

        # Open the cipher file path in binary and read
        # its contents into "crypto"
        with open(cipher_file, "rb") as f:
            crypto = f.read()

        # Decrypt the message using rsa.decrypt() and store the contents in "msg"
        msg = rsa.decrypt(crypto=crypto, priv_key=priv_key).decode()

        # Indicate what message number it is
        print(f"MESSAGE #{i+1}\n")

        # Pipe message contents to to_plaintxt{i+1}.txt
        with open(f"to_plaintxt{i+1}.txt", "w", encoding="windows-1252") as text_file:
            text_file.write(msg)
        # Print the message contents
        print(open(f"to_plaintxt{i+1}.txt", "r", encoding="utf-8").read(), "\n")


# Let ciphers = all the cipher files that we wish to decrypt
ciphers = ["cipher1.bin", "cipher2.bin"]
# Call the decrypt_ciphers functions taking the private key's
# filename and the ciphers to decrypt
decrypt_ciphers(priv_key_file="prv.key", ciphers=ciphers)
