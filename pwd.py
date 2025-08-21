# Import required modules
import random
import string

def generate_password(length=12, use_numbers=True, use_symbols=True):
    """
    Generate a random password with customizable complexity.
    
    Args:
        length (int): Length of the password (default: 12)
        use_numbers (bool): Include numbers (default: True)
        use_symbols (bool): Include symbols (default: True)
    
    Returns:
        str: Generated password
    """
    # Define character sets
    letters = string.ascii_letters  # Uppercase + lowercase letters
    numbers = string.digits if use_numbers else ""  # Numbers (0-9)
    symbols = "!@#$%^&*()_+-=" if use_symbols else ""  # Common symbols
    
    # Combine all allowed characters
    all_chars = letters + numbers + symbols
    
    # Ensure at least one character from each selected set
    password = []
    password.append(random.choice(letters))  # Mandatory letter
    
    if use_numbers:
        password.append(random.choice(numbers))  # Mandatory number
    if use_symbols:
        password.append(random.choice(symbols))  # Mandatory symbol
    
    # Fill remaining length with random choices
    for _ in range(length - len(password)):
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    # Convert list to string and return
    return "".join(password)

if __name__ == "__main__":
    # Example usage
    print("Single password:", generate_password())
    print("Password with 16 chars:", generate_password(length=16))
    print("Numbers only:", generate_password(use_symbols=False))
    print("Symbols only:", generate_password(use_numbers=False))
