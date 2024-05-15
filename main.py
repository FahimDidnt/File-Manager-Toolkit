import os
import shutil
import cv2
import hashlib
import zipfile
import patoolib
from cryptography.fernet import Fernet

# Generate encryption key
def generate_key():
    return Fernet.generate_key()

# Encrypt file
def encrypt_file(key, file_path):
    # Load the key and create a Fernet instance
    cipher = Fernet(key)
    
    # Check if the provided path is a file or a folder
    if os.path.isfile(file_path):
        # If it's a file, encrypt the file
        with open(file_path, 'rb') as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(file_path, 'wb') as f:
            f.write(encrypted_data)
        print("File encrypted successfully. Store the encryption key securely, as it is essential for future decryption.")
    elif os.path.isdir(file_path):
        # If it's a folder, encrypt all files within the folder
        for root, _, files in os.walk(file_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted_data = cipher.encrypt(data)
                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)
        print("Folder encrypted successfully. Store the encryption key securely, as it is essential for future decryption.")
    else:
        print("Invalid file or folder path.")

# Decrypt file
def decrypt_file(key, file_path):
    # Load the key and create a Fernet instance
    cipher = Fernet(key)
    
    # Check if the provided path is a file or a folder
    if os.path.isfile(file_path):
        # If it's a file, decrypt the file
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        decrypted_data = cipher.decrypt(encrypted_data)
        with open(file_path, 'wb') as f:
            f.write(decrypted_data)
        print("File decrypted successfully.")
    elif os.path.isdir(file_path):
        # If it's a folder, decrypt all files within the folder
        for root, _, files in os.walk(file_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    encrypted_data = f.read()
                decrypted_data = cipher.decrypt(encrypted_data)
                with open(file_path, 'wb') as f:
                    f.write(decrypted_data)
        print("Folder decrypted successfully.")
    else:
        print("Invalid file or folder path.")

# Get the hash of an image
def get_image_hash(image_path):
    # Read the image and compute its pHash
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(image, (8, 8))  # Resize image to 8x8 pixels
    _, image_hash = cv2.threshold(resized_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return image_hash.flatten().tolist()

# Get the hash of a file
def get_file_hash(file_path):
    # Read the file content and calculate its hash
    with open(file_path, "rb") as f:
        content = f.read()
        file_hash = hashlib.md5(content).hexdigest()  # Using MD5 for simplicity
    return file_hash

# Organize files by type
def organize_by_type(folder_path):
    file_types = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".svg": "Images",
    ".eps": "Images",
    ".psd": "Images",
    ".ai": "Images",
    ".tif": "Images",
    
    ".avi": "Videos",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".swf": "Videos",
    ".flv": "Videos",
    ".wmv": "Videos",
    ".asf": "Videos",
    ".rm": "Videos",
    ".vob": "Videos",
    ".webm": "Videos",
    
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pptx": "Documents",
    ".xlsx": "Documents",
    ".csv": "Documents",
    ".txt": "Documents",
    ".rtf": "Documents",
    ".html": "Documents",
    ".odt": "Documents",
    ".ods": "Documents",
    ".odp": "Documents",
    ".ppt": "Documents",
    ".xls": "Documents",
    ".key": "Documents",
    ".numbers": "Documents",
    ".pages": "Documents",
    
    ".mp3": "Audio",
    ".wav": "Audio",
    ".flac": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
    
    ".exe": "Applications",
    ".apk": "Applications",
    ".bat": "Applications",
    ".msi": "Applications",
    
    ".zip": "ZipFiles",
    ".7z": "ZipFiles",
    ".tar": "ZipFiles",
    ".gz": "ZipFiles",
    ".bz2": "ZipFiles",
    ".xz": "ZipFiles",
    ".z": "ZipFiles",
    ".war": "ZipFiles",
    ".jar": "ZipFiles",
    ".ear": "ZipFiles",
    ".cbz": "ZipFiles",
    ".cbr": "ZipFiles",
    ".deb": "ZipFiles",
    ".rpm": "ZipFiles",
    ".sit": "ZipFiles",
    ".sitx": "ZipFiles",
    ".rar": "RarFiles",
    
    ".iso": "DiskImages",
    ".img": "DiskImages",
    ".nrg": "DiskImages",
    ".toast": "DiskImages",
    ".vcd": "DiskImages",
    
    ".py": "TextFiles",
    ".java": "TextFiles",
    ".cpp": "TextFiles",
    ".h": "TextFiles",
    ".json": "TextFiles",
    ".xml": "TextFiles",
    ".yaml": "TextFiles",
    ".ini": "TextFiles",
    ".cfg": "TextFiles",
    ".log": "TextFiles",
    ".md": "TextFiles",
    ".php": "TextFiles",
    ".asp": "TextFiles",
    ".jsp": "TextFiles",
    
    ".bin": "BinaryFiles",
    ".dat": "BinaryFiles",
    ".db": "DatabaseFiles",
    ".sql": "DatabaseFiles",
    ".dbf": "DatabaseFiles",
    ".csv": "DatabaseFiles",
    
    ".bak": "BackupFiles",
    ".tmp": "TemporaryFiles",
    ".temp": "TemporaryFiles",
}
    
    image_hashes = {}
    file_hashes = {}
    
    # Iterate over files and organize them by type
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            file_extension = os.path.splitext(filename)[1].lower()  # Convert to lowercase for case-insensitive comparison
            file_path = os.path.join(folder_path, filename)
            if file_extension in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".eps", ".psd", ".ai", ".tif"]:
                # Compute image hash for image files
                image_hash = get_image_hash(file_path)
                # Check for duplicate images by comparing hash values
                if tuple(image_hash) in image_hashes:
                    duplicate_file = image_hashes[tuple(image_hash)]
                    choice = input(f"Duplicate image '{filename}' detected. It is identical to '{duplicate_file}'. Do you want to keep (K) or delete (D) it? ").upper()
                    if choice == 'K':
                        # Keep the duplicate image
                        print(f"Keeping duplicate image '{filename}'.")
                    elif choice == 'D':
                        # Delete the duplicate image
                        os.remove(file_path)
                        print(f"Deleting duplicate image '{filename}'.")
                    else:
                        print(f"Invalid choice. Keeping duplicate image '{filename}' by default.")
                else:
                    image_hashes[tuple(image_hash)] = filename
                    folder_name = file_types[file_extension]
                    destination_folder = os.path.join(folder_path, folder_name)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
            else:
                # For non-image files, use MD5 hash of content
                file_hash = get_file_hash(file_path)
                # Check for duplicate files by comparing hash values
                if file_hash in file_hashes:
                    duplicate_file = file_hashes[file_hash]
                    choice = input(f"Duplicate file '{filename}' detected. It is identical to '{duplicate_file}'. Do you want to keep (K) or delete (D) it? ").upper()
                    if choice == 'K':
                        # Keep the duplicate file
                        print(f"Keeping duplicate file '{filename}'.")
                    elif choice == 'D':
                        # Delete the duplicate file
                        os.remove(file_path)
                        print(f"Deleting duplicate file '{filename}'.")
                    else:
                        print(f"Invalid choice. Keeping duplicate file '{filename}' by default.")
                else:
                    file_hashes[file_hash] = filename
                    folder_name = file_types.get(file_extension, "Other")
                    destination_folder = os.path.join(folder_path, folder_name)
                    if not os.path.exists(destination_folder):
                        os.makedirs(destination_folder)
                    shutil.move(file_path, os.path.join(destination_folder, filename))
    print("Files organized successfully.")

