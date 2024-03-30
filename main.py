import rsa


# Function that, given the private key file path (string) and the
# cipher text file path (string), will decrypt the message contents
# in the cipher text file and return them in binary format.
def decrypt(priv_key_file: str, cipher_file: str) -> bytes:
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

    # Decrypt the message and return it
    return rsa.decrypt(crypto=crypto, priv_key=priv_key)


# Run the code as the main entry point to the program
if __name__ == "__main__":
    print("MESSAGE #1\n")
    # Call the function decrypt for cipher text #1
    msg1 = decrypt(priv_key_file="prv.key", cipher_file="cipher1.bin").decode("utf-8")
    # Print it and pipe the contents to output1.txt
    print(msg1)
    with open("output1.txt", "w", encoding="utf-8") as text_file:
        text_file.write(msg1)

    print("\nMESSAGE #2\n")
    # Call the function decrypt for cipher text #2
    msg2 = decrypt(priv_key_file="prv.key", cipher_file="cipher2.bin").decode("utf-8")
    # Print it and pipe the contents to output2.txt
    print(msg2)
    with open("output2.txt", "w", encoding="utf-8") as text_file:
        text_file.write(msg2)
