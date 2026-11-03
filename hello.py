import pandas as pd

data = {
    "component": ["Resistor", "Capacitor", "Inductor", "Diode"],
    "value": [220, 10, 4.7, 0.7],
    "unit": ["ohm", "uF", "mH", "V"],
}

df = pd.DataFrame(data)
print(df)
print()
print("Average value:", round(df["value"].mean(), 2))