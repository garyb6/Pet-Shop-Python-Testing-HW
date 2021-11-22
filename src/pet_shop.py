# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_name):
    return shop_name["name"]
    
def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount 

def get_pets_sold(pets_sold):
    return pets_sold["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, amount): ##this will be similar to those above, but calling to increase "pets_sold" rather than "total_cash"
    pet_shop["admin"]["pets_sold"] += amount

def get_stock_count(pet_shop):
    return len(pet_shop["pets"]) 

def get_pets_by_breed(pet_shop, pet_breed): 
    found_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            found_pets.append(pet) 
    return found_pets

# def get_pets_by_breed(pet_shop, pet_breed): 
#     number_of_breed = 0
#     for pet in pet_shop["pets"]:
#         if pet["breed"] == pet_breed:
#             number_of_breed += 1
#     return number_of_breed


def find_pet_by_name(pet_shop, pet_name):
    found_pet = None 
    for pet in pet_shop["pets"]: #accessing the dictionary and then the list within the dictionary - for examnple cc_pet_shop (dict) "pets" (list)
        if pet["name"] == pet_name:
            found_pet = pet 
    return found_pet 


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
