"""
This file contains call functions to final project of Git course for beggineers.
"""
from etty_dir.etty_palindrom import isPalindrom
from liad_dir.liad_palindrom import is_palindrom

def main():
    s1 = "saippuakivikauppias" 
    s2 = "Malayalam"
    s3 = "BaTHTuB"
    s4 = "ontotonto"
    s5 = "detartrated"
    
    is_palindrom(s1)
    is_palindrom(s2)
    is_palindrom(s3)
    is_palindrom(s4)
    is_palindrom(s5)


#call  ispalindrom() from main
def mainFunc():
    s1 = "saippuakivikauppias"
    s2 = "Malayalam"
    s3 = "BaTHTuB"
    s4 = "ontotonto"
    s5 = "detartrated"

    print(isPalindrom(s1))
    print(isPalindrom(s2))
    print(isPalindrom(s3))
    print(isPalindrom(s4))
    print(isPalindrom(s5))

    
    print("Congratulations on completing the Git course for beginners!")

if __name__ == "__main__":
    main()
    mainFunc()