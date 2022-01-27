import cx_Oracle
import pandas as pd
from sqlalchemy import types, create_engine
import matplotlib.pyplot as plt

connection = create_engine(
    'oracle+cx_oracle://user:password@213.184.8.44:1521/?service_name=orcl')

cx_Oracle.init_oracle_client(
    lib_dir=r"")

df = pd.read_sql('SELECT * FROM PROJECT_RAPORTS', connection)

raport_types = ['YEAR', 'MONTH', 'QUART']
fig, axes = plt.subplots(3, 2)
fig.tight_layout()

for key, raport in enumerate(raport_types):
    if len(df[df['type'] == raport]) > 0:
        raports = df[df['type'] == raport].sort_values('data_date')

        data = raports[raports['raport_date'] == raports['raport_date'].max()]

        axes[key][0].plot(data['data_date'], data['fights'], 'go-')
        axes[key][1].plot(data['data_date'], data['avg_rounds'], 'bo-')

        axes[key][0].title.set_text(f'Raport ilości walk: {raport}')

        if raport == 'QUART':
            axes[key][0].set_xlabel(f"Kwartał roku {data['year'].max()}")
        else:
            axes[key][0].set_xlabel('Data')

        axes[key][0].set_ylabel('Ilość walk', color='g')

        axes[key][1].title.set_text(f'Raport długości walk: {raport}')

        if raport == 'QUART':
            axes[key][1].set_xlabel(f"Kwartał roku {data['year'].max()}")
        else:
            axes[key][1].set_xlabel('Data')
        axes[key][1].set_ylabel('Średnia długość walk [rundy]', color='b')

        print(df)

plt.show()
