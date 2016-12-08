data_nasc=input("Insira sua data de nascimento(dd/mm/yyyy): ")

mes=data_nasc[data_nasc.find("/")+1:data_nasc.find("/")+3:1]

if mes=="01":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Janeiro", data_nasc[6:]))

elif mes=="02":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Fevereiro", data_nasc[6:]))

elif mes=="03":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Marco", data_nasc[6:]))

elif mes=="04":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Abril", data_nasc[6:]))

elif mes=="05":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Maio", data_nasc[6:]))

elif mes=="06":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Junho", data_nasc[6:]))

elif mes=="07":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Julho", data_nasc[6:]))

elif mes=="08":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Agosto", data_nasc[6:]))

elif mes=="09":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Setembro", data_nasc[6:]))

elif mes=="10":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Outubro", data_nasc[6:]))

elif mes=="11":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Novembro", data_nasc[6:]))

elif mes=="12":
    print("Voce nasceu em %s de %s de %s"%(data_nasc[:2], "Dezembro", data_nasc[6:]))
