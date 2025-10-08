def calculate_7_rings_purchases():

    purchase_list = {
        "Diamonds 💎": 10500.00,
        "Champagne 🍾": 150.00,
        "New House 🏡": 750000.00,
        "Private Jet Ticket ✈️": 4500.00,
        "New Hair 💇‍♀️": 850.00
    }
    
    total_cost = sum(purchase_list.values())
    
    print("✨ '7 Rings' Purchase Summary ✨")
    print("---------------------------------")
    
    for item, price in purchase_list.items():
        print(f"{item:<25} $ {price:,.2f}")
        
    print("---------------------------------")
    print(f"**Total Cost of All Purchases:** $ {total_cost:,.2f}")
    print("---------------------------------")
    print("\nI see it, I like it, I want it, I got it. 😉")

if __name__ == "__main__":
    calculate_7_rings_purchases()