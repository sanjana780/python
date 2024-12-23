#wap to calculate on purchasing movie ticket(payable_amount, discount,total_amount)
no_of_ticket = int(input("enter the number of ticket purchased"))
discount_price=7
per_price_ticket=120

#calculate total amount
total_amount = no_of_ticket*per_price_ticket

#discount value
discount_price = (total_amount*discount_price)/100

payble_amount = total_amount-discount_price;

print("no of ticket is",no_of_ticket)
print("price of per tickets is",per_price_ticket)
print("total amount of tickets are",total_amount)
print("discount on tickets are",discount_price)
print("payble amount on ticket are",payble_amount)