import hashlib

def hash_email_content(email_content):
    return hashlib.sha256(email_content.encode('utf-8')).hexdigest()

def is_spam(email_content, spam_hashes):
    email_hash = hash_email_content(email_content)
    return email_hash in spam_hashes

if __name__ == "__main__":
    spam_hashes = [
        # Precomputed spam hashes
        "d41d8cd98f00b204e9800998ecf8427e"
        # Add other hashes here
    ]
    with open("input.txt", "r") as f:
        email = f.read()
    if is_spam(email, spam_hashes):
        print("Spam detected!")
    else:
        print("Not spam.")
