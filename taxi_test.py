from taxi import Taxi


def main():
    """Test the Taxi class functionality as per practical instructions."""
    my_taxi = Taxi("Prius 1", 100)

    # Drive 40 km and display status
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # Reset fare, drive 100 km and display updated status
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


if __name__ == "__main__":
    main()
