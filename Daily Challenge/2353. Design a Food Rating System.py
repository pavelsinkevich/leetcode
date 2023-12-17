'''Design a food rating system that can do the following:

Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:

FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, 
all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, 
return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, 
or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.'''

# naive approach: 3 private lists, iterate every time
# passed basic testcase, but time limit exceeded on large test
'''class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        food_index = 0
        while food_index < len(self.foods):
            if self.foods[food_index] == food:
                self.ratings[food_index] = newRating
                return
            food_index += 1
        

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        highestRate = 0
        highestRateFood = ""
        for i in range(len(self.foods)):
            if self.cuisines[i] == cuisine:
                if self.ratings[i] == highestRate:
                    if self.foods[i] < highestRateFood:
                        highestRateFood = self.foods[i]
                if self.ratings[i] > highestRate:
                    highestRate = self.ratings[i]
                    highestRateFood = self.foods[i]
        return highestRateFood'''

# faster approach: use hashmaps
'''class FoodRatings(object):
    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # food_detail:
        # {food1: [cuisine1, rate1],
        # food2: [cuisine2, rate2],
        # ...
        # }
        self.food_details = dict()
        # cuisine_rate_food:
        # {cuisine1:
        #   {rate1:
        #       [food1, food2, ...]
        #   rate2:
        #       [food3, food4, ...]
        #   },
        # cuisine2: {...}, ...
        # }
        self.cuisine_rate_food = dict()


        for i in range(len(foods)):
            food_details = []
            food_details.append(cuisines[i])
            food_details.append(ratings[i])
            self.food_details[foods[i]] = food_details
            self.updateCuisineRateFood(foods[i], cuisines[i], None, ratings[i])

    def updateCuisineRateFood(self, food, cuisine, old_rating, new_rating):
        if cuisine not in self.cuisine_rate_food:
            rate_food = dict()
            foods = set()
            foods.add(food)
            rate_food[new_rating] = foods
            self.cuisine_rate_food[cuisine] = rate_food
        else:
            if old_rating != None and old_rating in self.cuisine_rate_food[cuisine]:
                # remove food from old rating dict
                self.cuisine_rate_food[cuisine][old_rating].discard(food)
                if len(self.cuisine_rate_food[cuisine][old_rating]) == 0:
                    del self.cuisine_rate_food[cuisine][old_rating]
            if new_rating in self.cuisine_rate_food[cuisine]:
                self.cuisine_rate_food[cuisine][new_rating].add(food)
            else:
                foods = set()
                foods.add(food)
                self.cuisine_rate_food[cuisine][new_rating] = foods

    def changeRating(self, food, newRating):
        if food in self.food_details:
            old_rating = self.food_details[food][1]
            cuisine = self.food_details[food][0]
            self.food_details[food][1] = newRating
            self.updateCuisineRateFood(food, cuisine, old_rating, newRating)

    def highestRated(self, cuisine):
        cuisine_max_rate = max(self.cuisine_rate_food[cuisine].keys())
        cuisine_max_rate_food = min(self.cuisine_rate_food[cuisine][cuisine_max_rate])

        return cuisine_max_rate_food'''

#even faster solution: use priority queue (heapq because we don't care about thread safety)
from collections import defaultdict
import heapq
# Custom default factory function to return an empty heap queue
def empty_heap_queue():
    return []

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        n = len(foods)
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.food_index = dict(zip(foods, range(n)))
        self.cuisinesMap = defaultdict(empty_heap_queue)
        for i, cuisine in enumerate(cuisines):
            heapq.heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))
            
    def changeRating(self, food, newRating):
        i = self.food_index[food]
        self.ratings[i] = newRating; cuisine = self.cuisines[i]
        heapq.heappush(self.cuisinesMap[cuisine], (-self.ratings[i], self.foods[i]))

    def highestRated(self, cuisine):
        rating, food = self.cuisinesMap[cuisine][0]
        while rating != -self.ratings[self.food_index[food]]:  # check highest rating is current
            heapq.heappop(self.cuisinesMap[cuisine])
            rating, food = self.cuisinesMap[cuisine][0]
        return food


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
'''foodRatings = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
                          ["korean", "japanese", "japanese", "greek", "japanese", "korean"], 
                          [9, 12, 8, 15, 14, 7]);
print(foodRatings.highestRated("korean")); # return "kimchi"
                                    # "kimchi" is the highest rated korean food with a rating of 9.
print(foodRatings.highestRated("japanese")); # return "ramen"
                                      # "ramen" is the highest rated japanese food with a rating of 14.
foodRatings.changeRating("sushi", 16); # "sushi" now has a rating of 16.
print(foodRatings.highestRated("japanese")); # return "sushi"
                                      # "sushi" is the highest rated japanese food with a rating of 16.
foodRatings.changeRating("ramen", 16); # "ramen" now has a rating of 16.
print(foodRatings.highestRated("japanese")); # return "ramen"
                                      # Both "sushi" and "ramen" have a rating of 16.
                                      # However, "ramen" is lexicographically smaller than "sushi".
'''
foodRatings = FoodRatings(["emgqdbo","jmvfxjohq","qnvseohnoe","yhptazyko","ocqmvmwjq"],
                           ["snaxol","snaxol","snaxol","fajbervsj","fajbervsj"],
                           [2,6,18,6,5])
foodRatings.changeRating("qnvseohnoe", 11)
print(foodRatings.highestRated("fajbervsj"))
foodRatings.changeRating("emgqdbo",3)
foodRatings.changeRating("jmvfxjohq",9)
foodRatings.changeRating("emgqdbo",14)
print(foodRatings.highestRated("fajbervsj"))
print(foodRatings.highestRated("snaxol"))
#output:    ["yhptazyko","yhptazyko","qnvseohnoe"]
#expected:  ["yhptazyko","yhptazyko","emgqdbo"]