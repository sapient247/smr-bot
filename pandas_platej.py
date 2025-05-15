mport pandas as pd
import openpyxl
import os

# Функция для чтения данных из Excel и создания отчета
def generate_and_send_report(payment_type, partner):
    df = pd.read_excel('Реестр платежей.xlsx')

    df['Контрагент без инн'] = df['Контрагент'].str.replace(r'\s*\(.*\)', '', regex=True)
    df['Контрагент за кого платим без инн'] = df['Контрагент (за кого платим)'].str.replace(r'\s*\(.*\)', '', regex=True)

    if payment_type == 'За поставку':
        filtered_df = df[(df['Контрагент за кого платим без инн'] == partner)]
    elif payment_type == 'Оплата работ':
        filtered_df = df[(df['Контрагент без инн'] == partner) & (df['Контрагент (за кого платим)'].isnull())]
    else:
        raise ValueError('Неподдерживаемый тип платежа')

    output_folder = 'запросы'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_filename = os.path.join(output_folder, f'{partner}.xlsx')
    filtered_df.to_excel(output_filename, index=False)
    return output_filename
