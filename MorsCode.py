# explain: this program convert characters to morse code
dic = {
    "A":"o-",
    "B":"-ooo",
    "C":"-o-o",
    "D":"-oo",
    "E":"o"
}
while True:
    mors = input(" Enter your word : ")
    mors = mors.upper()
    print(dic[mors])
    
    
    
