#หาผลรวมของตัวเลข แบบปรับเงื่อนไข

'''
หลักการคิดคือ กาารที่เรามาปรับเปลี่ยนเงื่อนไขนิดหน่อย โดยการเปลี่ยนเป็น while true เพื่อสามารถป้อนเลขกี่ตัวลงตัวไปก็ได้ 
เราจะหยุดลูปนี้ได้โดยใช้เงื่อนไข if และ break แล้วเราก็รระบุเลขผลรวมที่ต้องการที่จะหยุด 
หรือไม่ในบรรทัด while เราสามารถใข้ตัวดำเนินการเปรียบเทียบทางคณิตศาสตร์เลยก็ได้
'''

sum =0
while True:
    number=int(input("ป้อนตัวเลขของคุณ :"))
    sum+=number #บวกเลขที่ป้อนแต่ละรอบ
    if sum>100:
        break
    print("ผลรวม =" ,sum)