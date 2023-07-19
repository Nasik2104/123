import gspread
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('E:\\python_work\\wwork\\16_07\\homework\\creds.json', scope)
client = gspread.authorize(creds)
data = client.open_by_key('12QLk3yWwbmufeR8pmfszM3TDonA9zV-trMDpBZNaXEY')

worksheet_name = 'sheet2'

worksheet = data.worksheet(worksheet_name)

data2 = worksheet.get_all_values()

month = []
study = []
hobby = []

for i in data2[1:]:
    month.append(i[0])
    study.append(int(i[1]))
    hobby.append(int(i[2]))

print(month)
print(study)
print(hobby)

x_indexes = range(len(month))


plt.bar(x_indexes, study, width=0.4, align='center', label='Study')

hobby_shift = [x + 0.4 for x in x_indexes]

plt.bar(hobby_shift, hobby, width=0.4, align='center', label='Hobby')

plt.xlabel('Місяці')
plt.ylabel('Години')
plt.title('Стовпчаста діаграма')
plt.xticks(x_indexes, month)

# plt.xticks(x_indexes, month)

plt.legend()

plt.show()