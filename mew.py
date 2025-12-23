class MEW:
    def __init__(self, key_size=32):
        self.key_size = key_size
        self.km1 = self._generate_key_matrix()
        self.km2 = self._generate_key_matrix()

    def _generate_key_matrix(self):
        """Generate a key_size x key_size matrix with random bytes (0-255)"""
        matrix = []
        for i in range(self.key_size):
            row = []
            for j in range(self.key_size):
                row.append(secrets.randbelow(256))
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
        
    def _pass_encrypt(self)
        pass
    def _pass_decrypt(self)
        pass
    def encrypt(self):
        pass
    def decrypt(self):
        pass
        