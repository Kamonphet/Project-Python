#ตัวเลขขั้นบันได

'''
ตัวอย่าง int = 4
1
12
123
1234
เป็นต้น
'''
'''
หลักการคิดคือ การป้อนค่าเลขที่อยากจะทำเป็นขึ้นบันไดในลูป for ที่เราสามารถระบุรอบได้ชัดเจน
จากนั้นในแถวแนวตั้ง (row) ก็จะ print เลขออกมา ตามแถวที่เราระบุ 
และเราทำการซ้อนลูป for เข้าไปโดยทำให้ในแต่ละลูปนั้นจะมีแถวแนวนอน (column) ตามที่ระบุด้วยเช่นกัน
'''

last=int(input("ป้อนตัวเลข :"))

for row in range(1,last+1) :
    for column in range (1,row+1) :
        print (column,end='')
    print(" ")

print("จบโปรแกรม")
