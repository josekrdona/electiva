#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyodbc


# In[30]:


import pyodbc

direccion_servidor = '127.0.0.1'
nombre_bd = 'Hospital'
nombre_usuario = 'Hospital'
password = 'hospital'

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + direccion_servidor+';DATABASE='+nombre_bd+';UID='+ nombre_usuario +';PWD=' + password)
    print('Conexión exitosa')
    
    
    cursor = conexion.cursor()

    #Obtenemos los datos
    cursor.execute("SELECT Cantidad, Medicamento from Formulas")

    result = cursor.fetchall

    medicamentos = []
    cantidades = []

    for registro in cursor:
        medicamentos.append(registro[0])
        cantidades.append(registro[1])

    plt.bar(medicamentos, cantidades)
    plt.ylim(0,5)
    plt.xlabel("Cantidad")
    plt.ylabel("Medicamentos")
    plt.title("Cantidad de medicamentos por nombre")
    plt.show()
except Exception as e:
    print("Error: ", e)


