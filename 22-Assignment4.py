#โปรแกรมแยกธนบัตร-แลกเงินและหาจำนวนแบงค์

#2000 => 1000=> 2ใบ
#1500 => 1000=> 1ใบ  , 500=> 1ใบ
#1800 => 1000=> 1ใบ  , 500=> 1ใบ , 100=> 3ใบ
'''
หลักความคิดที่ใช้คือ การหารเลขโดยใช้เลขที่นำมาหารคือ เลขธนบัตรนั้นๆ 1000 , 500 , 100 , 50 , 20
และการจะทำให้หาแบงค์อื่นๆได้ต้องนำเศษที่หารได้จากธนบัตรก่อนหน้ามาหารกับธนบัตรต่อไป โดยใช้เครื่องหมาย %
'''
Bank= int(input("ป้อนจำนวนเงินนของคุณ :"))

if Bank >=1000 :
    print("1000 บาท =",Bank//1000 , "ใบ")
    Bank = Bank % 1000

if Bank >=500 :
    print("500 บาท =",Bank//500 , "ใบ")
    Bank = Bank % 500

if Bank >=100 :
    print("100 บาท =",Bank//100 , "ใบ")
    Bank = Bank % 100

if Bank >=50 :
    print("50 บาท =",Bank//50 , "ใบ")
    Bank = Bank % 50

if Bank >=20 :
    print("20 บาท =",Bank//20 , "ใบ")

print ("จบโปรแกรม")
