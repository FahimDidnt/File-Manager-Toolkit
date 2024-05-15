# File-Manager-Toolkit


This Python project provides a suite of file management utilities, including organization, compression, encryption, decryption and basic archive handling.  It aims to improve digital organization, streamline file sharing, and offer a layer of security for sensitive data.







## Features



- **File Organization:** Categorizes files within a target folder based on their extensions (e.g., images, documents, audio, text, etc.)

- **Duplicate Detection:** Duplicate Detection: Implements perceptual hashing and the cv2 library to identify duplicate images and files.

- **ZIP Compression:** Compresses folders into ZIP archives, optimizing storage space and facilitating easy sharing.

- **File Encryption/Decryption:** Utilizes Fernet symmetric encryption (cryptography library) to protect the confidentiality of files.

- **ZIP Extraction:** Offers extraction capabilities for ZIP archives using the patoolib library.





## Skills Utilized

- Python file I/O (os, shutil, zipfile)

- Data structure usage (dictionaries)

- Basic image processing (OpenCV)

- Working with external libraries (cryptography, patoolib, hashlib)

- Implementing symmetric encryption/decryption concepts

## Requirements



- Python 3.x

- Libraries:

    - cryptography

    - patoolib

    - OpenCV

    - hashlib

## Installation

1. **Install Python:** [Download](https://www.python.org/downloads/) and install an appropriate Python distribution.



2. **Install Libraries:** Run the following command in your terminal or command prompt:



```bash

pip install cryptography patoolib opencv-python hashlib

```



3. **Clone the Repository:** Clone the File Organizer repository to your local machine using Git. Open a terminal or command prompt and run the following command:

```bash

git clone https://github.com/FahimDidnt/File-Manager-Toolkit

```

## Usage



#### Execution:

```shell

python main.py

```



#### Menu-Driven Interface: Follow the on-screen prompts to select actions:



1. Organization

2. Compression

3. Encryption

4. Decryption

5. ZIP Extraction



    ##### *Important:* Store the Encryption Key securely, as it's essential for Decryption



    ### Workflow

    1. Start

    2. Choose Action:

    -  Organize Files

    -  Compress Files

    -  Encrypt File/Folder

    -  Decrypt File/Folder

    -  Unzip File

    3. If Action == "Organize Files":

    - Get Folder Path

    - Iterate Through Files:

        - Check File Type

            - If Image:

                - Calculate Image Hash

                - Duplicate Check

            - If Not Image:

                - Calculate File Hash

                - Duplicate Check

        - Organize: Move File to Subfolder Based on Type

    4. If Action == "Compress Files":

    - Get Folder Path

    - Create ZIP Archive

    5. If Action == "Encrypt File/Folder":

    - Get File/Folder Path

    - Key Generation

    - Encryption

    6. If Action == "Decrypt File/Folder":

    - Get File/Folder Path

    - Input Key

    - Decryption

    7. If Action == "Unzip File":

    - Get ZIP File Path

    - Get Destination Folder

    - Extract Files

    8. End



## Contributions

Contributions are welcome! To report issue or suggest features, please open an issue on the repository.
