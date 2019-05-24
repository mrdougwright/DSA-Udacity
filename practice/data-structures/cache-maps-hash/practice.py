# not great hash function
def hash_function(string):
    hash_code = 0
    for char in string:
        hash_code += ord(char)
    return hash_code

# notes
# For a number, say 578, we can represent this number in base 10 number system as
# 5 ∗ 102+7 ∗ 101+8 ∗ 100
# 
# Similarly, we can treat abcde as
# 𝑎 ∗ 𝑝4+𝑏 ∗ 𝑝3+𝑐 ∗ 𝑝2+𝑑 ∗ 𝑝1+𝑒 ∗ 𝑝0
