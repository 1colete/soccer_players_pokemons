import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def EDA_values(df):
    '''
    cria uma tabela com os valores, MINIMO, MAXIMO E MEDIANO das colunas com mais de 23 valores unicos
    caso a tenha menos valores coloca uma lista dos valores
    
    df -> dataframe que será analisado
    
    '''
    print("")
    counter=0
    max_col_name_char = 0
    for col_name in df.columns:
        if len(col_name) > max_col_name_char:
            max_col_name_char = len(col_name)+1
        if len(df.columns) < 10:
            digits = 0
        elif len(df.columns) < 100:
            digits = 1
        else:
            digits = 2
    for i in df.columns:
        if len(df[i].unique()) < 23:
            print(' '*(digits-counter//10), counter, '|', i, ' '*(max_col_name_char - len(i))+'| ',
                  df[i].unique())
        else:
            try:
                print(' '*(digits-counter//10), counter, '|', i,' '*(max_col_name_char - len(i))+'|  '+'Min:', df[i].unique().min(),
                      '| Max:', df[i].unique().max(), '| Avg:',round(df[i].dropna().unique().mean(),2),
                      '| Median:',round(np.median(df[i].dropna().unique()),2))
            except:
                print(' '*(digits-counter//10), counter, '|', i,
                      ' '*(max_col_name_char - len(i))+'|  '+'Min:', df[i].unique().min(), '| Max:',
                      df[i].unique().max())
        counter += 1
    return None

def EDA_graphs(df, disc_cols , cont_cols, target):
    '''
    Plota os graficos do relacionamento da variavel target com as variaveis discretas e continuas
    df -> dataframe que sera analisado
    cont_cols -> lista de colunas continuas
    disc_cols -> lista de colunas discretas
    target -> coluna target
    
    '''
    for col in df.columns:
        if col in disc_cols:
            fig, ax = plt.subplots (1,2, figsize = (15,6))
            fig.suptitle (f'Variavel {col}', fontsize = 20, fontweight = 'bold', y =1)
            sns.countplot(x=col, data=df, ax=ax[0], ec='black')
            ax[0].grid(axis = 'y')
            
            ax[0].set_title(f'Distribuicao de dados {col}')
            
            sns.barplot(x=col, y = target, data = df, ax=ax[1], ec='black', ci = None)
            ax[1].grid(axis = 'y')
            ax[1].set_title(f'{target} em funcao de  {col}')
            plt.show()

        elif col in cont_cols:
            fig, ax = plt.subplots (1,2, figsize = (15,6))
            fig.suptitle (f'Variavel {col}', fontsize = 20, fontweight = 'bold', y =1)
            sns.histplot(x=col, hue=target, data = df, ax=ax[0])
            ax[0].set_title(f'Distribuicao de {col}')
            
            sns.boxplot(x= target, y = col, data = df, ax=ax[1])
            ax[1].set_title(f'Boxplot de {col} em funcao de  {target}')
            plt.show()
            