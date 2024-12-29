def encrypt_text(pt,n): 
    ans1 = "" 
    temp1=pt.lower()
    for i in range(len(temp1)): 
        ch1 = temp1[i] 
        if ch1==" ": 
            ans1+=" " 
        else: 
            ans1 += chr((ord(ch1) + n-97) % 26 + 97) 
    return ans1 
def decrypt_text(pt,n): 
    ans2 = "" 
    temp2=pt.lower()
    for i in range(len(temp2)): 
        ch2 = temp2[i] 
        if ch2==" ": 
            ans2+=" " 
        else: 
            ans2 += chr((ord(ch2) - n-97) % 26 + 97) 
    return ans2 
pt = input("Enter a Text ") 
n = int(input("Enter a shift value: "))
choice=input("Enter Encrypt/Decrypt(E/D): ")
if choice=="E":
    print("Cipher Text is : " + encrypt_text(pt,n)) 
elif choice=="D":
    print("Plain Text is : " + decrypt_text(pt,n)) 
else:
    print("Enter a valid choice")