# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name["name"]
    
def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


# def add_or_remove_cash(total_cash, amount):
#     cash = 0
#     cash == total_cash["admin"]["total_cash"] + amount 
#     return cash


# def add_or_remove_cash(total_cash, amount): -10 ## I know this will be the same but subtract as above


def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

# def increase_pets_sold(): ##this will be similar to those above, but calling to increase "pets_sold" rather than "total_cash"
#     return 

def get_stock_count(pet_shop):
    return len(pet_shop["pets"]) 


# def get_pets_by_breed(breed, pet_breed):
#     pet_breed = ["pets"]["breed"] #list indices must be integers or slices, not str 
#     number_of_breed = []
#     for breed in pet_breed:
#         if breed == "British Shorthair":
#             number_of_breed.append(breed) 
#     len(number_of_breed)



# def get_pets_by_breed(breed, pet_shop): dalmation
#     number_of_breed = []
#     for breed in pet_shop:
#         if ["breed"] == "British Shorthair":
#             number_of_breed.append(breed) 
#     return number_of_breed 

# def find_pet_by_name(pet, pet_shop): #I get what I need to do but I really can't figure out how to access the cc_pet_shop (dictionary), "into pets" (list) and then access the dictionary key "name" to see if the value matches Arthur
#     found_pet = None 

#     for pet in pet_shop:
#         if pet("pets"["name"]) == "Arthur":
#             found_pet = pet 
#     return found_pet 

# def find_chicken_by_name(list, chicken_name):
#     found_chicken = None
#     for chicken in list:
#         if chicken ["name"] == chicken_name:
#             found_chicken = chicken 
# 
#     return found_chicken 
# 
# def find_record_by_title (title, record_store):
#     found_record = None #in case nothing is found
# 
#     for record in record_store ["records"]: #for dictionary item in key of dictionary
#         if record["title"] == title: #does the title passing in match dictionary items
#             found_record = record #if true, return it. if not, return None. 
# 
#     return found_record 

def find_pet_by_name (pet, pet_shop):
    pet_name = None 
    for pet in pet_shop["pets"]: #TypeError: string indices must be integers
        if pet["name"] == "Arthur":
            pet_name = pet 
    return pet_name 


def remove_pet_by_name ():
    pass

def add_pet_to_stock():
    pass

def get_customer_cash(customer_cash):
    return customer_cash ["cash"]

def remove_customer_cash(): #similar to total cash manipulation above
    pass 

def get_customer_pet_count():
    pass 

def add_pet_to_customer ():
    pass 

#optional
#ensure code works if elif else 
def customer_can_afford_pet ():
    pass
