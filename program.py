# opens and reads a file's data
def get_orders(file):
	file = open(file)
	data = file.read()
	return data

# finds next instance of price number, returns the price and it's end index number
def get_next_order(order):
    start = order.find("\"total_price_usd\"")
    if start == -1:
        return None, 0
    start = order.find(':', start + 1)
    end = order.find(',', start + 2)
    price = order[start + 2:end - 1]
    return price, end

# extracts all price numbers, returns a list of floats
def get_all_orders(page):
    targets = []
    targets_floats = []
    while True:
        price,end = get_next_order(page)
        if price:
            targets.append(price)
            page = page[end:]
        else:
            break

    for i in targets:
	targets_floats.append(float(i))

    return targets_floats

print "total earning are:", sum(get_all_orders(get_orders("orders"))), "USD"

