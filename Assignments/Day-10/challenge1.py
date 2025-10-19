# Function with Outputs

def format_name(first_name,last_name):
    # Make it Tile Case. For example Yujan Basnet
    formatted_fname=first_name.title()
    formatted_lname=last_name.title()
    # print(f"After::\nWith Title Case format: {f_name} {l_name}\n")

    # returning as a string. IF directly sent it is as SET
    return f"{formatted_fname} {formatted_lname}"

# print("Before::")
# print("YUJAN BASNET")
# format_name(first_name="YUJAN",last_name="BASNET")


print(format_name(first_name="YUJAN",last_name="BASNET"))