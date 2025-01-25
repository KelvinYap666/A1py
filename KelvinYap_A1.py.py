#Name: KelvinYap
#UOW Student number:8750762
#Tutorial group 04F
#Declaration: This is my own program and I have not passed my program to anyone in this class.
#demo not shown as assignment deadline is 16jan next tutorial is 19jan

#print company name
print("Welcome to KelvinYap company\n__________________________")
#user input item to be sold
print("Enter 3 items to be sold:")
item_1=str(input("1. "))
item_2=str(input("2. "))
item_3=str(input("3. "))

#enter quantities and costs
print("Enter each item information\n____________________________")

#item 1
quantity1=int(input("\nEnter quantity for {0} : ".format(item_1)))
unitprice1=float(input("Enter unit price for {0} : ".format(item_1)))
#item 2
quantity2=int(input("\nEnter quantity for {0} : ".format(item_2)))
unitprice2=float(input("Enter unit price for {0} : ".format(item_2)))
#item 3
quantity3=int(input("\nEnter quantity for {0} : ".format(item_3)))
unitprice3=float(input("Enter unit price for {0} : ".format(item_3)))

#swapping item 1 with item 2
item_2,item_1=item_1,item_2
quantity2,quantity1=quantity1,quantity2
unitprice2,unitprice1=unitprice1,unitprice2

#print summary table
print("\nSummary of item\n_________________")
print("\n{2:<15}{0:^18}{1:>15}".format("Quantity","Unit Price","Item"))
print("================================================")
print("{0:<15}{1:^18}{2:>15}".format(item_1,quantity1,unitprice1))
print("{0:<15}{1:^18}{2:>15}".format(item_2,quantity2,unitprice2))
print("{0:<15}{1:^18}{2:>15}".format(item_3,quantity3,unitprice3))

#print delivery info
print("\nEnter delivery information")
print("___________________________")
cust_name=str(input("Enter customer name: "))
cust_collection=str(input("Enter collection point: "))

#input print order
print("Please place your order")
print("_______________________")
order1=int((input("No of {0} : ".format(item_1))))
order2=int((input("No of {0} : ".format(item_2))))
order3=int((input("No of {0} : ".format(item_3))))

#immediately print order
print("Summary of order")
print("________________")
print("\n{2:<15}{0:^20}{1:>13}".format("Quantity","Cost Price","Item"))
print("================================================")
print("{0:<15}{1:^20}{2:>13}".format(item_1,order1,unitprice1*float(order1)))
print("{0:<15}{1:^20}{2:>13}".format(item_2,order2,unitprice2*float(order2)))
print("{0:<15}{1:^20}{2:>13}".format(item_3,order3,unitprice3*float(order3)))
print("================================================")
add_price=(unitprice1*float(order1)+(unitprice2*float(order2)+(unitprice3*float(order3))))
gst=round(add_price*0.08,2)
total_price=add_price+gst
print("{1:<15}{0:>33}".format(add_price,"Subtotal"))
print("{1:<15}{0:>33}".format(float(gst),"8.0(%)"))
print("{1:<15}{0:>33}".format(total_price,"Total cost"))
print("================================================")

#print some important delivery note
print("Some important notes for delivery")
print("__________________________________")
print("\nCustomer name: {0}".format(cust_name))
print("Collection point: {0}".format(cust_collection))
print("Note that payment by cash upon delivery\nThank you for using our system")

#print the remaining stock
left_quant1=(quantity1)-(int(order1))
left_quant2=(quantity2)-(int(order2))
left_quant3=(quantity3)-(int(order3))
print("\nBalance report")
print("_______________")
print("{3:<15}{0:<12}{1:^22}{2:>4}".format("Quantity","Sold","Balance","\nItem"))
print("=======================================================")
print("{0:<15}{1:<12}{2:^22}{3:>4}".format(item_1,quantity1,order1,left_quant1))
print("{0:<15}{1:<12}{2:^22}{3:>4}".format(item_2,quantity2,order2,left_quant2))
print("{0:<15}{1:<12}{2:^22}{3:>4}".format(item_3,quantity3,order3,left_quant3))
print("=======================================================")


#input enter to terminate program
input("press enter to terminate")
