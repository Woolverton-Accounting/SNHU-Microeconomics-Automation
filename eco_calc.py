def calculate_elasticity(old_p, new_p, old_q, new_q):
    # Calculate percentage changes
    pct_change_price = (new_p - old_p) / old_p
    pct_change_quantity = (new_q - old_q) / old_q
    
    # Calculate Elasticity (using absolute value for standard economics)
    elasticity = abs(pct_change_quantity / pct_change_price)
    
    # Analyze the result using Python conditional logic
    if elasticity > 1:
        status = "Elastic (Highly sensitive to price changes)"
    elif elasticity < 1:
        status = "Inelastic (Low sensitivity to price changes)"
    else:
        status = "Unit Elastic"
        
    return round(elasticity, 2), status

# Example: SNHU homework problem where a price hike drops sales
price_today, price_tomorrow = 10, 12
sales_today, sales_tomorrow = 500, 350

score, evaluation = calculate_elasticity(price_today, price_tomorrow, sales_today, sales_tomorrow)
print(f"Elasticity Score: {score} -> {evaluation}")
