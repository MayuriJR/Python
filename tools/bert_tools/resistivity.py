
def compute_resistivity(voltage_resistor, voltage_measure,
                        r=100, length=0.1, square=0.003):
    current = voltage_resistor / r
    r_soil = voltage_measure / current
    resistivity = r_soil * square / length
    return resistivity


if __name__ == "__main__":
    print(compute_resistivity(0.38, 4.3))

