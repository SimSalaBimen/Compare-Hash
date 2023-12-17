import os, hashlib

# Definerer et fast directory
base_directory = r'LEGG TIL FILSTI HER'

def sha256sum(filename):
    sha256_hash = hashlib.sha256()
    with open(filename, 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def compare_hash(filename):
    # Konstruerer stien til filen basert på det faste directoryet
    file_path = os.path.join(base_directory, filename)
    hash_filename = f"{file_path}.hash"

    if os.path.exists(file_path):
        print("Fil funnet!")

        if os.path.exists(hash_filename):
            with open(hash_filename, 'r') as f:
                oldhash = f.read().strip()
            
            current_hash = sha256sum(file_path)

            if current_hash == oldhash:
                print("Checksum/hash er den samme!")
            else:
                print("Fila er ikke den samme lenger!")
        else:
            print("Hash fil finnes ikke her. Kan ikke sammenligne.")
    else:
        print("Fila er ikke her lenger!")

def hash_and_save(filename):
    # Konstruerer stien til filen basert på det faste directory
    file_path = os.path.join(base_directory, filename)
    hash_filename = f"{file_path}.hash"

    if os.path.exists(file_path):
        print("Fil funnet!")

        # Generer hash
        current_hash = sha256sum(file_path)

        # Lagre hashen i ei tekstfil
        with open(hash_filename, 'w') as hash_file:
            hash_file.write(current_hash)

        print(f"Hashen er lagret i {hash_filename}")
    else:
        print("Fila er ikke her lenger!")





# Eksempelbruk:
compare_hash('eksempelfil.txt')
hash_and_save('eksempelfil.txt')
