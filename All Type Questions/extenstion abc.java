#Write a Python program to accept a filename from the user and print the extension of that. Sample filename : abc.java Output : java
print("instruction Enter A file name and extenstion abc.java")
print('-------------------------------------------------------------running------------------')
while True:
    try:
        path=input("enter a filename:")
        path=path.split(".")
        get_last_text=path[0]
        filename=get_last_text
        print("file Name:",filename)
        print("file extension:",path[1])
    except:
        print("file not formate ):")








