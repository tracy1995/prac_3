name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# Using f-string formatting
print(f"{year} {name} for about ${cost:,.0f}")

# Using a for loop with range function and string formatting
for i in range(0, 201, 50):
    print(f"{i:3}")
