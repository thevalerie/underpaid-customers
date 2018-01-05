def find_underpaid_customers(source_file, melon_cost = 1.00):
    """

    - takes a file with customer order data
    - prints the names, amounts paid, and amounts expected for any underpaid customers
    """

    # open the file with customer order data
    order_data = open(source_file)

    # for each customer's data:
    for line in order_data:

        # remove the return at the end of the line
        line = line.rstrip()

        # tokenize the data on the delimeter |
        customer_order = line.split("|")

        # the 1st item is customer name, 2nd is quantity ordered, 3rd is total amount paid
        customer_name = customer_order[1]
        customer_melons = int(customer_order[2])
        customer_paid = float(customer_order[3])
        #print customer_name, customer_melons, customer_paid

        # calculate amount total amount expected
        customer_expected = customer_melons * melon_cost

        # if the amount expected is not what the customer paid, print a statement with the customer name, amount paid, and amount expected
        if customer_expected != customer_paid:
            print customer_name, "paid {:.2f}, expected {:.2f}".format(
                customer_paid, customer_expected)        
    
    # close the file
    order_data.close()


find_underpaid_customers("customer-orders.txt")

