def categoryTemp():
    cat = []
    fCat = open("source/products/category.txt", 'w')
    catRep = '1'
    while cat == '' or catRep == '1':
        userCat = str(input(" \t \tEnter a category: "))
        catRep = str(input("Do you want to enter the category again (1 for yess/ 0 for no): "))
        if catRep != '0' and catRep != '1':
            print("Invalid input!")
            catRep = '1'
        if catRep == '0':
            print()
            print("-" * 184)
    for i in range(0, len(cat)):
        fCat.write(cat[i] + '\n')
def addcategories(inp):
    fCat = open("source/products/category.txt", 'r')
    catlist = []
    for i in fCat:
        catlist.append(i)
    catlist.append(inp)
    fCat.close()
    fCat = open("source/products/category.txt", 'w')
    for i in range(0, len(catlist)):
        fCat.write(catlist[i] + '\n')

    fCat.close()

def showcategory():
    fCat = open("source/products/category.txt", 'r')
    catlist = []
    dumyvar = ''
    for i in fCat:
        catlist.append(i)
    for i in range(0, len(catlist)):
        print("Categories: ")
        print(i,":", catlist[i])
    fCat.close()



def showProducts():
    fPrice = open("source/products/products_prices.txt", 'r')
    fName = open("source/products/raw_products.txt", 'r')
    fQuantities = open("source/products/products_quantities.txt", 'r')
    fCat = open("source/products/category.txt", 'r')
    print("-" * 184)
    print("\t\t\t\t\t\t\tPRODUCTS DETAILS")
    nameTemp =[]
    priceTemp = []
    quantityTemp = []
    catlist = []
    for i in fName:
        nameTemp.append(i)
    for i in fPrice:
        priceTemp.append(i)
    for i in fQuantities:
        quantityTemp.append(i)
    for i in fCat:
        catlist.append(i)
    for i in range(0, len(nameTemp)):
        print()
        print("\t \tKey ", i,":", end='')
        print("PRODUCT NAME: ", nameTemp[i], end="")
        print("\t\t \tPRODUCT PRICE: Rs: ", priceTemp[i], end="")
        print("\t\t \tPRODUCT QUANTITY: ", quantityTemp[i], end="")
        print("\t\t \tCATEGORY: ", catlist[i])
        print("\t", end='')
        print(" - " * 44)
    print()
    if len(nameTemp) == 0:
        print("\t\t\t\t\t\t\t NONE!")
    print("-" * 184)
    print()
    fCat.close()
    fName.close()
    fQuantities.close()
    fPrice.close()

def addProducts():
    fPrice = open("source/products/products_prices.txt", 'r')
    fName = open("source/products/raw_products.txt", 'r')
    fQuantities = open("source/products/products_quantities.txt", 'r')
    fCat = open("source/products/category.txt", 'r')

    catlist = []
    nameTemp = []
    priceTemp = []
    quantityTemp = []
    dumyvar = 0

    for i in fName:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        nameTemp.append(dumyvar)
    for i in fPrice:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        priceTemp.append(dumyvar)
    for i in fQuantities:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]
        quantityTemp.append(dumyvar)
    for i in fCat:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]
        catlist.append(dumyvar)


    print("-" * 184)
    print()

    print(" \t \tFill the following blacks to enter the New products, its prices and Quantities!")
    print()

    name = ''
    price = ''
    quantities = ''
    while name == '' or price =='' or quantities =='':

        name = str(input("\t Enter the name of the product: "))
        price = str(input("\t Enter the price of the product: "))
        quantities = str(input("\t Enter the quantity of the product: "))
        category = str(input("\t Enter the category of the product: "))
        if name == '' or price =='' or quantities =='' or category == '':
            print()
            print("\t No field should be empty!!")
            print()

    nameTemp.append(name)
    priceTemp.append(price)
    quantityTemp.append(quantities)
    addcategories(category)
    fName.close()
    fPrice.close()
    fQuantities.close()
    fPrice = open("source/products/products_prices.txt", 'w')
    fName = open("source/products/raw_products.txt", 'w')
    fQuantities = open("source/products/products_quantities.txt", 'w')

    for i in range(0, len(nameTemp)):
        fName.write(nameTemp[i] + '\n')
    for i in range(0, len(priceTemp)):
        fPrice.write(priceTemp[i] + '\n')
    for i in range(0, len(quantityTemp)):
        fQuantities.write(quantityTemp[i] + '\n')

    fName.close()
    fPrice.close()
    fQuantities.close()

    print()
    print("-" * 184)


