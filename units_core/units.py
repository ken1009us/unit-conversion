from pint import UnitRegistry

class Units:
    def __init__(self):
        self.unit_registry = UnitRegistry()


    def convert(self, value, from_unit, to_unit):
        """
        Convert a value from one unit to another.

        :param value: The value to convert.
        :param from_unit: The unit of the value.
        :param to_unit: The unit to convert the value to.
        :return: The converted value.
        """

        quantity = value * self.unit_registry(from_unit)
        converted_value = quantity.to(to_unit).magnitude

        return converted_value

