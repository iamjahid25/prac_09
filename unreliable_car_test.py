from unreliable_car import UnreliableCar


def main():
    """Test driving behavior of reliable and unreliable UnreliableCar instances."""
    reliable_car = UnreliableCar("Reliable", 100, 90)
    unreliable_car = UnreliableCar("Unreliable", 100, 10)

    print("Driving ReliableCar:")
    for i in range(5):
        distance = reliable_car.drive(20)
        print(f"Attempt {i+1}: drove {distance}km")

    print("\nDriving UnreliableCar:")
    for i in range(5):
        distance = unreliable_car.drive(20)
        print(f"Attempt {i+1}: drove {distance}km")


if __name__ == "__main__":
    main()