# Compress folder to ZIP
def compress_zip(folder_path):
    folder_name = os.path.basename(folder_path)
    zip_filename = os.path.join(os.path.dirname(folder_path), f"{folder_name}.zip")
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # Use relative path within the ZIP file
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
    print("Compression completed successfully.")

# Main function
def main():
    while True:
        choice = input("Choose an option:\n1. Organize Files\n2. Compress Files\n3. Encrypt File\n4. Decrypt File\n5. Unzip File\nEnter your choice (1/2/3/4/5): ")
        if choice == "1":
            folder_path = input("Enter the path of the folder you want to organize: ")
            print("Folder path:", folder_path)
            organize_by_type(folder_path)
        elif choice == "2":
            folder_path = input("Enter the path of the folder you want to compress: ")
            print("Folder path:", folder_path)
            compress_zip(folder_path)
        elif choice == "3":
            file_path = input("Enter the path of the file you want to encrypt: ")
            print("File path:", file_path)
            key = generate_key()
            print("Encryption key:", key.decode())
            encrypt_file(key, file_path)
        elif choice == "4":
            file_path = input("Enter the path of the file you want to decrypt: ")
            print("File path:", file_path)
            key = input("Enter the encryption key:")
            decrypt_file(key.encode(), file_path)
        elif choice == "5":
            zip_path = input("Enter the path of the file you want to unzip: ")
            print("ZIP file path:", zip_path)
            destination_path = input("Enter the path where you want to unzip the files: ")
            print("patool: Extracting {} ...".format(zip_path))
            patoolib.extract_archive(zip_path, outdir=destination_path)
            print("Unzipping completed successfully.")
        else:
            print("Invalid choice. Please choose 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()
