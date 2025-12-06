from inventory import Product

def main():
    print("Reorder Report:\n" + "-" * 20)

    products = [
        Product("Notebook", 12, 20),
        Product("Pen", 30, 10),
        Product("Marker", 10, 15),
        Product("Stapler", 5, 10),
    ]

    for p in products:
        if p.needs_reorder():
            print(f" Reorder needed for {p.name} (Stock: {p.stock}, Min: {p.min_stock})")

    print("Check complete.")

if __name__ == "__main__":
    main()
