#!/usr/bin/env python3
"""Module implementing the Decorator pattern for beverages and toppings."""


class Beverage:
    """Base interface/class for beverages."""

    def cost(self):
        """Return the cost of the beverage."""
        raise NotImplementedError

    def description(self):
        """Return the description of the beverage."""
        raise NotImplementedError


class Coffee(Beverage):
    """Concrete Coffee beverage."""

    def cost(self):
        """Return the base cost of coffee."""
        return 50

    def description(self):
        """Return the description of coffee."""
        return "Coffee"


class BeverageDecorator(Beverage):
    """Abstract decorator wrapping a beverage."""

    def __init__(self, beverage):
        """Initialize decorator with an inner beverage."""
        self._inner = beverage

    def cost(self):
        """Delegate cost to inner beverage."""
        return self._inner.cost()

    def description(self):
        """Delegate description to inner beverage."""
        return self._inner.description()


class MilkDecorator(BeverageDecorator):
    """Decorator adding milk to a beverage."""

    def cost(self):
        """Add milk cost to inner beverage cost."""
        return self._inner.cost() + 10

    def description(self):
        """Append milk to inner beverage description."""
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Decorator adding sugar to a beverage."""

    def cost(self):
        """Add sugar cost to inner beverage cost."""
        return self._inner.cost() + 5

    def description(self):
        """Append sugar to inner beverage description."""
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Decorator adding caramel to a beverage."""

    def cost(self):
        """Add caramel cost to inner beverage cost."""
        return self._inner.cost() + 15

    def description(self):
        """Append caramel to inner beverage description."""
        return self._inner.description() + " + caramel"


def main():
    """Main function to test the beverage decorator pattern."""
    bev1 = MilkDecorator(Coffee())
    print("{} {}".format(bev1.description(), bev1.cost()))

    bev2 = MilkDecorator(SugarDecorator(Coffee()))
    print("{} {}".format(bev2.description(), bev2.cost()))

    bev3 = CaramelDecorator(MilkDecorator(SugarDecorator(Coffee())))
    print("{} {}".format(bev3.description(), bev3.cost()))


if __name__ == "__main__":
    main()
