alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(plain_text,shift_amount):


    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
    
    # Holds the text position that helps in updating text list
    i=0

    # String are immutable in python so changing it to list
    cipher_list=list(text)

    # Final output or the cipher text
    cipher_text=''

    # Looping each letter of text
    for letter in text:
        # Original Index of the letter in alphabet list
        index=alphabet.index(letter)
        # print(index, letter)

        # Shifting the index in alphabet list
        changed_index=index+shift

        # Length of alphabet list
        len_alphabet = len(alphabet)
        
        # For array out of index problem
        if(changed_index>=len_alphabet):
            changed_index=changed_index-len_alphabet
            cipher_list[i]=alphabet[changed_index]
        else:
            cipher_list[i]=alphabet[changed_index]
        
        i+=1

    cipher_text=''.join(cipher_list)
    print(cipher_text)

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
if direction=='encode':
    encrypt(plain_text=text,shift_amount=shift)
