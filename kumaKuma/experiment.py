lines = 0
with open('primary.txt', 'r') as firstfile:
    for line in firstfile:
        lines += 1
print(lines)

cp = open('primary.txt', 'r')
content = cp.readlines()
a = 0

for line in content:
    for i in line:
        if i.isdigit() == True:
            a+=int(i)

print("The sum is:", a)

firstfile = open('primary.txt', 'r')
secondfile = open('secondary.txt', 'a')
for line in firstfile:
    secondfile.write(line.upper())
secondfile.close()
firstfile.close()

sf = open('secondary.txt', 'r')
con = sf.read()
print(con)

