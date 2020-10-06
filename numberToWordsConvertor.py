awww={4:"trillion",3:"billion", 2:"million" ,1:"thousand"}

ones={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
elevens={0:"ten",1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'forteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen',9:'ninteen'}
tens={20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',80:"eighty",90:"ninety"}

def convert(num):
    a=list(str(num).rjust(3,"0"))
    if a[1]!="1":
        string=(ones.get(int(a[0]),"") +" "+ ("Hundred" if a[0] !="0" else "")+ " "+
                tens.get(int((a[1]+"0")),"")+" "+
                ones.get(int(a[2]),""))
    else:
        string=(ones.get(int(a[0]),"") +" "+ ("Hundred" if a[0] !="0" else "")+ " "+
                elevens.get(int((a[2])),"")+" ")

    return string.strip()

class word:

    def __init__(self,number):
        self.number=str(number)
    def towords(self):

        finalstring=""
        if self.number=="0":
            finalstring= "zero"
        i=1
        portion=self.number[-3*i:]
        while len(portion)>=1:
            if portion=="000":
                i = i + 1
                portion = self.number[-3 * i:-3 * i + 3]
                continue
            finalstring= convert(int(portion))+" "+awww.get(i-1,"")+" "+finalstring
            i=i+1
            portion=self.number[-3*i:-3*i+3]
        return finalstring.strip().capitalize()

#number=999999999
#print(word(number).towords() if number<=999_000_000_000_000 else exec("print('Enter less than 1000 Trillion')"))


for i in range(100,103,1):
    print(word(i).towords())



