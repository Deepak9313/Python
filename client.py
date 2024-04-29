import module1 as m
string = "   I like to watch cartoons and animated movies   "
print(len(string))
res = m.cut_whitespace(string)
print(len(res))
inp = int(input("Enter the number and i will give you word :\n"))
res1 = m.find_word(res,inp)
print(res1)