from random import randint
welcome_banner = """Welcome to the Random Username Generator! Answer the propmts to generate your random username."""
print(welcome_banner)
first_name = input("Your first name:")
last_name = input("Your last name:")
favorite_pet_name = input("Your favorite pet name:")
favorite_food = input("Your favorite food:")
random_number = randint(0,4)
if random_number == 0:
    band_name = (f"{first_name} and the {last_name}")
    
elif random_number==1:
    band_name = (f"{favorite_pet_name} and the {favorite_food}")

elif random_number==2:
    print(f"Your Random Username is {first_name}{last_name}_7361")
    
elif random_number==3:
    print(f"Your OTHER username is {favorite_pet_name}{last_name}_9184")
    
elif random_number==4:
    print(f"Your OTHER username is {random_number}_5904")
