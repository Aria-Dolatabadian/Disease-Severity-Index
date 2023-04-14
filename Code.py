#Suppose you are a plant pathologist studying a particular plant disease,
# and you have collected data on the disease severity for a sample of plants.
# You want to calculate the Disease Severity Index (DSI) for this sample,
# which will give you a measure of the overall severity of the disease across all plants.
#You ask the user for the following input values:
#The total number of plants in the sample (let's say 50): num_plants = 50
#The maximal disease index for this particular disease (let's say 5): max_index = 5.0
#The score of each rating class, separated by spaces (let's say a rating of 1 corresponds to a score of 1, a rating of 2 corresponds to a score of 2, and so on): rating_scores = [1.0, 2.0, 3.0, 4.0]
#The frequency of each rating class, separated by spaces (let's say 10 plants had a rating of 1, 20 plants had a rating of 2, 15 plants had a rating of 3, and 5 plants had a rating of 4): class_freq = [10, 20, 15, 5]

#DSI = (Σ (class_freq[i] * rating_scores[i]) / (num_plants * max_index)) * 100
# Get input values from the user
import matplotlib.pyplot as plt
num_plants = int(input("Enter the total number of plants: "))  # Enter 50
max_index = float(input("Enter the maximal disease index: "))  # Enter 5
rating_scores = list(map(float, input("Enter the score of each rating class, separated by spaces: ").split()))  # Enter 1 2 3 4
class_freq = list(map(int, input("Enter the frequency of each rating class, separated by spaces: ").split()))  # Enter 10 20 15 5
# Calculate the Disease Severity Index (DSI)
numerator = sum([class_freq[i] * rating_scores[i] for i in range(len(class_freq))])  # numerator = (10 * 1) + (20 * 2) + (15 * 3) + (5 * 4) = 115
denominator = num_plants * max_index  # denominator = 250
dsi = (numerator / denominator) * 100  # dsi = (115 / 250) * 100 = 46.00
# Print the Disease Severity Index (DSI)
print("The Disease Severity Index (DSI) is: {:.2f}%".format(dsi))  # This will print: "The Disease Severity Index (DSI) is: 46.00%"
fig, ax = plt.subplots()
ax.bar(rating_scores, class_freq)
ax.set_xlabel("Rating Scores")
ax.set_ylabel("Frequency")
ax.set_title("Rating Class Frequency")
ax.text(0.7, 0.9, f"DSI = {dsi:.2f}%", transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

plt.show()
