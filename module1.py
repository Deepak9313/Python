def cut_whitespace(str):
    res = str.strip()
    return res
# user input string and number
# user want to display the input number word
def find_word(str,num):
    res = str.strip()
    cut = res.split(" ")
    if num <= 0 or num > len(cut):
        return "Enter a valid range"
    else:
        return cut[num-1]