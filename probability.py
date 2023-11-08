import itertools

dice_faces = [1, 2, 3, 4, 5, 6]
dice_rolls = list(itertools.product(dice_faces, repeat=6))

sum_18_count = sum(1 for roll in dice_rolls if sum(roll) == 18)

probability = sum_18_count / len(dice_rolls)

print(f"The probability of the sum being 18 when rolling 6 dice is {probability}")
