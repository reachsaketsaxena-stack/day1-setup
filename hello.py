import pandas as pd

data = {
    "component": ["Resistor", "Capacitor", "Inductor"],
    "value": [220, 10, 4.7],
    "unit": ["ohm", "uF", "mH"],
}

df = pd.DataFrame(data)
print(df)
print()
print("Average value:", df["value"].mean())