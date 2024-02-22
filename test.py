from thefuzz import fuzz

name = "Kurtis Pykes"
full_name = "Kurtis K D Pykes"

print(f"Similarity score: {fuzz.ratio(name, full_name)}")

