class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(c):
        c = (c * 9/5) +32
        return print(f"The fahrehnheit value is : {c}")
    

t1 = TemperatureConverter()
TemperatureConverter.celsius_to_fahrenheit(36)

