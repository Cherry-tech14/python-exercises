resources = [
    {
        "id": "R001",
        "name": "Laptop",
        "category": "Electronics",
        "total": 10,
        "available": 10
    },
    {
        "id": "R002",
        "name": "Keyboard",
        "category": "Accessories",
        "total": 5,
        "available": 5
    },
    {
        "id": "R003",
        "name": "Headset",
        "category": "Accessories",
        "total": 3,
        "available": 3
    }
]

fellows = {
    "F001": "Ada",
    "F002": "John",
    "F003": "Grace"
}

borrow_records = []


def list_resources():
    for resource in resources:
        print(
            f"ID: {resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']}"
        )


def add_resource():
    resource_id = input("Enter resource ID: ")

    for resource in resources:
        if resource["id"] == resource_id:
            print("Error: Resource ID already exists.")
            return

    name = input("Enter resource name: ")
    category = input("Enter resource category: ")
    total = int(input("Enter total units: "))

    resource = {
        "id": resource_id,
        "name": name,
        "category": category,
        "total": total,
        "available": total
    }

    resources.append(resource)

    print("Resource added successfully.")


def borrow_resource():
    fellow_id = input("Enter fellow ID: ")

    if fellow_id not in fellows:
        print("Error: Fellow ID not found.")
        return

    resource_id = input("Enter resource ID: ")

    resource = None

    for item in resources:
        if item["id"] == resource_id:
            resource = item
            break

    if resource is None:
        print("Error: Resource ID not found.")
        return

    quantity = int(input("Enter quantity to borrow: "))

    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return

    if quantity > resource["available"]:
        print("Error: Not enough stock available.")
        return

    resource["available"] -= quantity

    borrow_records.append({
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    })

    print("Borrowing successful.")


def return_resource():
    fellow_id = input("Enter fellow ID: ")
    resource_id = input("Enter resource ID: ")
    quantity = int(input("Enter quantity to return: "))

    for record in borrow_records:
        if record["fellow_id"] == fellow_id and record["resource_id"] == resource_id:

            if quantity > record["quantity"]:
                print("Cannot return more than borrowed.")
                return

            for resource in resources:
                if resource["id"] == resource_id:
                    resource["available"] += quantity
                    break

            record["quantity"] -= quantity

            if record["quantity"] == 0:
                borrow_records.remove(record)

            print("Return successful.")
            return

    print("No loan found.")


def search_resources():
    search_name = input("Enter resource name: ")

    for resource in resources:
        if search_name.lower() in resource["name"].lower():
            print(
                f"{resource['id']} | "
                f"{resource['name']} | "
                f"{resource['category']} | "
                f"Available: {resource['available']}"
            )


def filter_by_category():
    category = input("Enter category: ")

    for resource in resources:
        if resource["category"].lower() == category.lower():
            print(
                f"{resource['id']} | "
                f"{resource['name']} | "
                f"{resource['category']} | "
                f"Available: {resource['available']}"
            )


def show_report():
    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    borrowed_units = total_units - available_units

    print("Total units:", total_units)
    print("Available units:", available_units)
    print("Borrowed units:", borrowed_units)

    print("Low stock resources:")

    for resource in resources:
        if resource["available"] < 3:
            print(resource["name"])

    most_borrowed = 0

    print("Most borrowed resources:")

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed > most_borrowed:
            most_borrowed = borrowed

    for resource in resources:
        borrowed = resource["total"] - resource["available"]

        if borrowed == most_borrowed and borrowed > 0:
            print(resource["name"])


while True:
    print("\nLearn2Earn Equipment System")
    print("1. List resources")
    print("2. Add resource")
    print("3. Borrow resource")
    print("4. Return resource")
    print("5. Search resources")
    print("6. Filter by category")
    print("7. Show report")
    print("8. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        list_resources()

    elif choice == "2":
        add_resource()

    elif choice == "3":
        borrow_resource()

    elif choice == "4":
        return_resource()

    elif choice == "5":
        search_resources()

    elif choice == "6":
        filter_by_category()

    elif choice == "7":
        show_report()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")