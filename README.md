# 🔐 Simple Python Password Generator

A customizable CLI password generator written in Python.

## Features
- Adjustable password length.
- Optional inclusion of numbers and symbols.
- Avoids ambiguous characters (e.g., `l` vs `1`).

## Usage
1. **Run the script:**
   ```sh
   python pwd.py
   ```

2. **Generate passwords programmatically:**
   ```python
   from password_generator import generate_password
   
   # Basic password (12 chars, numbers + symbols)
   print(generate_password())
   
   # Customized examples
   print(generate_password(length=16))              # 16 characters
   print(generate_password(use_symbols=False))       # No symbols
   ```

Thanks for checking it out! Feel free to modify and enhance it! 😊
```

You can copy and paste this README into your project. Let me know if you need any further adjustments!
