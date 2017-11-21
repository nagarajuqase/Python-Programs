import pandas as pd
df = pd.read_excel('D:\\RobotFramework_Selenium\\ReadFilePandas.xlsx', 'Sample')
print(df)
print(df.columns)
print(df['Locator'])

for i in df.index:
    print(df['Locator'][i])

locator = df['Locator']
print(locator[0])

df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],
                   'b':[3,5,6,2,4,6,7,8,7,8,10]})

writer = pd.ExcelWriter('D:\\RobotFramework_Selenium\\ReadFilePandas2.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()

df = pd.read_excel('D:\\RobotFramework_Selenium\\ReadFilePandas2.xlsx', 'Sheet1')
print(df)