# โปรแกรมหาตัวเลข มาก/น้อย/เท่ากับ


'''
หลักการคิดคือ การป้อนเลขที่เป็นจำนวนเต็มลงไป แล้วทำการตั้งเงื่อนไขโดยการใช้เครื่องหมายเปรียบเทียบ < , > , ==
'''

a = int(input("ป้อนเลขที่ 1 :"))
b = int(input("ป้อนเลขที่ 2 :"))

if a > b:
    print(str(a)+" มากกว่า "+str(b))  # ใส่แบบนี้ก็ได้  print(a,"มากกว่า",b)
elif a == b:
    print(str(a)+" เท่ากับ "+str(b))  # ใส่แบบนี้ก็ได้  print(a,"เท่ากับ",b)
else:
    print(str(a)+" น้อยกว่า "+str(b))  # ใส่แบบนี้ก็ได้  print(a,"น้อยกว่า",b)
print("จบโปรแกรม")