def removeProduct():

    showProducts()

    fPrice = open("source/products/products_prices.txt", 'r')
    fName = open("source/products/raw_products.txt", 'r')
    fQuantities = open("source/products/products_quantities.txt", 'r')

    productName = []
    productPrice = []
    productQuantity = []
    dumyvar = 0
    for i in fName:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productName.append(dumyvar)
    for i in fPrice:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productPrice.append(dumyvar)
    for i in fQuantities:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productQuantity.append(dumyvar)

    fPrice.close()
    fQuantities.close()
    fName.close()

    key = int(input("Enter the product key to remove that product: "))
    del productName[key]
    del productPrice[key]
    del productQuantity[key]

    fPrice = open("source/products/products_prices.txt", 'w')
    fName = open("source/products/raw_products.txt", 'w')
    fQuantities = open("source/products/products_quantities.txt", 'w')

    for i in range(0, len(productName)):
        fName.write(productName[i]+ '\n')
    for i in range(0, len(productPrice)):
        fPrice.write(productPrice[i] + '\n')
    for i in range(0, len(productQuantity)):
        fQuantities.write(productQuantity[i] + '\n')
    fName.close()
    fPrice.close()
    fQuantities.close()


def cheakOutHistory():
    print("-" * 184)
    print()
    print("\t\t\t\t\t\t CheckOut history")
    print()

    f = open('source/Cheackout_history.txt', 'r')
    for i in f:
        print("\t\t",i)
    f.close()
    print()
    print("-" * 184)



def adminBlock():
    print("-" * 184)
    print("\t \t \t \t \t\tAdmin block!")
    print("\t \t \t \t \ta: Show products")
    print("\t \t \t \t \tb: Add products")
    print("\t \t \t \t \tc: Remove products")
    print("\t \t \t \t \td: Show CheckOut History")
    print("\t \t \t \t \te: Add categories")
    print("\t \t \t \t \tf: show categories")
    print("\t \t \t \t \t0: Exit Admin Menu")

    adminMenuOptions = '1'
    adminMenuOptionsRep = '1'

    while adminMenuOptions == '1':
        adminMenuOptions = str(input("\t \t \t \t \tPlease one of the above options Correctly: "))
        while adminMenuOptionsRep == '1' and adminMenuOptions != '0':

            if adminMenuOptions == 'a' or adminMenuOptions =='A' or adminMenuOptions == 'b' or adminMenuOptions == 'B' or adminMenuOptions == 'c' or adminMenuOptions == 'C' or adminMenuOptions == 'd' or adminMenuOptions == 'D':
                print("\t \t \t \t \tValid input!")

            else:
                print("\t \t \t \t \tINVALID INPUT ", end="")
                print('\u274C')

            if adminMenuOptions == 'a' or adminMenuOptions == 'A':
                showProducts()
            elif adminMenuOptions == 'b' or adminMenuOptions == 'B':
                addProducts()
            elif adminMenuOptions == 'c' or adminMenuOptions == 'C':
                removeProduct()
            elif adminMenuOptions == 'd' or adminMenuOptions == 'D':
                cheakOutHistory()
            elif adminMenuOptions == 'e' or adminMenuOptions == 'E':
                categoryTemp()
            elif adminMenuOptions == 'f' or adminMenuOptions == 'F':
                showcategory()

            adminMenuOptionsRep = str(input("\t \t \t \t \tDo you want to perform one of the above options again (1 for yess/ 0 fro No): "))
            if adminMenuOptionsRep == '1':
                adminMenuOptions = str(input("\t \t \t \t \tPlease one of the above options Correctly: "))
            elif adminMenuOptionsRep == '0':
                adminMenuOptions = '0'

