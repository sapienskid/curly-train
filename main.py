from mew import MEW

def print_matrix_preview(name, matrix):
    print(f"{name} Preview (Top-Left 4x4:)")
    for r in range(min(4, len(matrix))):
        print(" " + " ". join(f"{b:02x}" for b in matrix [r][:4]))
    print(" ...")

def main():
    print ("--- Matrix Encryption Walk")
    # initialize the walk
    key_size =32
    print (f"Initializing MEW with Key Size {key_size}x{key_size}..."
    )
    mew = MEW(key_size=key_size)
    print_matrix_preview("Key Matrix 1", mew.km1)
    print_matrix_preview("Key Matrix 2", mew.km2)

    # Encrypting the message
    plaintext = "matrix encryption walks"
    print (f"Plaintext: '{plaintext}'")
    cipher_text = mew.encrypt(plaintext)
    print (f"Ciphertext (Hex): {cipher_text.hex()}")
    print (f"Ciphertext Length: {len(cipher_text)} bytes (Original: {len(plaintext)})")
    # Decrypting the message
    decrypted = mew.decrypt(cipher_text)
    print (f"Decrypted: '{decrypted.decode('utf-8')}'")
    if decrypted.decode('utf-8') == plaintext:
        print ("\nSUCCESS: Decryption matched original plaintext.")
    else:
        print ("\nFAILURE: Decryption did not match.")
if __name__ == "__main__":
    main()