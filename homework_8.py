# You have 100 cats.  
#One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, 
# always starting at the same spot, with the first cat (cat # 1).
# Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.



def is_square_number(num):
    if num < 0:
        return False

    root = int(num ** 0.5)
    return root * root == num  


def calculate_hats_at_end(num_giri):
    cats_with_cap = []
    for i in range(1, num_giri + 1):
        if is_square_number(i):
            cats_with_cap.append(i) 
        else:
            pass  

    return cats_with_cap

num_giri = 100
result = calculate_hats_at_end(num_giri)
print(result)

