string = 'X-DSPAM-Confidence:0.8475'

init = string.find(":")
get_number = float(string[init+1:])
print(get_number)
print(type(get_number))