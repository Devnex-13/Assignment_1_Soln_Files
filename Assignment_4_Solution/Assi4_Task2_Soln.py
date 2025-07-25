with open('output.txt','w') as f:
    content = input("Enter text to write to the file:")
    f.write(content)
    print("Data successfully written to output.txt.")
print("\n")

f= open('output.txt','a+')
content1 = input("Enter additional text to append:")
f.write("\n"+content1)
print("Data successfully appended.")
f.close()
print("\n")

with open('output.txt','r') as f:
    print("Final Content of output.txt:")
    for line in f.readlines():
        print(line)