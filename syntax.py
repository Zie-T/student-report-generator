#def say_hello():
#    return "Hello"

#message = say_hello()
#print(message)

#def add_numbers(a, b):
#    return a + b

#results = add_numbers(3, 7)
#print(results)

#def check_pass(score):
 #   if score >= 50:
 #       return "Pass"
  #  else:
 #       return "Fail"

#results = check_pass(78)
#print(results)

#def big_or_small(number):
#   if number > 10:
 #       return "Big" 
#    else:
#        return "Small"

#print(big_or_small(20))

# ex 2

#def square_number(number):
#    return number **2

#ex 3
#def no_negatives(number):
#    if number <0:
 #       return 0
  #  else:
 #       return number

#print (no_negatives(4))

#ex 4 correction

#def max_number(a, b):
 #   if a > b:
 #       return a
#    else:
 #       return b

 #ex 5

#def sum_positives(numbers):
    #total = 0
    #for num in numbers:
        #if num > 0:
            #total += num
    #return tota


#def count_positives(numbers):
 #   count = 0
 #   for num in numbers:
 #       if num > 0:
 #           count += 1
 #   return count

#def count_evens(numbers): 
   # counter = 0
 #   for num in numbers:
 #       if num % 2 == 0 :
 #           counter += 1
 #   return counter

#def clean_sale(amount):
    
#    if amount < 0:
 #       return  0
#    else :
 #       return amount

#def apply_discount(amount):
#    if amount >= 100:
#        return amount -10
#    else :
#        return amount

#def process_sales(sales):
#    discounted_sales = 0
#    total_sales = 0
 #   for sale in sales :
 #       clean_amount = clean_sale(sale)

#        if clean_amount >= 100:
#            discounted_sales += 1

 #       final_amount = apply_discount(clean_amount)
 #       total_sales += final_amount

 #   return total_sales, discounted_sales

#sales = [120, 500, -50, 80, -6, 90]

#totals, discounts = process_sales(sales)

#print(totals)
#print(discounts)

#def count_large(numbers):
 #   count = 0
 #   for num in numbers:
 #       if num < 0:
 #           continue
 #       if num > 100:
 #           count += 1
 #   return count
 
 #DAY 4 OF PYTHON WITH GPT

#def sum_large(numbers):
 #   total = 0
#    for num in numbers:
#        if num < 0:
 #           continue
#        if num > 100:
#            total += num
#    return total   

#def count_range(numbers):
#    total = 0
 #   for num in numbers:
#        if num < 0:
#            continue
#        if num > 50 and num <= 150:
 #           total += 1
#    return total

#def count_even_mid(numbers):
 #   total = 0
 #   for num in numbers:
 #       if num < 0:
#            continue
#        if 200 <= num <= 500:
#            if num % 2 == 0:
 #               total += 1
 #   return total

 #USING AND DAY 5 OF SHOWING UP
#def count_valid(numbers):
 #   total = 0
 #   for num in numbers:
 #       if num < 0:
 #           continue
 #       if 50 <= num <= 150 and num % 2 == 0:
 #           total += 1
 #   return total

#USING OR
#def count_outside(numbers):
 #   total = 0
 #   for num in numbers:
 #       if num < 0:
 #           continue
 #       if num < 50 or num > 150:
 #           total += 1
 #   return total

#USING NOT
#def count_not_even(numbers):
 #   total = 0
 #   for num in numbers:
 #       if num < 0:
 #           continue
 #       if  50<= num <= 150 and not (num % 2 == 0):
 #           total += 1
 #   return total

#TYPE CONVERSION
#def check_number(): 
#    lucky_number = (int(input("Enter your lucky number.: ")))
 #   if lucky_number < 0 :
#        return 'Negative'
#    elif lucky_number % 2 == 0:
#        return 'Even'
#    else:
#        return 'Odd'

#DAY 6 PYTHON PROGRAMMMING Practisee

#def check_price():
#    price = float(input("Enter your price.: "))
#if price < 0 :
 #       return "Invalid"
 #   elif price <= 10:
 #       return "Cheap"
#elif price < 100:
#return "Moderate"
 #   else:
 #       return "Expensive"
#check = check_price()
#(check)

#Falsey /Truthy
#def check_list(numbers):
 #   if not numbers:
#        return "empty"
3#else:
 #       return "has data"

#booleaan
#def is_provided(text):
#    return bool(text)



