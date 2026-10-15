from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def aes_mode_ecb_basic(texto_plano, clave_cifrado):

    # Cifrado sin padding
    try:
        AES_algoritmo_cifrado = AES.new(clave_cifrado, AES.MODE_ECB)
        AES_algoritmo_cifrado.encrypt(texto_plano)
    except ValueError as e:
        print(f"Error ECB sin padding: {e}")

    # Añadir padding al texto plano (bytes nulos)
    texto_plano_padding = texto_plano
    while len(texto_plano_padding) % 16 != 0:
        texto_plano_padding += b"\x00"

    # Cifrado AES modo ECB
    print(f"Texto con padding: {texto_plano_padding} (Longitud: {len(texto_plano_padding)} bytes)")
    AES_algoritmo_cifrado = AES.new(clave_cifrado, AES.MODE_ECB)
    texto_cifrado_ecb = AES_algoritmo_cifrado.encrypt(texto_plano_padding)
    print(f"Texto cifrado ECB: {texto_cifrado_ecb} (Longitud: {len(texto_cifrado_ecb)} bytes)\n")
    return texto_cifrado_ecb


def aes_mode_ctr_basic(texto_plano, clave_cifrado):

    # Cifrado SIN padding: CTR funciona como cifrado de flujo y admite cualquier longitud
    AES_algoritmo_cifrado = AES.new(clave_cifrado, AES.MODE_CTR)
    nonce = AES_algoritmo_cifrado.nonce  # aleatorio; es necesario para descifrar
    texto_cifrado_ctr = AES_algoritmo_cifrado.encrypt(texto_plano)
    print(f"Nonce CTR: {nonce.hex()}")
    print(f"Texto cifrado CTR: {texto_cifrado_ctr} (Longitud: {len(texto_cifrado_ctr)} bytes)")

    # Descifrado de comprobación
    AES_algoritmo_descifrado = AES.new(clave_cifrado, AES.MODE_CTR, nonce=nonce)
    texto_descifrado = AES_algoritmo_descifrado.decrypt(texto_cifrado_ctr)
    print(f"Texto descifrado CTR: {texto_descifrado}\n")
    return texto_cifrado_ctr


if __name__ == "__main__":

    texto_plano = input("Introduce un mensaje para Bob: ").encode("utf-8")

    # Parte 1: clave de 128 bits (16 bytes)
    clave_cifrado = b'A\x83\xbeU\xd7\xa9b\x18\x85AN0\xbft\xc3\xab'
    print(f"\n=== Clave de {len(clave_cifrado) * 8} bits ===")
    aes_mode_ecb_basic(texto_plano, clave_cifrado)
    aes_mode_ctr_basic(texto_plano, clave_cifrado)

    # Parte 2: clave de 256 bits (32 bytes)
    clave_cifrado_256 = get_random_bytes(32)
    print(f"=== Clave de {len(clave_cifrado_256) * 8} bits ===")
    aes_mode_ecb_basic(texto_plano, clave_cifrado_256)
    aes_mode_ctr_basic(texto_plano, clave_cifrado_256)
