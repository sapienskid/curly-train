import secrets
class MEW:
    def __init__(self, key_size=32):
        self.key_size = key_size
        self.km1 = self._generate_key_matrix()
        self.km2 = self._generate_key_matrix()

    def _generate_key_matrix(self):
        """Generate a key_size x key_size matrix with random bytes (0-1023)"""
        matrix = []
        for i in range(self.key_size):
            row = []
            for j in range(self.key_size):
                row.append(secrets.randbelow(1024))
            matrix.append(row)
        return matrix

    def _get_move(self,byte_val):
        """Determine the direction and movement from a byte value.
        Directions:
        00: Down
        11: Up_
        01: Right
        10: Left

        """
        direction = byte_val & 0b11  # Last 2 bits
        movement = byte_val >> 2      # Remaining bits
        return direction, movement
    def _move(self, row, col, direction, movement):
        """Move in the matrix based on direction and movement."""
        if direction == 0b00:  # Down
            row = (row + movement) % self.key_size
        elif direction == 0b11:  # Up
            row = (row - movement) % self.key_size
        elif direction == 0b01:  # Right
            col = (col + movement) % self.key_size
        elif direction == 0b10:  # Left
            col = (col - movement) % self.key_size
        return row, col
        
    def _unmove(self, row, col, direction, movement):
        """Reverse the move in the matrix based on direction and movement."""
        if direction == 0b00:  # Was Down
            row = (row - movement) % self.key_size
        elif direction == 0b11:  # Was Up
            row = (row + movement) % self.key_size
        elif direction == 0b01:  # Was Right
            col = (col - movement) % self.key_size
        elif direction == 0b10:  # Was Left
            col = (col + movement) % self.key_size
        return row, col


    def _pass_encrypt(self, plaintext_bytes, start_row=0, start_col=0):
        """Encrypt a single pass over the plaintext bytes."""
        cipher_bytes = bytearray()
        curr_row, curr_col = start_row, start_col
        for p_byte in plaintext_bytes:
            k1_val = self.km1[curr_row][curr_col]
            t = p_byte^k1_val
            direction,movement = self._get_move(t)
            curr_row, curr_col = self._move(curr_row,curr_col, direction,movement)
            k2_val = self.km2[curr_row][curr_col]
            c_byte = t^k2_val
            cipher_bytes.append(c_byte)
        
        return cipher_bytes,curr_row, curr_col
        
    def _pass_decrypt(self, cipher_bytes, end_row, end_col):
        """Decrypt a single pass over the ciphertext bytes."""
        plaintext_reversed = bytearray()
        curr_row, curr_col = end_row, end_col

        for c_byte in reversed(cipher_bytes):
            k2_val = self.km2[curr_row][curr_col]
            t = c_byte^k2_val
            direction, movement = self._get_move(t)
            prev_row, prev_col = self._unmove(curr_row, curr_col, direction, movement)
            k1_val = self.km1[prev_row][prev_col]
            p_byte = t^k1_val
            plaintext_reversed.append(p_byte)
            curr_row, curr_col = prev_row, prev_col
        
        return bytearray(reversed(plaintext_reversed))

    def encrypt(self, plaintext_str):
        """Encrypt the given plaintext string or bytes."""
        if isinstance(plaintext_str, str):
            data = plaintext_str.encode('utf_8')
        else:
            data = plaintext_str
        
        pass1_out, row, col = self._pass_encrypt(data, 0, 0)

        if self.key_size>1024:
            raise ValueError("Key Size > 1024 requires multi byte coordinate, not implemented yet")

        pass1_out.append(row)
        pass1_out.append(col)
        pass1_reversed = pass1_out[::-1]
        
        pass2_out, final_row, final_col = self._pass_encrypt(pass1_reversed, 0, 0)

        pass2_out.append(final_row)
        pass2_out.append(final_col)

        return bytes(pass2_out)
        
    def decrypt(self, ciphertext_bytes):
        """Decrypt the given ciphertext bytes."""
        if len(ciphertext_bytes)<2:
            raise ValueError("Ciphertext too short")
        final_col = ciphertext_bytes[-1]
        final_row = ciphertext_bytes[-2]
        data = ciphertext_bytes[:-2]
        pass2_decrypted = self._pass_decrypt(data, final_row, final_col)

        pass1_out_full = pass2_decrypted[::-1]

        pass1_col = pass1_out_full[-1]
        pass1_row = pass1_out_full[-2]
        pass1_data = pass1_out_full[:-2]

        plaintext = self._pass_decrypt(pass1_data, pass1_row, pass1_col)

        return bytes(plaintext)
        
        
