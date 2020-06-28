'''Write a Python function to insert a string in the middle of a string.'''
def insert_string_middle(symbol,string):
    print(symbol[:2]+string+symbol[-2:])
insert_string_middle('[[]]]','python')
insert_string_middle('{{}}','PHP')