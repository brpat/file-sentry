import hashlib

class FileHandler:
    def hash_file(src_path: str, hashtype: str = "sha256") -> str:
    # Open the file in binary mode
        with open(src_path, "rb") as f:
            hash_object = None
            # Read the contents of the file
            contents = f.read()

            if hashtype == "sha256":
                # Generate the SHA-256 hash of the contents
                hash_object = hashlib.sha256(contents)
            elif hashtype =="sha1":
                hash_object = hashlib.sha1(contents)

        # Return the hexadecimal representation of the hash
        return hash_object.hexdigest()

    def scan_file_vt(src_path: str):
        #Upload file to virus total
        pass
    
    def diff_file(src_path: str):
        pass
    
    def scan_file_local(src_path: str):
        pass
    
    
