# 
print("SECURE LOGIN")
username = input("Username > ")
if username == "mark":
    print("Welcoem Mark!")
elif username == "suzanne":
    print("Hey there Suzanne!")
elif username == "jo":
    print("Yo Jo!")
else:
    print("Go away!")
# new section if we add the password
print("SECURE LOGIN")
username = input("Username > ")
password = input("password> ")

if username == "mark" and password == "password":
    print("Welcoem Mark!")
elif username == "suzanne" and password == "Su74nne":
    print("Hey there Suzanne!")
elif username == "jo":
    print("Yo Jo!")
else:
    print("Go away!")
    