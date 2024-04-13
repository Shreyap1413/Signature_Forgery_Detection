import os

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as fin:
        data = bytearray(fin.read())
    for i in range(len(data)):
        data[i] ^= key
    with open(output_file, 'wb') as fout:
        fout.write(data)

def decrypt_file(input_file, output_file, key):
    encrypt_file(input_file, output_file, key)

def process_folder(input_folder, output_folder, key, operation):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        if os.path.isfile(input_path):
            output_path = os.path.join(output_folder, filename)
            if operation == 'encrypt':
                encrypt_file(input_path, output_path, key)
                print(f"Encrypted {input_path} -> {output_path}")
            elif operation == 'decrypt':
                decrypt_file(input_path, output_path, key)
                print(f"Decrypted {input_path} -> {output_path}")

# Prompt the user to enter the encryption key
encryption_key = int(input("Enter encryption key: "))

# Define paths for input and output folders
input_folder1 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\real'
input_folder2 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\forged'
encrypted_folder_1 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\encrypted_real'
encrypted_folder_2 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\encrypted_forged'
decrypted_folder_1 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\decrypted_real'
decrypted_folder_2 = r'C:\Users\Windows\Desktop\Signature-Forgery-Detection\Signature-Forgery-Detection-main\decrypted_forged'

# Encrypt images from the first input folder
process_folder(input_folder1, encrypted_folder_1, encryption_key, 'encrypt')
print("Images from folder 1 encrypted and saved to:", encrypted_folder_1)

# Encrypt images from the second input folder
process_folder(input_folder2, encrypted_folder_2, encryption_key, 'encrypt')
print("Images from folder 2 encrypted and saved to:", encrypted_folder_2)

# Prompt the user to enter the decryption key
decryption_key = int(input("Enter decryption key: "))

# Decrypt images from the first encrypted folder
process_folder(encrypted_folder_1, decrypted_folder_1, decryption_key, 'decrypt')
print("Images from folder 1 decrypted and saved to:", decrypted_folder_1)

# Decrypt images from the second encrypted folder
process_folder(encrypted_folder_2, decrypted_folder_2, decryption_key, 'decrypt')
print("Images from folder 2 decrypted and saved to:", decrypted_folder_2)