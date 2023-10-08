from pint import UnitRegistry, UndefinedUnitError, DimensionalityError

class Units:
    """
    A class used to handle unit conversions.

    Attributes:
    - unit_registry (UnitRegistry): A registry to handle unit conversions and definitions.

    Methods:
    - convert(value, from_unit, to_unit): Converts a value from one unit to another.
    """

    def __init__(self):
        """
        Initializes the Units class with a unit registry for handling unit conversions.
        """
        self.unit_registry = UnitRegistry()


    def convert(self, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.

        :param value: The value to convert.
        :param from_unit: The unit of the value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        """

        try:
            quantity = value * self.unit_registry(from_unit)
            converted_value = quantity.to(to_unit).magnitude

            return converted_value

        except UndefinedUnitError as e:
            print(f"Error: The unit '{e.unit}' is not defined.")
            raise

        except DimensionalityError as e:
            print(f"Error: Cannot convert from '{from_unit}' to '{to_unit}'. {e}")
            raise

        except ValueError as e:
            print(f"Error: The value must be a number. {e}")
            raise
