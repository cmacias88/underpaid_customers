# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

def customer_expected(path):

    """Gives the expected cost of the melons and only shows if there is a discrepancy in the expected cost."""

    customer_log = open(path) 

    for line in customer_log:
        line = line.rstrip() 
        customer_info = line.split('|')
        customer_number, name, melons, money_paid = customer_info

        melon_cost = 1.00
        
        melons = int(melons)
        money_paid = float(money_paid)

        expected_cost = melons * melon_cost

        if expected_cost != money_paid:
            print()
            print(f"Customer {customer_number}, {name} paid ${money_paid:.2f},",
            f"expected ${expected_cost:.2f}"
            )
        else: 
            print()
            print(f"Customer {customer_number}, {name} paid the adequate amount.")

customer_expected("customer-orders.txt")
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