def adminCheak():
    print("-" * 184)
    f = open("source/passward.txt", 'r')
    passward = f.read()
    user_passward = ""
    admin_rep = 1

    while admin_rep == 1:
        user_passward = str(input("\t \t \t \t \tPlease enter the admin passward: "))
        if user_passward == passward:
            print("\t \t \t \t \tCorrect passward!", end='')
            print(u' \N{check mark}')
            admin_rep = 0
        elif user_passward != passward:
            print("\t \t \t \t \tWrong Passward!",end="")
            print('\u274C')
            admin_rep = int(input("\t \t \t \t \tDo you want to enter passward again (1 for yes/0 for false): "))
    f.close()
    if user_passward == passward:
        adminBlock()
        return True



def checkOut(h,m, UserName):
    fPrice = open("source/products/products_prices.txt", 'r')
    fName = open("source/products/raw_products.txt", 'r')
    fQuantities = open("source/products/products_quantities.txt", 'r')

    productName = []
    productPrice = []
    productQuantity = []

    for i in fName:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productName.append(dumyvar)
    for i in fPrice:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productPrice.append(dumyvar)
    for i in fQuantities:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productQuantity.append(dumyvar)
    nameOfproduct = []
    priceOfproduct = []
    quantityOfproduct = []
    name = []
    price = ''
    TotalBill = 0
    for i in range(0, len(h)):
        nameOfproduct.append(int(h[i]))
    for i in range(0, len(m)):
        quantityOfproduct.append(int(m[i]))
    for i in range(0, len(nameOfproduct)):
        priceOfproduct.append(nameOfproduct[i])


    for i in range(0, len(nameOfproduct)):
        name.append(productName[nameOfproduct[i]])


    print("-" * 184)

    print("\t\t\t\t\t\t\t\t\tCheckOut details")
    print()
    for i in range(0, len(nameOfproduct)):
        price = priceOfproduct[i]
        TotalBill = TotalBill + (int(productPrice[price]) * quantityOfproduct[i])
        print("\t\t\t\t",i,': ', end="")
        print("\tProduct name: "+name[i])

        print("\t\t\t\t\tProduct Price Each: " + (productPrice[price]) + ' Rs')
        print("\t\t\t\t\tQuantity of product: " + str(quantityOfproduct[i]))
        print("\t\t\t", end="")
        print(" - " * 44)
        print()

    fPrice.close()
    fQuantities.close()
    fName.close()

    print("\t \t \t \t \t \t Dear Mr/Ms " + UserName)
    print()
    print("\t \t \t \t \t \tYour total bill is: ", TotalBill, " Rs")
    print("\t \t \t \t \t \tKindly pay it, at the counter!")

    f = open("source/cheackout_history.txt", "a")
    f.write("Name: "+ UserName + " Bill: "+ str(TotalBill) + '\n')
    f.close()
    print()
    print("-" * 368)

