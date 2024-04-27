import rsa


# Define the number of messages that we want to encrypt (in our case,
# we want to decrypt two cipher texts, so we initialize it = 2)
NUM_MESSAGES = 2


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
    # Decrpyt each of the cipher text files specfied by
    # the total number of messages to decrypt
    for i in range(NUM_MESSAGES):
        print(f"MESSAGE #{i+1}\n")
        # Call the function decrypt for cipher text #1
        msg = decrypt(priv_key_file="prv.key", cipher_file=f"cipher{i+1}.bin").decode()
        # Print it and pipe the contents to output1.txt
        print(msg, "\n")
        with open(f"to_plaintxt{i+1}.txt", "w") as text_file:
            text_file.write(msg)

    print("Finished decrypting all messages!")
