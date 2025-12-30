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
