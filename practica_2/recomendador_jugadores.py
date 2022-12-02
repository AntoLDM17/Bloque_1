import pandas as pd
import re

def extract():
    df = pd.read_csv('fifa23players.csv')
    return df

def transform(df):
    
    #Escojo las columnas que me interesan
    df = df[['Known As','Full Name','Overall','Potential','Best Position','Age','Height(in cm)','Weight(in kg)','Value(in Euro)','Nationality','Club Name','Preferred Foot','Skill Moves','Weak Foot Rating','Positions Played']]
    #Obtenemos todas las posiciones
    all_positions = [re.sub(r'\[|\]|\'', '', x).split(", ") for x in df['Best Position'].unique()]
    #Obtenemos todas las posiciones sin repetir
    all_positions_filtered = [j for i in all_positions for j in i]

    list_of_positions = list(set(all_positions_filtered))
    list_of_positions.sort()

    #Obtenemos la posición que vamos a buscar
    valid = False
    while valid == False:
        print("You can choose between the following positions:\n", list_of_positions)
        entrada = input("Enter the position you want to see the best players for:\n")
        regex = re.compile(entrada, re.IGNORECASE)
        if regex.match("GK"):
            valid = True
        elif regex.match("CB"):
            valid = True
        elif regex.match("LB"):
            valid = True
        elif regex.match("RB"):
            valid = True
        elif regex.match("LWB"):
            valid = True
        elif regex.match("RWB"):
            valid = True
        elif regex.match("CDM"):
            valid = True
        elif regex.match("CM"):
            valid = True
        elif regex.match("CAM"):
            valid = True
        elif regex.match("LM"):
            valid = True
        elif regex.match("RM"):
            valid = True
        elif regex.match("LW"):
            valid = True
        elif regex.match("RW"):
            valid = True
        elif regex.match("CF"):
            valid = True
        elif regex.match("ST"):
            valid = True
        else:
            print("Please enter a valid option")

    #Limpio la regex 
    position = [x for x in all_positions_filtered if regex.match(x)][0]
    

    #Sacamos un nuevo dataframe sólo con los jugadores que juegan en la posición que buscamos
    final_df = df[df['Best Position'].str.contains(position)]
    final_df = final_df.sort_values(by=['Overall'], ascending=False)
    return final_df
   

def load(data):
    print("Recommending the 5 best players for that position:\n")
    #Imprimimos los 5 primeros:
    for i in range(5):
        print(str(i+1) + ".-", data.iloc[i]['Known As'], "(", data.iloc[i]['Overall'], ")")
    
    valid = False
    while valid == False:
        entrada = input("Would you like to see more data about the players? (1 to 5, or EXIT to exit app):\n")
        #Intentamos convertir la entrada a un número
        try:
            entrada = int(entrada.replace(" ", ""))
            if entrada >= 1 and entrada <= 5:
                print("Nombre completo:",data.iloc[entrada-1]['Full Name'])
                print("Valoración:",data.iloc[entrada-1]['Overall'])
                print("Potencial:",data.iloc[entrada-1]['Potential'])
                print("Edad:",data.iloc[entrada-1]['Age'])
                print("Altura:",data.iloc[entrada-1]['Height(in cm)'])
                print("Peso:",data.iloc[entrada-1]['Weight(in kg)'])
                print("Valor de mercado:",data.iloc[entrada-1]['Value(in Euro)'])
                print("Nacionalidad:",data.iloc[entrada-1]['Nationality'])
                print("Club:",data.iloc[entrada-1]['Club Name'])
                print("Pie hábil:",data.iloc[entrada-1]['Preferred Foot'])
                print("Filigranas (estrellas):",data.iloc[entrada-1]['Skill Moves'])
                print("Pierna mala (estrellas):",data.iloc[entrada-1]['Weak Foot Rating'])
                print("Posiciones alternativas:",data.iloc[entrada-1]['Positions Played'])

        except:
            #comprobamos si la entrada es EXIT
            regex = re.compile(entrada, re.IGNORECASE)
            if regex.match("exit"):
                valid = True
            else:
                print("Please, introduce an existing option")
        
if __name__ == '__main__':
    df = extract()
    data = transform(df)
    load(data)