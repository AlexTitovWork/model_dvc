import pandas as pd
array_data = [["repair", "materials", "rub"],
    ["food", "pizza", "rub"],
    ["services", "delivery", "rub"],
    ["donation", "donation", "usd"],
    ["repair", "work", "rub"],
    ["coffee", "usd"],
    ["lunch", "rub"],
    ["lunch","usd"],
    ["dentist", "usd"]]
splitMessage = pd.DataFrame(array_data)
print(splitMessage)
# splitMessage.get_value(1,)