#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Letters/starting_letter.txt") as f:
    # print(f.read())
    start_letter_content=f.read()

with open("Input/Names/invited_names.txt") as names:
    all_names = names.read().split()    #makes a list fromt the read text


def ready_to_send(name):
    final_letter = start_letter_content.replace("[name]",name)
    with open(f"Output/ReadyToSend/{name}.txt",mode="w") as output:
        output.write(final_letter)

# Sending each name individually
for name in all_names:
    ready_to_send(name)
