import math, random

#Step-1
def chromosome_structure(chromosome):
    out=[]
    for key,value in chromosome.items():
        out.append(value)
    return out


#Step-2
initial_random= []
for i in range(4):
    chromosome = {}
    chromosome["stop_loss"] = random.randint(1, 99)
    chromosome["take_profit"] = random.randint(1, 99)
    chromosome["trade_size"] = random.randint(1, 99)
    initial_random.append(chromosome)


#step-3
def fitness(chromosome):
    history = [-1.2, 3.4, -0.8, 2.1, -2.5, 1.7, -0.3, 5.8, -1.1, 3.5]
    icapital = 1000
    fcapital = icapital
    for i in range(len(history)):
        size=(chromosome[2]*0.01)*fcapital
        if history[i]*-1>chromosome[0]:
            loss=size*chromosome[0]*0.01
            fcapital-=loss
        elif history[i]>chromosome[1]:
            profit=size*chromosome[1]*0.01
            fcapital+=profit
        else:
            profit=size*history[i]*0.01
            fcapital+=profit
        
    return round(fcapital-icapital,2)


#Step-4
def parent_selection(initial_population):
    i,j=random.randint(0,3),random.randint(0,3)
    while i==j:
        j=random.randint(0,3)
    return [initial_population[i],initial_population[j]]


#Step-5
def crossover(parents):
    p1,p2=parents[0],parents[1]
    idx=random.randint(1,2)
    child1=p1[:idx]+p2[idx:]
    child2=p2[:idx]+p1[idx:]
    return [child1,child2]


#step-6
def mutation(child1,child2):
    #10% mutation rate
    idx=random.randint(0,2)

    child1_range=round(child1[idx]*0.1,1)
    child1_lower_bound=child1[idx]-child1_range
    child1_upper_bound=min(99,child1[idx]+child1_range)
    child1[idx]=round(random.uniform(child1_lower_bound,child1_upper_bound),2)


    child2_range=round(child2[idx]*0.1,1)
    child2_lower_bound=child2[idx]-child2_range
    child2_upper_bound=min(99,child2[idx]+child2_range)
    child2[idx]=round(random.uniform(child2_lower_bound,child2_upper_bound),2)

    return child1,child2


#Miscellaneous
def fittest_parents(population):
    temp={}
    for i in range(len(population)):
        score=fitness(population[i])
        key=tuple(population[i])
        temp[key]=score
    fittest=list(sorted(temp.items(), key=lambda value: value[1],reverse=True))
    fittest=fittest[:2]
    fittest=[list(parents[0]) for parents in fittest] 
    return fittest

        


######################################################
def gen_algo(init):
    new_population=[]

    for i in range(10):
        parents=parent_selection(init)
        children=crossover(parents)
        child1,child2=mutation(children[0],children[1])

        #Step-7
        new_population.extend([child1,child2])
        elites=fittest_parents(init)
        new_population.extend(elites)

        init=new_population
        new_population=[]


    best=[None,-math.inf]
    for i in init:
        score=fitness(i)
        if score>best[1]:
            best[0]=i
            best[1]=score
    return best


initial_population=[]
for i in range(len(initial_random)):
    initial_population.append(chromosome_structure(initial_random[i]))

best,score=gen_algo(initial_population)


#Output
print(f"""best_strategy:
stop_loss: {best[0]}, take_profit: {best[1]}, trade_size: {best[2]}
Final_profit: {score}""")
 





print("############################################")
#Part-2

def two_point_crossover(parents):
    p1,p2=parents
    idx1=random.randint(1,1)
    idx2=random.randint(2,2)

    child1=p1[:idx1]+p2[idx1:idx2]+p1[idx2:]
    child2=p2[:idx1]+p1[idx1:idx2]+p2[idx2:]
    return child1,child2

parents=parent_selection(initial_population)
print(f"Parents : {parents[0]}, {parents[1]}")
child1,child2=two_point_crossover(parents)
print(f"""Two offsprings after two-point crossover:
{child1}, {child2}""")