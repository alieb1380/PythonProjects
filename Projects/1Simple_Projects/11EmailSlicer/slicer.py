# first thing we should get input from user
# the input should be without spaces
email = input("Enter Your Email: ").strip()

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]

print(f"Your username is {username} & domain is {domain}")