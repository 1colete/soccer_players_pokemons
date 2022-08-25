import pandas as pd
import numpy as np
from scipy import stats

def cramer_v(df, cat_cols):
    """Recebe um dataframe e colunas categoricas e aplica o V de Cramer retornando a interferencia das variaveis categoricas na variavel target.

    Args:
        df (dataframe): dataframe que sera aplicado o V de cramer
        cat_cols (list): Lista de colunas categoricas

    Returns:
        dataframe: Retorna um dataframe com o percentual de influencia da variavel categorica na target.
    """
    df=df
    cat_cols=cat_cols
    # dicionário para guardar o cramer V de cada coluna em relação às demais
    dict_cramer = {}
    # primeiro for loop é para percorrer as colunas categóricas
    for cat in cat_cols:
        # lista para guardar os valores obtidos de cramer v a cada coluna 
        cramer_v_list = []
        # segundo for loop é para percorrer para uma variável categórica todas as colunas do dataframe
        for cat_ in cat_cols:
            # gerando a tabela de contingência
            df_cross = pd.crosstab(df[cat], df[cat_])
            # extraindo o valor de chi2
            chi2_teste, p, df_, arr = stats.chi2_contingency(df_cross)
            # calculando o número de linhas
            r = len(df_cross)
            # calculando o número de colunas
            c = len(df_cross.columns)
            # calculando a soma dos elementos das células
            n = df_cross.to_numpy().sum()
            # calculando o V de cramer
            V = np.sqrt((chi2_teste/(n*(np.min([r,c]) -1))))
            # appendando o resultado na lista
            cramer_v_list.append(V)
        # salvando para um elemento do dicionário a lista contendo os V de cramer correspondentes
        dict_cramer[cat] = cramer_v_list
        # criando dataframe a partir do dicionário
        df_v_cramer = pd.DataFrame(dict_cramer)
        # adicionando o índice com o nome das variáveis
        df_v_cramer.index=cat_cols
    return df_v_cramer