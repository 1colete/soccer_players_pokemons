import pandas as pd
import unidecode
from sklearn.preprocessing import MinMaxScaler

def linhas_duplicadas(df):
    '''
    recebe um df e retorna a quandidade de linhas duplicadas
    '''
    # Linhas duplicadas
    if df.shape[0] != df.drop_duplicates().shape[0]:
        n_linhas_duplicadas = df.shape[0] - df.drop_duplicates().shape[0]
        print(f'Existem {n_linhas_duplicadas} linhas duplicadas')
    else:
        print('Não há linhas duplicadas no conjunto de dados.')
    return None

def colunas_duplicadas(df):
    '''
    recebe um df e retorna a quandidade de colunas duplicadas
    '''
    # Colunas duplicadas
    colunas_duplicadas = []
    for col1 in df.columns.tolist():
        for col2 in df.columns.tolist():
            if col1 != col2:
                if (df[col1] == df[col2]).all():
                    colunas_duplicadas.append([col1, col2])

    if len(colunas_duplicadas) > 0:
        print('Colunas duplicadas:', colunas_duplicadas)
    else:
        print('Não há colunas duplicadas no conjunto de dados.')
    return None

def colunas_constantes(df):
    '''
    recebe um dataframe e dropa as colunas que são constantes
    '''
    # Colunas constantes
    colunas_constantes = []
    for col in df.columns.tolist():
        if df[col].nunique() == 1:
            colunas_constantes.append(col)

    if len(colunas_constantes) > 0:
        print('Colunas constantes:', colunas_constantes)
        df.drop(colunas_constantes, axis=1, inplace=True)
    else:
        print('Não há colunas constantes no conjunto de dados.')
    return None

def identify_cols_low_variance(df, low_variance_threshold):
    '''
    recebe um df
    retorna uma lista de colunas com baixa variancia
    -
    df - > dataframe a ser analisado
    low_variance_threshold -> 0.001 (indicado)
    '''
    # Inicializa scaler
    scaler = MinMaxScaler()
    # Seleciona apenas variáveis numéricas
    df_numericas = df.select_dtypes(exclude=['object'])
    # Faz scaling das variáveis
    df_scaled = pd.DataFrame(
        scaler.fit_transform(df_numericas),
        columns=df_numericas.columns
    )
    
    colunas_baixa_variancia = []
    for col in df_scaled.columns:
        if df_scaled[col].var() < low_variance_threshold:
            colunas_baixa_variancia.append(col)
            
    return colunas_baixa_variancia

def checa_nulos(df):
    '''
    recebe um dataframe e retorna a porcentagem de nulos em cada uma das colunas
    '''
    # Checando colunas com nulos
    coluna_nulos = pd.Series(df.isnull().sum(), name='nulos')

    coluna_nulosperc = pd.Series(100 * (df.isnull().sum()/ df.shape[0]), name='%')

    df_nulos = pd.merge(coluna_nulos, coluna_nulosperc, right_index = True,
                left_index = True).round(2)
    return df_nulos


def corrigir_nomes(nome):
    """ Remove todos a a acentuação e deixa a string em minúscula

    Args:
        nome (str): nome que será manipulado
    """

    nome = unidecode.unidecode(nome).lower()
    return nome