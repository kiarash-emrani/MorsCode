# explain: this program convert characters to morse code
dic = {
    "A":"o-",
    "B":"-ooo",
    "C":"-o-o",
    "D":"-oo",
    "E":"o"
}
while True:
    mors = input(" harf khod ra vared koni : ")
    mors = mors.upper()
    print(dic[mors])
    
    
    