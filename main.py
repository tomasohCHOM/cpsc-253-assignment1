import rsa


def decrypt(priv_key_file, crypto_file):
    with open(priv_key_file, "rb") as f:
        keydata = f.read()
    priv_key = rsa.PrivateKey.load_pkcs1(keydata)

    with open(crypto_file, "rb") as f:
        crypto = f.read()

    return rsa.decrypt(crypto=crypto, priv_key=priv_key)


if __name__ == "__main__":
    print("MESSAGE #1\n")
    print(decrypt(priv_key_file="prv.key", crypto_file="cipher1.bin"), "\n")
    print("MESSAGE #2\n")
    print(decrypt(priv_key_file="prv.key", crypto_file="cipher2.bin"))
