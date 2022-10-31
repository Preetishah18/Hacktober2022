"""
Returns the character occurence count in key value pair
key : character
value : count
"""
inp_str="HacktoberFest2022"
op_dict={}

for chr in inp_str:
    if chr not in op_dict:
        op_dict[chr]=1
    else:
        op_dict[chr]+=1

print(op_dict)