#แปลง ค.ศ เป็น พ.ศ + 543
#แปลง พ.ศ เป็น ค.ศ - 543

'''
หลักการคิด คือ การนำเลข ค.ศ หรือ พ.ศ จากการรับข้อมูลมา และทำการ + หรือ - ด้วย 543 ก็จะได้ค่าปี ค.ศ / พ.ศ นั้น ๆ 
'''

Year = int(input("กรุณาป้อนปี ค.ศ :"))

Year = Year + 543

print("เป็นปี พ.ศ :" ,Year)

Years = int(input("กรุณาป้อนปี พ.ศ :"))

Years = Years - 543

print("เป็นปี ค.ศ :" ,Years)

print("จบโปรแกรม")