def main():
    weight_on_Earth = input("What do you weigh on Earth? ")
    weight_on_Mercury = float(weight_on_Earth) * .38
    weight_on_Jupiter = float(weight_on_Earth) * 2.53
    print("\nOn Mercury you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds." %(weight_on_Mercury, weight_on_Jupiter))

# NOTE: This means if the code is run as `python3 planets.py`, run the
# main function.  If the code is merely imported, don't do anything.
if __name__ == '__main__':
    main()


