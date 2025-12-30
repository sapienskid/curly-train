"""
Expreriments Plan for Matrix Encryption Walk.
This script runs a series of experiments on the MEW encryption scheme.
## Expreriment Goals
- Evaluate the security and performance of our MEW implementation.
- Test encryption/decryption correctness for various plaintexts and key sizes.
- Measure speed and memory usage for different message lengths.
- Optionally, analyze resistance to simple attacks (e.g., avalanche effect, key sensitivity).
## Experimental Variables
- Key size: Try different matrix sizes (e.g., 8x8, 16x16, 32x32, 64x64).
- Plaintext length: Short, medium, and long messages.
- Random keys: Use multiple random seeds for key generation.
## Metrics to Collect
- Encryption and decryption time.
- Ciphertext length vs. plaintext length.
- Success/failure of decryption (does output match input?).
- (Optional) Bit-flip/avalanche effect: How much does ciphertext change if you flip one bit in plaintext or key?
## Experiment Script Structure
Loop over key sizes and plaintexts.
For each, generate random keys, encrypt, decrypt, and record results.
Print or save results in a table or CSV for analysis.
"""
import secrets
from mew import MEW
# helpers used by experiments
def flip_random_bit(data: bytes) -> bytes:
    ba = bytearray(data)
    if len(ba) == 0:
        return bytes(ba)
    byte_idx = secrets.randbelow(len(ba))
    bit_idx = secrets.randbelow(8)
    ba[byte_idx] ^= (1 << bit_idx)
    return bytes(ba)

def count_different_bits(b1: bytes, b2: bytes) -> int:
    min_len = min(len(b1), len(b2))
    diff = 0
    for i in range(min_len):
        diff_bits = b1[i] ^ b2[i]
        diff += diff_bits.bit_count()
    # account for any extra bytes in the longer value
    if len(b1) > min_len:
        for i in range(min_len, len(b1)):
            diff += b1[i].bit_count()
    elif len(b2) > min_len:
        for i in range(min_len, len(b2)):
            diff += b2[i].bit_count()
    return diff
#Execution Time
# For each key size and data length combination:
# - Run 1000 iterations
# - Measure encryption time
# - Measure decryption time
# - Calculate mean value

iterations = 1000

for key_size in [8, 16, 32, 64, 128, 256]:
    for data_length in [1024, 2048, 4096, 8192, 16384]:
        # Generate random plaintext
        plaintext = secrets.token_bytes(data_length)
        
        # Time encryption (1000 iterations)
        # Time decryption (1000 iterations)
        # Record results


# Key Generation Time
# For each key size:
# - Run 5000 iterations
# - Measure time to generate both key matrices
# - Calculate mean value

iterations = 5000
for key_size in [8, 16, 32, 64, 128, 256]:
    # Time key generation (5000 iterations)
    # Record results
    pass

#Memory Allocation

# For each key size:
# - Measure bytes required to store both key matrices

for key_size in [8, 16, 32, 64, 128, 256]:
    # Measure memory for km1 and km2
    # Record in bytes
    pass

#Avalanche Effect

# For each combination:
# - Run 1000 iterations
# - Flip a single random bit in plaintext
# - Compare original and modified ciphertext
# - Calculate percentage of bits changed

iterations = 1000

for key_size in [64, 128, 256]:
    for plaintext_length in [256, 512, 1024, 2048, 4096, 8192, 16382, 32764]:
        # Generate random plaintext
        plaintext = secrets.token_bytes(plaintext_length)
        
        # Encrypt original
        ciphertext1 = mew.encrypt(plaintext)
        
        # Flip ONE random bit in plaintext
        modified_plaintext = flip_random_bit(plaintext)
        
        # Encrypt modified
        ciphertext2 = mew.encrypt(modified_plaintext)
        
        # Calculate avalanche effect
        changed_bits = count_different_bits(ciphertext1, ciphertext2)
        total_bits = len(ciphertext1) * 8
        avalanche_percentage = (changed_bits / total_bits) * 100