import subprocess as sp
import pymysql
import pymysql.cursors


def option1():
    X = int(input("Enter the Minimum Price(in Rs.): "))
    Y=int(input("Enter the Maximum Price(in Rs.): "))

    try:
        query = "SELECT * FROM PRODUCT WHERE PRICE BETWEEN %d AND %d;" % (X, Y)
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")

    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option2():
    X = int(input("Enter Product ID: "))

    try:
        query = "SELECT USER, RATING, DESCRIPTION FROM REVIEW WHERE PRODUCT = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option3():
    X = int(input("Enter User ID: "))

    try:
        query = "SELECT CARTNUMBER, CHECKOUTAMOUNT FROM CART WHERE USER = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option4():
    X = int(input("Enter User ID: "))
    
    try:
        query = "SELECT PRODUCT, RATING, DESCRIPTION FROM REVIEW WHERE USER = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option5():
    X = int(input("Enter Product ID: "))

    try:
        query = """ SELECT W.WAREHOUSE_NUMBER, W.STREET, W.CITY, W.STATE 
                    FROM WAREHOUSE AS W, INSTOCK AS S
                    WHERE W.WAREHOUSE_NUMBER = S.WAREHOUSE
                    AND S.QUANTITY > 0
                    AND S.PRODUCT = %d """ % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option6():
    X = int(input("Enter User ID of the seller: "))

    try:
        query = "SELECT PRODUCT FROM SOLDBY WHERE SELLER = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option7():
    try:
        query = "SELECT PRODUCT, AVG(RATING) AS AVERAGE_REVIEW FROM REVIEW GROUP BY PRODUCT"
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option8():
    X = int(input("Enter Product ID: "))

    try:
        query = "SELECT PRODUCT, MIN(RATING) AS MIN_REVIEW, MAX(RATING) AS MAX_REVIEW FROM REVIEW WHERE PRODUCT = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option9():
    X = int(input("Enter Product ID: "))
    
    try:
        query = "SELECT PRODUCT, SUM(QUANTITY) AS QTY_IN_STOCK FROM INSTOCK WHERE PRODUCT = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option10():
    X = input("Enter the search word: ")

    try:
        query = "SELECT * FROM PRODUCT WHERE PRODUCTNAME LIKE \"%%%s%%\" " % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option11():
    X = input("Enter name of user for search: ")

    try:
        query = "SELECT * FROM USER WHERE FIRSTNAME OR LASTNAME LIKE \"%%%s%%\" " % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option12():
    X = int(input("Enter User ID of Seller: "))

    try:
        query = """ SELECT PRODUCT, AVG(RATING) AS AVG_RATING FROM REVIEW WHERE PRODUCT IN
                    (SELECT PRODUCT FROM SOLDBY WHERE SELLER = %d)
                    GROUP BY PRODUCT""" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option13():
    try:
        query = "SELECT PRODUCT, SUM(PRODUCT) AS QTY_SOLD FROM BUYUSED GROUP BY PRODUCT ORDER BY QTY_SOLD DESC LIMIT 10"
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")

        query = "SELECT PRODUCT, SUM(PRODUCT) AS QTY_SOLD FROM BUYUSED GROUP BY PRODUCT ORDER BY QTY_SOLD DESC LIMIT 10"
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")

    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    
    return


def option14():
    print("Enter user details: ")
    X = (input("Name (firstname lastname): ")).split(' ')
    Y = input("Mobile Number: ")
    Z = input("Email id: ")

    try:
        query = """INSERT INTO USER (FIRSTNAME, LASTNAME, MOBILE, EMAIL) 
                VALUES(\"%s\", \"%s\", \"%s\", \"%s\")""" % (X[0], X[1], Y, Z)
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
        con.commit()
        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def option15():
    X = int(input("Enter User ID: "))
    
    try:
        query = "UPDATE USER SET IS_SELLER = TRUE WHERE USERID = %d" % X
        print(query)
        con.commit()
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
    except Exception as e:
        print("Failed to retrieve data")
        print(">>>>>>>>>>>>>", e)
    return


def option16():
    X = int(input("Enter User ID:"))
    Y = input("Enter new email: ")

    try:
        query = "UPDATE USER SET EMAIL = \"%s\" WHERE USERID = %d" % (Y, X)
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
        con.commit()
        print("Record modified")
    
    except Exception as e:
        con.rollback()
        print("Failed to modify database")
        print(">>>>>>>>>>>>>", e)

    return


