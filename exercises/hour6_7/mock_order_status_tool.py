def get_order_status(order_id):
    orders = {
        "1001": "Shipped",
        "1002": "Delivered",
        "1003": "Processing"
    }

    return orders.get(order_id, "Order Not Found")

print(get_order_status("1002"))