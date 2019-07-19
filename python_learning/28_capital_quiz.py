import sys
print sys.getdefaultencoding()

import random

capitals_dict={
"Andaman and Nicobar Islands":"Port Blair",
"Andhra Pradesh":"Hyderabad ",
"Arunachal Pradesh":"Itanagar",
"Assam":"Dispur",
"Bihar":"Patna",
"Chandigarh":"Chandigarh",
"Chattisgarh":"Raipur",
"Dadra and Nagar Haveli ":"Silvassa",
"Daman and Diu ":"Daman",
"National Capital Territory of Delhi ":"New Delhi",
"Goa":"Panaji",
"Gujarat":"Gandhinagar",
"Haryana":"Chandigarh",
"Himachal Pradesh":"Shimla",
"Jammu and Kashmir":"Srinagar ",
"Jharkhand":"Ranchi",
"Karnataka":"Bengaluru",
"Kerala":"Thiruvananthapuram",
"Lakshadweep ":"Kavaratti",
"Madhya Pradesh":"Bhopal",
"Maharashtra":"Mumbai",
"Manipur":"Imphal",
"Meghalaya":"Shillong",
"Mizoram":"Aizawl",
"Nagaland":"Kohima",
"Odisha":"Bhubaneswar",
"Puducherry ":"Puducherry",
"Punjab":"Chandigarh",
"Rajasthan":"Jaipur",
"Sikkim":"Gangtok",
"Tamil Nadu":"Chennai",
"Telangana":"Hyderabad",
"Tripura":"Agartala",
"Uttar Pradesh":"Lucknow",
"Uttarakhand":"Dehradun",
"West Bengal":"Kolkata"
}

states = list(capitals_dict.keys())
for i in [1,2,3,4,5]:
    state = random.choice(states)
    capital = capitals_dict[state]
    capital_guess = str(raw_input("What is the capital of " + state +" ? "))

    if capital_guess == capital :
        print("Correct")
    else:
       print("Incorrect. The capital of " + state + " is " + capital + ".")

print ("All Done")


