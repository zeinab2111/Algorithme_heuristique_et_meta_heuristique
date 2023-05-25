import random
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

#glouton selon l'ingredient le plus demande:
def glouton(nb_ingredients):
    list_all, like_client, unlike_client, like= data()
    nb_clients= len(like_client)
    like = sorted(like.items(), key=lambda x: x[1], reverse=True)
    list_ingredients=[]
    for i in range(nb_ingredients):
        list_ingredients.append(like[i][0])
    print(list_ingredients)
    score = calculate_score(nb_clients,like_client, unlike_client, list_ingredients)
    print(score)

#glouton(4)

#glouton en prenant a chaque fois un ingredient et on voit si on le laisse ou pas:
def glouton1(nb_ingredients):
    random.seed(1)
    list_score=[]
    list_all, like_client, unlike_client, like= data()
    nb_clients = len(like_client)
    like = sorted(like.items(), key=lambda x: x[1], reverse=True)
    list_ingredients = [like[0][0]]
    score = calculate_score(nb_clients, like_client, unlike_client, list_ingredients)
    list_score.append(score)
    i=1
    list_nb_try = [0]
    random.shuffle(like)
    while len(list_ingredients)<nb_ingredients:
        #attentionnnn il fautt mettre list
        #print("like",like)
        list_ingredients1 = list(list_ingredients)
        list_ingredients1.append(like[i][0])
        score1= calculate_score(nb_clients, like_client, unlike_client, list_ingredients1)
        if score1 >= score:
            list_ingredients.append(like[i][0])
            score=score1
        list_score.append(score)
        list_nb_try.append(i)
        i+=1
    return list_nb_try,list_ingredients, list_score, score
print(glouton1(10))
list_nb_try,list_ingredients, list_score, score=glouton1(10)
fig, ax = plt.subplots()
ax.plot(list_nb_try, list_score)
plt.xlabel('nombre d' + "\'" + 'essai')
plt.ylabel('score')
plt.title("Progres du score par la methode glouton")
plt.show()

with open ('a_an_example.out.txt', 'w') as file:
    list_nb_try,list_ingredients, list_score, score = glouton1(3)
    file.write(str(len))
    file.write(str(list_ingredients))
    file.write(str(score))










