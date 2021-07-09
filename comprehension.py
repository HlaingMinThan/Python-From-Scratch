# prices = [2000,1000,3000,5000]

# double_prices=[];
# for price in prices:
#     double_prices.append(price*2)

# print(double_prices);

# double_prices=[price*2 for price in prices ]
# print(double_prices);

nums=[1,2,3,4,5,6,7,8,9,10]
# even_double_nums=[]
# for num in nums:
#     if (num%2)==0 :
#        even_double_nums.append(num*2)

# print(even_double_nums);

even_double_nums=[num*2 for num in nums if (num%2)==0]
print(even_double_nums);
