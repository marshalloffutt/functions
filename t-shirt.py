# 8-3 & 8-4

def make_shirt(text, size = 'large'):
    print("One " + size + " t-shirt that says: ")
    print("\t" + text)

make_shirt("hello world", "medium")
make_shirt(text="Hello world", size="small")
make_shirt("Hello world")
make_shirt("O'Doyle rules")