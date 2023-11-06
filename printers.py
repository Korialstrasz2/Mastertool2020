# def tirod6(attacco, difesa,dado) :
#     hit = 0
#     miss = 0
#     for item in range(attacco):
#         for dif in range(difesa):
#             for tiro in range(dado):
#
#                 if item + tiro > difesa+5:
#                     hit += 1
#                 else:
#                     miss += 1
#     return(round((100/(hit+miss)),2)* hit)
#
# for ciclo in range(5,20):
#     array = []
#     for ciclo2 in range(5,20):
#         array.append(tirod6(ciclo, ciclo2, 20))
#     print(array)


def tirod6(attacco, difesa,dado) :
    hit = 0
    miss = 0
    for tiro in range(dado):
        if attacco + tiro > difesa + 5:
            hit += 1
        else:
            miss += 1
    return(round((100/(hit+miss))* hit))

for ciclo in range(5,20):
    array = []
    for ciclo2 in range(5,20):
        array.append(tirod6(ciclo, ciclo2, 14))
    print(array)

# import openpyxl
# datab = 699
# skilln = 1
# topv = 0.17
# x = 0.05
# y = 0.12
# for item in range(31,61):
#     print(f"""            TextInput:
#                 padding: 2, 2, 2, 2
#                 size_hint: 0.015, 0.025
#                 background_color: 0.3, 0.7, 0, 0.15
#                 pos_hint: {{"x": {x}, "top": {y}}}
#                 id: freccia{item}kv
#                 font_size: 14""")
#     x += 0.015
#     if item == 45:
#         x = 0.05
#         y = 0.085
# for item in range(31,61):
#     print(f"freccia{item}kv: freccia{item}kv")

#---------------------------------NEGOZIO, IMPORTA E STAMPA COLONNE ----------------------------
# valori_colonna_1 = [4,1,1,0,2,3,1,5,4,1,1,1,'7%',0,3,0,1,0,0,1,'no']
# y = 0.9
# for item in valori_colonna_1:
#     print(f"""box.add_widget(Button(text="{str(item)}", pos_hint={{"center_x": 0.05, "center_y": {round(y, 5)}}}, on_release=partial(addspesa, 30),
#                       size_hint=(0.03, 0.05), background_color=(1, 0.3, 0.3, 0.5)))""")
#     y -= 0.05
# wb = openpyxl.load_workbook("tansactions.xlsx")
# sheet = wb["Foglio1"]
# for colonna in range(1,11):
#     exec(f"valori_colonna_{colonna} = []")
#     for valore in range(21):
#         cell = sheet.cell(valore+2, 21+colonna)
#         exec(f"valori_colonna_{colonna}.append(str(cell.value))")
#     printer = (f"valori_colonna_{colonna}")
#     print(f"valori_colonna_{colonna} = " + str(eval(printer)))
# -----------------------------------IMPORTA DATI NEMICI EXCEL-------------------------------------
# wb = openpyxl.load_workbook("tansactions.xlsx")
# sheet = wb["Foglio1"]
# distruttorelivello = []
# for value1 in range(1, 19):
#     cell = sheet.cell(12,value1+1)
#     distruttorelivello.append(str(cell.value))
# print(f"distruttorelivello = {distruttorelivello}")
#
#
# gruppo1 = ["pf", "attacco", "difesa", "mana", "potere", "volonta", "pa", "res_fis", "res_mag", "rd", "livello",
#            "velocita","skill1", "skill2", "paspesi", "arma", "parimanenti", "manaspeso", "danno", "crit_min",
#            "crit_nor", "crit_mag", "bucard", "dado","rd_fuoco","rd_gelo","rd_elettro"]
#
# numeroitem = 198
# for item in gruppo1:
#     exec(f"""scheletro{item} = []
# for value1 in range(1, 19):
#     cell = sheet.cell({numeroitem},value1+1)
#     scheletro{item}.append(str(cell.value))
# print(f"scheletro{item} = {{scheletro{item}}}")""")
#     numeroitem += 1
# --------------------------------------------------------------------------------------------------

# def printer():
#     y = 0.8
#     x = 0.1
#     alfa = 1
#     tipo = ["rossi", "verdi", "blu", "extra", "skill","na"]
#     roll = 0
#     beta = 1
#     tipoprint = tipo[roll]
#     for valore in range(200):
#
#         print(f"""box.add_widget((Label(text="S. {valore+1}", pos_hint={{"center_x": 0.08, "center_y": {y}}}, size_hint=(0.1, 0.05))))""")
#         alfa += 1
#         y -= 0.035
#
#         if alfa == 41:
#             alfa = 1
#             roll += 1
#             tipoprint = tipo[roll]
#
#
#
#
# printer()
#
# for numero in range(21):
#     print(f"self.zaino_slot_1= self.ids['zaino{numero}'].text")
#
# for item in range(20):
#     print(f"""    TextInput:
#         text:""
#         id: zaino_slot_{item+1}kv""")



