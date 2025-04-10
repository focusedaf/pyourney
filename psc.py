import sys

def passwordStrengthChecker(password):
   if (len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(not char.isalnum() for char in password)): 
        return 'Strong'
   else:
        return 'Weak'

# please don't remove this code
def main():
    for line in sys.stdin:
        result = passwordStrengthChecker(line.strip())
        sys.stdout.write(result)

if __name__ == "__main__":
    main()
