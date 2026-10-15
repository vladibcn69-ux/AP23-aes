# AP23-aes — Programa con AES

Laboratorio [AP 23]: cifrado con AES (ECB vs CTR) usando `pycryptodome`.

## Ejecución

```bash
pip install pycryptodome
python aes_lab.py
```

## Parte 1 — Modo CTR (`AES.MODE_CTR`)

Se ha añadido la función `aes_mode_ctr_basic(texto_plano, clave_cifrado)`.

**¿Qué ocurre si intentas cifrar el texto plano (sin padding)?**
En CTR no ocurre ningún error. CTR convierte AES en un cifrado de flujo: cifra un contador (nonce + contador) y hace XOR del resultado con el texto plano, por lo que acepta textos de cualquier longitud. En cambio, en ECB sin padding salta `ValueError: Data must be aligned to block boundary in ECB mode` cuando la longitud no es múltiplo de 16 bytes.

**¿Cuál es el tamaño del texto cifrado resultante?**
Exactamente el mismo que el del texto plano. Por ejemplo, `Hola Bob` (8 bytes) produce 8 bytes cifrados. El nonce (8 bytes, aleatorio) se guarda aparte y es necesario para descifrar.

## Parte 2 — Clave de 256 bits

Se ha usado `get_random_bytes(32)` como clave de 256 bits.

**¿Qué diferencias hay entre el tamaño del texto cifrado en ECB y CTR?**

| Mensaje (bytes) | ECB (con padding) | CTR |
|---|---|---|
| 8 (`Hola Bob`) | 16 | 8 |
| 20 | 32 | 20 |

- ECB trabaja por bloques de 16 bytes, así que necesita padding y el texto cifrado es siempre múltiplo de 16 (mayor o igual que el original).
- CTR no necesita padding y el texto cifrado mide lo mismo que el texto plano.
- El tamaño de la clave (128, 192 o 256 bits) no cambia el tamaño del texto cifrado: el bloque de AES siempre es de 16 bytes. La clave solo cambia el número de rondas (10, 12 o 14).

## Notas de seguridad

- ECB no es seguro: bloques iguales de texto plano producen bloques iguales cifrados.
- En CTR nunca se debe reutilizar el mismo nonce con la misma clave.
