class Flight:
    def __init__(self, id, src, destination, price):
        self.id = id
        self.src = src
        self.destination = destination
        self.price = price

class f_t:
    def __init__(self):
        self.flights = []

    def add(self, flt):
        self.flights.append(flt)

    def srch(self, City_m):
        result = []
        for flt in self.flights:
            if flt.src == City_m or flt.destination == City_m:
                result.append(flt)
        return result

    def srch_form(self, City_m):
        result = []
        for flt in self.flights:
            if flt.src == City_m:
                result.append(flt)
        return result

    def srch_betweem(self, c1, c2):
        result = []
        for flt in self.flights:
            if (flt.src == c1 and flt.destination == c2) or \
               (flt.src == c2 and flt.destination == c1):
                result.append(flt)
        return result

def main():
    ft = f_t()

    # Adding flight data
    ft.add(Flight("AI161E90", "BLR", "BOM", 5600))
    ft.add(Flight("BR161F91", "BOM", "BBI", 6750))
    ft.add(Flight("AI161F99", "BBI", "BLR", 8210))
    ft.add(Flight("VS171E20", "JLR", "BBI", 5500))
    ft.add(Flight("AS171G30", "HYD", "JLR", 4400))
    ft.add(Flight("AI131F49", "HYD", "BOM", 3499))

    print("Select search parameter:")
    print("1. Flights for a particular City")
    print("2. Flights From a city")
    print("3. Flights between two given cities")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        City_m = input("Enter the city: ")
        result = ft.srch(City_m)
    elif choice == 2:
        City_m = input("Enter the city: ")
        result = ft.srch_form(City_m)
    elif choice == 3:
        c1 = input("Enter the first city: ")
        c2 = input("Enter the second city: ")
        result = ft.srch_betweem(c1, c2)
    else:
        print("Invalid choice")
        return

    if result:
        print("ID\tFrom\tTo\tPrice")
        for flt in result:
            print(f"{flt.id}\t{flt.src}\t{flt.destination}\t{flt.price}")
    else:
        print("No flights found for the given criteria")

main()
