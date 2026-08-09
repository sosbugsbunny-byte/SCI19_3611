fruitPrices = {'apples': 2.00, 'oranges': 1.50, 'pears': 1.75}

def buyFruit(fruit, numPounds):
    if fruit not in fruitPrices:
        print("Sorry we don't have %s - fruit.py:5" % (fruit))
        return
    else:
        cost = fruitPrices[fruit] * numPounds #numPounds คือ ราคาที่ซื้อ
        print("That'll be %f please - fruit.py:9" % (cost))
        totalMoney = 0
        totalMoney += cost
        return totalMoney

# Main Function
if __name__ == '__main__':
    buyFruit('apples', 2.4)
    buyFruit('coconuts', 2) 
    buyFruit('oranges', 1.5)
    buyFruit('pears', 3)
    buyFruit('pears', 5)

#เรียก 'buyFruit' เพิ่ม 2 เคส (มี/ไม่มีสินค้า)
#ปรัับฟังชันให้ return cost ถ้ามีสินค้า
#พิมพ์ Total = ... จากค่าที่คืนมา