def userBlock():
    fPrice = open("source/products/products_prices.txt", 'r')
    fName = open("source/products/raw_products.txt", 'r')
    fQuantities = open("source/products/products_quantities.txt", 'r')

    productName = []
    productPrice = []
    productQuantity = []
    for i in fName:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productName.append(dumyvar)
    for i in fPrice:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]

        productPrice.append(dumyvar)
    for i in fQuantities:
        for j in (0, len(i) - 1):
            if i[j] == '\n':
                dumyvar = i[:j]
    print("-" * 184)
    print()

    print("\t \t \tYou have entered into the user block!")
    print("\t \t \tPlease be kind enough to enter the following things:")
    print()
    userName = ''
    userCellNo = ''
    while userName == '' or userCellNo == '':
        userName = str(input("\t\tName (Mandatory):"))
        userCellNo = str(input("\t\tCell phone (Mandatory):"))
        if userName == '' or userCellNo == '':
            print("\tBoth of above fields should not be empty!", end='')
            print('\u274C')
    userEmail = str(input("\t\tEmail (Temporary):"))

    userfile = 'source/users/'+userName+'_'+userCellNo+'_'+'.txt'
    f = open(userfile, 'w+')

    showProducts()
    print()
    itemsPurchased = []
    itemsQuantity = []
    productVeriRep = '1'

    print()
    print("Please give the info about the product you want to purchase!")
    print()

    while itemsPurchased == [] or itemsQuantity == [] or productVeriRep == '1':

        productKey = ''
        productQuanti = ''
        while productQuanti == '' or productKey == '':
            productKey = str(input("\tKey of the product: "))
            productQuanti = str(input("\tQuantity of the product: "))
            if productQuanti == '' or productKey == '':
                print()
                print("\tAbove fields can not be empty!!", end='')
                print('\u274C')
                print()
            if int(productKey) > len(productName)-1:
                print("\tOUT OF PRODUCTS!", end='')
                print('\u274C')
                productVeriRep = '1'
            else:
                itemsPurchased.append(productKey)
                itemsQuantity.append(productQuanti)
                productVeriRep = str(input("\tDo you want to enter another product again (1 for yes/ 0 for no): "))

        print()

        if productVeriRep != '0' and productVeriRep != '1':
            productVeriRep = '1'
            print("\tInvalid input!",end='')
            print('\u274C')

    f.write(userName + "\n")
    f.write(userCellNo + "\n")
    f.write(userEmail + "\n")
    f.close()
    checkOut(itemsPurchased, itemsQuantity, userName)

print()
print()

print("-"*368)

print()
print()
print()
print("\t \t \t \t \t******** WELCOME TO THE UTILITY MANAGEMENT SYSTEM ********")
print()
print("\t \t \t \t \tIN THIS PROGRAM YOU ARE REQUIRED TO ENTER SOME INFORMATION")
print("\t \t \t \t \tOF YOURS. BASE THAT IT WILL BE DETERMINED WEATHER YOU ARE \n\t \t \t \t \tTHE USER OR ADMIN")
print()
print()
print("\t \t \t \t \tPLEASE TELL US WHO YOU ARE!")
print("\t \t \t \t \tENTER ONE  THE FOLLOWING OPTIONS:")
print()

dum = 0
while dum == 0 or dum == 1 or dum == 2:
    dum = '1'
    while dum != '3':
        print(" - " * 60)
        print()
        print("\t \t \t \t \t \t \t**MAIN MENU**")
        print()
        print("\t \t \t \t \t \t \t1: ADMIN")
        print("\t \t \t \t \t \t \t2: USER")
        print("\t \t \t \t \t \t \t3: EXIT")

        print()
        print("\t \t \t \t \t \t    ", end="")

        dum = str(input("Enter: "))
        if dum == '1' or dum == '2' or dum == '3':
            print()
        else:
            print()
            print("\t \t \t \t \t \t INVALID INPUT!", end="")
            print('\u274C')
        if dum == '1':
            adminCheak()
        elif dum == '2':
            userBlock()
        if dum != '1':
            if dum != '2':
                dum = '3'

    print("-" * 184)

print()
print("\t\t\t\t\tThe Project has been created with Great effort!")
print("\t\t\t\t\t***********************************************")
print("\t\t\t\t\t\tAUTHERS: Muneeb ur rehman")
print("\t\t\t\t\t\t         Jahangir Ahmad")
print("\t\t\t\t\t\t         Samran Ahmad")
print("\t\t\t\t\t\t         Muhammad Arsalan")
print()

print("-"*368)
