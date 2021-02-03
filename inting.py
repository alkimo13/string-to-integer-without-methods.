a = "176"
dicti = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
leng =0
for i in a:
    leng=leng+1
x = leng
sayı = 0
for i in a:
    sayı = sayı + dicti[i]*(10**(x-1))
    x = x-1
#multipling outcome with 10 to see if it is integer
print(sayı*10)