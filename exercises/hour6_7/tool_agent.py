from datetime import datetime


# Calculator Tool
def calculator_tool():

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nCalculator Results")
    print("------------------")
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)

    if num2 != 0:
        print("Division:", num1 / num2)
    else:
        print("Division: Cannot divide by zero")


# Date Helper Tool
def date_helper_tool():

    print("\nDate Helper Results")
    print("-------------------")
    print("Current Date:", datetime.now().date())
    print("Current Time:", datetime.now().strftime("%H:%M:%S"))


# Mock Order Status Tool
def order_status_tool(order_id):

    orders = {
        "1001": "Shipped",
        "1002": "Delivered",
        "1003": "Processing",
        "1004": "Cancelled"
    }

    return orders.get(order_id, "Order Not Found")


# Main Agent Loop
while True:

    print("\n===================================")
    print("AGENT TOOL MENU")
    print("===================================")
    print("1. calculator")
    print("2. date")
    print("3. order")
    print("4. exit")

    user_input = input(
        "\nChoose tool (calculator/date/order/exit): "
    ).strip().lower()

    if user_input == "exit":

        print("\nAgent: Goodbye!")
        break

    elif user_input == "calculator":

        print("\nAgent selected Calculator Tool")
        calculator_tool()

    elif user_input == "date":

        print("\nAgent selected Date Tool")
        date_helper_tool()

    elif user_input == "order":

        order_id = input("Enter Order ID: ").strip()

        print("\nAgent selected Order Status Tool")
        print("Status:", order_status_tool(order_id))

    else:

        print("\nAgent: Unknown request. Please choose:")
        print("calculator, date, order, or exit")