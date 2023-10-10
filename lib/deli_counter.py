katz_deli = []

def line(customers):
    if len(customers) == 0:
        return "The line is currently empty."
    
    number = [f"{index}. {customer}" for index, customer in enumerate(customers, 1)]
    return "The line is currently: " + ", ".join(number)

print(line(["Ada", "Gracie", "Kent"]))

def take_a_number(customers, customer_name):
    customers.append(customer_name)  # Add the customer to the end of the line
    position = len(customers)  # Calculate the position in line (count starts from 1)
    return f"Welcome, {customer_name}. You are number {position} in line."

print(take_a_number(katz_deli, "Ada"))

def now_serving(customers):
    if len(customers) == 0:
        return "There is nobody waiting to be served!"
    else:
        served_customer = customers.pop(0)  # Serve the first customer in line
        return f"Currently serving {served_customer}."

print(now_serving(katz_deli))
