
# Defining all characters in the form of lists:
alphabets_list_lc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x',
                     'y','z']
alphabets_list_uc = [item.upper() for item in alphabets_list_lc]
numbers_list = ['0','1','2','3','4','5','6','7','8','9']
special_char_list = ['~','!','@','#','$','%','^','&','*','(',')','_','+',' ']

# variables for counters:
alpha_lc_count = 0
alpha_uc_count = 0
numbers_count = 0
special_char_count = 0
with open("junk_text.txt", 'r') as file:
    text = file.read()
    for i in text:
        if i in alphabets_list_lc:
            alpha_lc_count += 1

        if i in alphabets_list_uc:
            alpha_uc_count += 1

        if i in numbers_list:
            numbers_count += 1

        if i in special_char_list:
            special_char_count += 1


print(f"Number of lower case alphabets in the file is {alpha_lc_count}")
print(f"Number of upper case alphabets in the file is {alpha_uc_count}")
print(f"Number of numeric characters in the file is {numbers_count}")
print(f"Number of special characters in the file is {alpha_uc_count}")


