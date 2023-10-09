import os

def colectInfo():
    class InfoPROJ:
        obj = "Informations"

    os.system('clear') or None

    InfoPROJ.name = input("Qual o nome do projeto? \n")
    os.system('clear') or None

    InfoPROJ.weeks_study = float(input("Quantas semanas você precisa para estudar? \n"))
    os.system('clear') or None
    
    dublework = int(input("Você fará o design junto com o protótipo? \n 1) SIM \n 2) NÃO \n R: "))
    os.system('clear') or None
    
    if(dublework == 1):
        InfoPROJ.dublework = True

        InfoPROJ.weeks_dublework = float(input("Quantas semanas você precisa para fazer o design? \n"))
        os.system('clear') or None
    else:
        InfoPROJ.dublework = False

        InfoPROJ.weeks_design = float(input("Quantas semanas você precisa para fazer o design? \n"))
        os.system('clear') or None
        
        InfoPROJ.weeks_prot = float(input("Quantas semanas precisa para fazer o protótipo? \n"))
        os.system('clear') or None
    
    InfoPROJ.devs_num = int(input("Quantas pessoas trabalharão no {}? \n".format(InfoPROJ.name)))
    os.system('clear') or None
    
    if(InfoPROJ.devs_num > 1):
        InfoPROJ.wages = []
        for x in range(InfoPROJ.devs_num):
            InfoPROJ.wages.append(float(input("Salário do funcionário {}? \n" .format(x))))
            os.system('clear') or None
    else:
        InfoPROJ.wage = 1320

    
    InfoPROJ.weeks_development = float(input("Quantas semanas para programação? \n"))
    os.system('clear') or None
    
    InfoPROJ.weeks_tests = float(input("Quantas semanas ao todo de testes? (Lembrando que são importantes estarem presentes desde o inicio) \n"))
    os.system('clear') or None

    InfoPROJ.weeks_security = float(input("Qual será a margem de segurança? \n"))
    os.system('clear') or None

    return InfoPROJ

def calculatePrice():
    Project = colectInfo()

    weeks_total = Project.weeks_tests + Project.weeks_security + Project.weeks_development

    if(Project.dublework == True):
        weeks_total += Project.weeks_dublework
    else:
        weeks_total += Project.weeks_design + Project.weeks_prot

    weeks_total += Project.weeks_study

    days_of_job = weeks_total * 7
    
    if(Project.devs_num > 1):
        employees = 0
        for i in Project.wages:
            employees += i
        price = (employees / 30) * days_of_job
    else:
        price = (Project.wage / 30) * days_of_job
    
    price_dol = price / 5.06

    print(f"O valor para desenvolver o {Project.name} é R${price} ou US${price_dol} \n" )
    reply = int(input("Deseja fazer novo projeto? \n 1)Sim \n 2)Sair \n"))
    if(reply == 1):
        calculatePrice()
    else:
        return 0

calculatePrice()