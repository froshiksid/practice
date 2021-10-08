SNP_age_disease = {}  # Создаем пустой словарь для добавления туда значений

# Создаем списки, для добавления туда соответсвующих значений
SNP_age_disease['Фамилия     '] = []
SNP_age_disease['Имя         '] = []
SNP_age_disease['Отчество    '] = []
SNP_age_disease['Год рождения'] = []
SNP_age_disease['Болезнь     '] = []

number = 0

# Дабавляем значения в списки и словарь
for i in range(1, 6):
    number += 1
    value_1 = input('Введите фамилию призывника №%d: ' % number) + ' | '
    SNP_age_disease['Фамилия     '].append(value_1)
    value_2 = input('Введите имя призывника №%d: ' % number) + ' | '
    SNP_age_disease['Имя         '].append(value_2)
    value_3 = input('Введите отчество призывника №%d: ' % number) + ' | '
    SNP_age_disease['Отчество    '].append(value_3)
    value_4 = input('Введите год рождения призывника №%d: ' % number) + ' | '
    SNP_age_disease['Год рождения'].append(value_4)
    value_5 = input('Введите данные о болезни призывника №%d: ' % number) + ' | '
    SNP_age_disease['Болезнь     '].append(value_5)

# Вывод значений
for i in SNP_age_disease:
    print(i, ' |', *SNP_age_disease[i], sep="")
