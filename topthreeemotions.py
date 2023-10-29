import json

print("Which prediction.json to find top three: ")
result_file = input()

# Open the JSON file and read its contents
with open(f"{result_file}.json", 'r') as fileNow:
    json_response = fileNow.read()

# Parse the JSON response
data = json.loads(json_response)

# Extract emotions and their scores
emotions_data = data[0]["results"]["predictions"][0]["models"]["face"]["grouped_predictions"][0]["predictions"][0]["emotions"]

# Sort emotions by score in descending order
sorted_emotions = sorted(emotions_data, key=lambda x: x["score"], reverse=True)

# Extract top 3 emotions
top_3_emotions = sorted_emotions[:3]

# Print the top 3 emotions
for emotion in top_3_emotions:
    print(f"{emotion['name']}: {emotion['score']}")
