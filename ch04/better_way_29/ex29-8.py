class FixedResistance(Resistor):
    # ...
    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms


r4 = FixedResistance(1e3)
r4.ohms = 2e3

>>>
AttributeError: Can't set attribute
