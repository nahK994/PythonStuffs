import pandas as pd

record = { 

 'Name' : ['Ankit', 'Swapnil Roy', 'Aishwarya Roy', 
          'Priyanka Chopra', 'Shivangi', 'Shomi Khan' ],
  
 'Age' : [22, 20, 21, 19, 18, 22], 
  
 'Stream' : ['Math', 'Commerce', 'Science', 
            'Math', 'Math', 'Science'], 
  
 'Percentage' : [90, 90, 96, 75, 70, 80],
 'Hobbies': [["Sleeping", "Eating"], ["Coding"], ["Gardening", "Reading"], ["Bicycle riding"], ["Travelling"], ["Travelling", "Bicycle riding"]]
} 

df = pd.DataFrame(record)

# df.to_csv('dataset.csv', index=False)

# df.index = ['r1', 'r2', 'r3']
# df.columns = ['c1', 'c2', 'c3', 'c4']
# print(df)

# print(df.loc[(df['Stream'] == "Math") & (df['Percentage'] > 80)])


# filtered_list = {
#   'Name': [],
#   'Age': [],
#   'Stream': [],
#   'Percentage': [],
#   'Hobbies': []
# }
# for i in range(len(df.loc[:, "Age"])):
#   if "Bicycle riding" in df.loc[i, 'Hobbies']:
#     filtered_list['Name'].append(df.loc[i, 'Name'])
#     filtered_list['Age'].append(df.loc[i, 'Age'])
#     filtered_list['Stream'].append(df.loc[i, 'Stream'])
#     filtered_list['Percentage'].append(df.loc[i, 'Percentage'])
#     filtered_list['Hobbies'].append(df.loc[i, 'Hobbies'])

# filtered_df = pd.DataFrame(filtered_list)


# filtered_df = df[df['Hobbies'].apply(lambda x: 'Bicycle riding' in x)]
# print(filtered_df)

def calculate_grade(percentage):
    if percentage >= 80:
      return 'A+'
    elif percentage >= 75:
      return 'A'
    elif percentage >= 70:
      return 'A-'
    elif percentage >= 65:
      return 'B+'
    elif percentage >= 60:
      return 'B'
    elif percentage >= 55:
      return 'B-'
    elif percentage >= 50:
      return 'C'
    else:
      return 'F'
    
df['Grade'] = df['Percentage'].apply(calculate_grade)
df['First Name'] = df['Name'].apply(lambda x: x.split(' ')[0])
df['Last Name'] = df['Name'].apply(lambda x: x.split(' ')[1] if len(x.split(' ')) == 2 else '')
print(df.drop('Name', axis=1))
