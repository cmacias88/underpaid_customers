# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

customer_1 = ["Joe", "5", "5.00"]

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

customer_2 = ["Frank", "6", "6.00"]

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

customer_3 = ["Sally", "3", "3.00"]

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

customer_4 = ["Sean", "9", "9.50"]

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

customer_5 = ["David", "4", "4.00"]

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

customer_6 = ["Ashley", "3", "2.00"]

customer_list = [customer_1, customer_2, customer_3, customer_4, customer_5, customer_6]

def customer_expected(list):
    """Gives the expected cost of the melons and only shows if there is a discrepancy in the expected cost."""

    melon_cost = 1.00
    
    for customer in list: 

        name, melons, money_paid = customer 
        
        melons = int(melons)
        money_paid = float(money_paid)

        expected_cost = melons * melon_cost

        if expected_cost != money_paid:
            print()
            print(f"{name} paid ${money_paid:.2f},",
            f"expected ${expected_cost:.2f}"
            )
        else: 
            print()
            print(f"{name} paid the adequate amount.")

customer_expected(customer_list)
# customer_expected(customer_2)
# customer_expected(customer_3)
# customer_expected(customer_4)
# customer_expected(customer_5)
# customer_expected(customer_6)

# The previous code:

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
