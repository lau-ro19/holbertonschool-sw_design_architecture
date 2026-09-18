#!/usr/bin/env python3
"""Module implementing the Factory pattern with a registry for vehicles."""


class VehicleFactory:
    """A factory to manage and create vehicle instances using a registry."""

    def __init__(self):
        """Initialize the factory with an empty registry."""
        self._registry = {}

    def register_kind(self, kind, cls):
        """Register a new vehicle class with a given key."""
        self._registry[kind] = cls

    def create(self, kind):
        """Create and return an instance of the registered vehicle kind."""
        if kind in self._registry:
            return self._registry[kind]()
        raise ValueError("Unknown vehicle kind: {}".format(kind))


class Bus:
    """Represent a bus vehicle."""

    def mode(self):
        """Return the operation mode of a bus."""
        return "road"


class Train:
    """Represent a train vehicle."""

    def mode(self):
        """Return the operation mode of a train."""
        return "rails"


class Bike:
    """Represent a bike vehicle."""

    def mode(self):
        """Return the operation mode of a bike."""
        return "lane"


class Scooter:
    """Represent a scooter vehicle."""

    def mode(self):
        """Return the operation mode of a scooter."""
        return "scooter_lane"


def main():
    """Main function to test the vehicle factory."""
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)
    factory.register_kind("scooter", Scooter)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
