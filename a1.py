class StringReverser:
    """A class to handle string operations, including reversal."""

    def __init__(self, input_string):
        self.original_string = input_string
        self.reversed_string = ""

    def reverse_with_slicing(self):
        """Reverses the string using slicing [::-1] and stores the result."""
        # Slicing creates a new string with characters in reverse order
        self.reversed_string = self.original_string[::-1]
        return self.reversed_string

# --- Example Usage ---
# 1. Create an instance of the class
my_string_object = StringReverser("Hello, World!")

# 2. Call the reversal method
reversed_text = my_string_object.reverse_with_slicing()

# 3. Print the results
print(f"Original: {my_string_object.original_string}")
print(f"Reversed: {reversed_text}")

# You can reuse the class with different strings if needed
another_object = StringReverser("Python")
print(f"\nOriginal: {another_object.original_string}")
print(f"Reversed: {another_object.reverse_with_slicing()}")