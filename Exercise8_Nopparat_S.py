userID = input("Username :")
userPassword = input("Password : ")

if userID == "admin" and userPassword == "1234" :
    print("Wellcome to Our Shop")
    print("Product list")
    print("1. apple : 30 thb. ")
    print("2. orange : 25 thb. ")
    print("3. coconut : 40 thb. ")
    userSelected = int(input("เลือกสินค้า (หมายเลข) >> "))
    if userSelected == 1:
        item_01 = int(input("apple จำนวน : "))
        total_price = item_01 * 30
        print("ยอดรวมทั้งหมด" + str(total_price) + "บาท")
    elif userSelected == 2:
        item_02 = int(input("orange จำนวน : "))
        total_price = item_02 * 25
        print("ยอดรวมทั้งหมด" + str(total_price) + "บาท")
    elif userSelected == 3:
        item_03 = int(input("coconut จำนวน : "))
        total_price = item_03 * 40
        print("ยอดรวมทั้งหมด" + str(total_price) + "บาท")
else :
        print("ยังไม่มีการสั่งซื้อ")