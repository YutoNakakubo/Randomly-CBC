import random

def generate_blood_counts():
    data = {
        "WBC": random.randint(30, 80),
        "RBC": random.randint(300, 500),
        "Plt": random.randint(150, 300)
    }
    return data

# Example usage
if __name__ == "__main__":
    counts = generate_blood_counts()
    print(counts)