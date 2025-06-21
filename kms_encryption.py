from google.cloud import kms

def encrypt_data(project_id, location_id, key_ring_id, key_id, plaintext):
    client = kms.KeyManagementServiceClient()
    key_name = client.crypto_key_path(project_id, location_id, key_ring_id, key_id)

    encrypted = client.encrypt(request={"name": key_name, "plaintext": plaintext.encode("utf-8")})
    print("Encrypted ciphertext:", encrypted.ciphertext)
    return encrypted.ciphertext