def option17():
    X = int(input("Enter Product ID: "))
    Y = int(input("Enter Warehouse number: "))
    Z = int(input("Enter new quantity in-stock: "))

    try:
        query = "UPDATE INSTOCK SET QUANTITY = %d WHERE WAREHOUSE = %d AND PRODUCT = %d" % (Z, Y, X)
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
        con.commit()
        print("Record modified")
    
    except Exception as e:
        con.rollback()
        print("Failed to modify database")
        print(">>>>>>>>>>>>>", e)

    return


def option18():
    X = int(input("Enter Product ID to delete: "))

    try:
        query = "DELETE FROM PRODUCT WHERE PRODUCTID = %d" % X
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
        con.commit()
        print("Record modified")
    
    except Exception as e:
        con.rollback()
        print("Failed to modify database")
        print(">>>>>>>>>>>>>", e)

    return


def option19():
    X = int(input("Enter user id: "))
    Y = int(input("Enter Cart Number: "))

    try:
        query = "DELETE FROM CART WHERE USER = %d AND CARTNUMBER = %d" % (X, Y)
        print(query)
        cur.execute(query)
        retval = cur.fetchall()

        for row in retval:
            for a in row.items():
                print(a[0], end = '')
                print(", ", end = '')
            print("")
            break

        for row in retval:
            for a in row.items():
                print(a[1], end = '')
                print(", ", end = '')
            print("")
        con.commit()
        print("Record modified")
    
    except Exception as e:
        con.rollback()
        print("Failed to modify database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):

    if(ch == 1):
        option1()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    elif(ch == 5):
        option5()
    elif(ch == 6):
        option6()
    elif(ch == 7):
        option7()
    elif(ch == 8):
        option8()
    elif(ch == 9):
        option9()
    elif(ch == 10):
        option10()
    elif(ch == 11):
        option11()
    elif(ch == 12):
        option12()
    elif(ch == 13):
        option13()
    elif(ch == 14):
        option14()
    elif(ch == 15):
        option15()
    elif(ch == 16):
        option16()
    elif(ch == 17):
        option17()
    elif(ch == 18):
        option18()
    elif(ch == 19):
        option19()
    else:
        print("Error: Invalid Option")


while(1):
    tmp = sp.call('clear', shell=True)
    # username = input("Login ID: ")
    # password = input("Password: ")
    
    try:
            # Set db name accordingly which have been create by you
            # Set host to the server's address if you don't want to use local SQL server 
            con = pymysql.connect(host='localhost',
                                port=30306,
                                user="root",
                                password="dna_project",
                                db='dna_project',
                                cursorclass=pymysql.cursors.DictCursor)
            tmp = sp.call('clear', shell=True)

            if(con.open):
                print("Logged In")
            else:
                print("Failed to Log In, Try again")

            tmp = input("Enter any key to CONTINUE>")
            with con.cursor() as cur:
                while(1):
                    tmp = sp.call('clear', shell=True)
                    print("1. Display products in particular price range") 
                    print("2. Display all reviews of a Product")
                    print("3. Display all the carts owned by a user")
                    print("4. Display all reviews by a certain user") 
                    print("5. Display addresses of warehouses having certain product") 
                    print("6. Display ids of all products sold by a particular seller")
                    print("7. Get the average review of every products")
                    print("8. Get the maximum and minimum review of each product")
                    print("9. Get the total quantity of a certain product in stock")
                    print("10. Search for a product by name")
                    print("11. Search for a user by name")
                    print("12. Get the average rating of all products sold by a particular seller")
                    print("13. Get the top 10 most sold products")
                    print("14. Add User")
                    print("15. Add a user as seller")
                    print("16. Modify user email")
                    print("17. Modify quantity in stock of a product")
                    print("18. Delete Product")
                    print("19. Delete cart")
                    print("20. Logout")
                    ch = int(input("Enter choice> "))
                    tmp = sp.call('clear', shell=True)
                    if ch == 20:
                        exit()
                    else:
                        dispatch(ch)
                        tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
            tmp = sp.call('clear', shell=True)
            print(e)
            print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
            tmp = input("Enter any key to CONTINUE>")
