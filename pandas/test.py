import pandas as pd

mydataset = {
  "name": ["Shomi", "Khan", "Batman"],
  "city": ["Kushtia", "Sylhet", "Gotham"],
  "age": [31, 32, 33],
  "hobbies": [["Sleeping", "Eating"], ["Coding"], ["vigilante"]]
}

df = pd.DataFrame(mydataset)

# df.to_csv('dataset.csv', index=False)
print(df.loc[(df['age'] == 32)])
