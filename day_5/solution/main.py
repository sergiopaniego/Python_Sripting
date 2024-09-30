# main.py

from my_package import multiply, divide, first_character, last_character

def main():
    # Test math operations
    print("Multiplication of 6 and 3:", multiply(6, 3))
    print("Division of 9 by 3:", divide(9, 3))
    
    # Test string operations
    sample_string = "Hello"
    print("First character:", first_character(sample_string))
    print("Last character:", last_character(sample_string))

if __name__ == "__main__":
    main()
