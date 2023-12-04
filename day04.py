def calculate_points(cards):
    total_points = 0

    for idx, card in enumerate(cards, start=1):
        # Split the card data into winning and your numbers
        card_data = card.split(': ')[1].split('|')
        winning_numbers = set(map(int, card_data[0].split()))
        your_numbers = list(map(int, card_data[1].split()))

        points = 0  # Reset points to 0 for each card
        matched_numbers = set()

        for num in your_numbers:
            if num in winning_numbers and num not in matched_numbers:
                matched_numbers.add(num)
                if points == 0:
                    points = 1 
                elif points >= 1:
                    points *= 2  # Double points for subsequent matches

        total_points += points
        print(f"Card {idx}: {points} points")
        print(f"Matched numbers for Card {idx}: {matched_numbers}")

    return total_points


# Read card data from file
file_path = 'puzzle-day04.txt'
with open(file_path, 'r') as file:
    cards_data = file.readlines()

total_points = calculate_points(cards_data)
print(f"\nThe total points of the cards are: {total_points}")
