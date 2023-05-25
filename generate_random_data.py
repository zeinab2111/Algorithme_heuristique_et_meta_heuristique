import random
all_ingredients=["fromage","tomates","poivrons","oignons","champignons","olives","épinards","artichauts","courgettes","aubergines",
                      "maïs","jambon","bacon","l'origan","thym","romarin","basilic","saucisses","poulet","boeuf"]
nb_clients=1000
with open ('random_data_in.txt', 'w') as file:
    file.write(str(nb_clients)+"\n")
    for i in range(nb_clients):
        random_number_like_ingredients = random.randint(1, 5)
        file.write(str(random_number_like_ingredients)+" ")
        like_list=[]
        unlike_list=[]
        for j in range(random_number_like_ingredients):
            like_ingredient=random.choice(all_ingredients)
            while like_ingredient in like_list:
                like_ingredient = random.choice(all_ingredients)
            like_list.append(like_ingredient)
            file.write(str(like_ingredient)+" ")
        print(random_number_like_ingredients, like_list)
        file.write("\n")

        random_number_unlike_ingredients = random.randint(0, 5)
        file.write(str(random_number_unlike_ingredients) + " ")
        for k in range(random_number_unlike_ingredients):
            unlike_ingredient=random.choice(all_ingredients)
            while unlike_ingredient in like_list or unlike_ingredient in unlike_list:
                unlike_ingredient = random.choice(all_ingredients)
            unlike_list.append(unlike_ingredient)
            file.write(str(unlike_ingredient) + " ")
        print(random_number_unlike_ingredients, unlike_list)
        file.write("\n")


