# Writing data

f = open("credentials.txt", 'w')
f.write("USER_NAME\tPASSWORD\n")
f.write("admin\tpass123\n")
f.write("user1\tabcd")
f.close()


# Reading data
f = open("credentials.txt", "r")
# data = f.read()
# print(data)

print(f.tell())
line1 = f.readline()
f.seek(33)
print(f.tell())
line2 = f.readline()
print(f.tell())

print(line1)
print(line2)
#
# lines = f.readlines()
# print(lines)

f.close()


# Other way of opening a file
with open("credentials.txt") as f:
    print(f.read())
