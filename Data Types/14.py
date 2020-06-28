'''Write a Python function to create the HTML string with tags around the
word(s).'''
def add_tags(tag,name):
    print("<%s>%s</%s>"%(tag,name,tag))
t=input("Enter tag")
tag_name=input("Enter tag content")
add_tags(t,tag_name)