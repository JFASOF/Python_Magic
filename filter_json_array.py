import json , requests

url = 'https://api.slingacademy.com/v1/sample-data/files/customers.json'
response = requests.get(url)
data = response.json()

json_array = json.dumps(data)
customer_list = json.loads(json_array)
#print(customer_list)

#Use a list comprehension to filter the list.
filtered_cus_list =[d for d in customer_list
                    if  20<d['age'] < 23 
]
print(filtered_cus_list)
print("-----------------------------------------------------------------------------------------------------------------")

"""
Other Example
filtered_list = []

for dictionary in customer_list:
    if dictionary['salary'] > 50:
        filtered_list.append(dictionary)
"""


filtered_cus_list_oth = list(filter(lambda dictionary: dictionary['orders'] < 5,
        customer_list))
print(filtered_cus_list_oth)




"""
json_array = json.dumps([{
        {'name': 'Ali', 'salary': 100},
        {'name': 'Bobby', 'salary': 50},
        {'name': 'Carl', 'salary': 75}
}])
"""