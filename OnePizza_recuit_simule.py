import random
import math
import matplotlib.pyplot as plt

def data():
    with open("random_data_in.txt", "r") as f:
        like_client={}
        unlike_client={}
        list_all=[]
        next(f)
        for line in f:
            l = line.split()
            list_all.append(l[1:])
        for i in range(0,len(list_all)-1,2):
            j=i+1
            like_client[int(i/2)]=list_all[i]
            unlike_client[int(i/2)]=list_all[j]
        like={}
        for k in range(len(like_client)):
            for ingredient in like_client[k]:
                if ingredient in like:
                    like[ingredient]+=1
                else:
                    like[ingredient] = 1
        return list_all, like_client, unlike_client, like
#une fonction du cout:
def calculate_score(nb_clients,like_client, unlike_client, list_ingredients):
    score = 0
    for j in range(nb_clients):
        my_ing = 0
        for ing in like_client[j]:
            if ing in list_ingredients:
                my_ing += 1
        if my_ing == len(like_client[j]):
            not_my_ing = 0
            for ingr in unlike_client[j]:
                if ingr in list_ingredients:
                    not_my_ing += 1
            if not_my_ing == 0:
                score += 1
    return score

def change_ingredients(list_ingredients, like, nb_ingredients):
    #un ingredient random de ma liste solution
    random_ingredient = random.choice(list_ingredients)
    #un ingredient random de la liste like
    random_like = random.choice(like)
    while random_like in list_ingredients:
        random_like = random.choice(like)
    #delete
    nn_boucle = len(list_ingredients)//3
    random_choice = random.randint(1, 3)
    if random_choice == 1:
        if len(list_ingredients) > 1:
            list_ingredients.remove(random_ingredient)
        else:
            random_choice = random.randint(1, 3)
    #ajout
    if random_choice == 2:
        if len(list_ingredients) < nb_ingredients:
             list_ingredients.append(random_like)

        else:
         random_choice = random.randint(1, 3)
    #remplacement
    if random_choice == 3:
        list_ingredients.remove(random_ingredient)
        list_ingredients.append(random_like)
    return list_ingredients
#nb_ingredients <=10
def initial_solution(nb_ingredients, like):
    initial_sol = []
    for i in range(nb_ingredients):
        random_like = random.choice(like)
        while random_like in initial_sol:
            random_like = random.choice(like)
        initial_sol.append(random_like)
    return initial_sol

def recuit_simule(nb_ingredients):
    random.seed(1)
    #temperature initiale:
    Temp_initial = 1000
    #taux de referoidissement:
    taux_ref = 0.99
    temp = Temp_initial
    _, like_client, unlike_client, like = data()
    nb_clients = len(like_client)
    like = list(like.keys())
    #solution initiale:
    best_solution = initial_solution(nb_ingredients, like)
    first_score= calculate_score(nb_clients, like_client, unlike_client, best_solution)
    print("FISRT_SCORE",first_score)
    #boucle:
    i=0
    list_score=[first_score]
    list_temp=[temp]
    list_solutions=[best_solution]
    while temp > 0.1:

        i+=1
        score_best_solution = calculate_score(nb_clients, like_client, unlike_client, best_solution)
        copy_best_solution = best_solution.copy()
        solution = change_ingredients(copy_best_solution, like, nb_ingredients)
        score_solution = calculate_score(nb_clients,like_client, unlike_client, solution)
        delta_score = score_solution - score_best_solution
        temporary_best_solution=[]
        if delta_score >= 0:
            best_solution = solution
        else:
            # P = exp(-∆score / Temp)
            prob = math.exp(delta_score/temp)
            r=random.uniform(0, 1)
            if r < prob:
               best_solution =solution
        score_this_solution = calculate_score(nb_clients, like_client, unlike_client, best_solution)
        list_score.append(score_this_solution)
        list_solutions.append(best_solution)
        temp = taux_ref * temp
        list_temp.append(temp)
        # print("teperatureeeee", temp)
        # print("scoreeee", score_this_solution)
    #fig, ax = plt.subplots()
    #list_temp.reverse()
    plt.plot(list_temp, list_score)
    plt.xlabel('temperature')
    plt.ylabel('score')
    plt.title("variation du score en fonction de la temperature")
    plt.show()
    score = calculate_score(nb_clients,like_client, unlike_client, best_solution)
    #return best_solution, score
    return score, list_temp , list_score, best_solution

score, list_temp , list_score ,best_solution = recuit_simule(10)
print("LAST_SCORE :",score, "\n", list_temp ,"\n", list_score, "\n","best solution", best_solution)


