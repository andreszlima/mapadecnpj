# Script to convert some columns to specific data types
# Will do this to every file in the directory, but segmented by filenames

import os
import pandas as pd


try:
    # Get Cnaes.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Cnaes.csv')
    cnaes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Cnaes.csv'), header=None, encoding='latin-1', delimiter=';')
    cnaes[0] = cnaes[0].astype(int)
    cnaes[1] = cnaes[1].astype(str)
    cnaes.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Cnaes.csv'), index=False, header=False)
    print('Converted file: Cnaes.csv')

    del cnaes

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Cnaes.csv'))
    print('Removed original file: ' + 'Cnaes.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Cnaes.csv')


try:
    # Get all files that have "Empresas" in their name. This dataset doesnt have headers
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'csv')):
        if file.startswith('.'):
            continue
        if file.startswith('parsed_'):
            continue
        if 'Empresas' in file:
            print('Converting file: ' + file)
            df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', file), header=None, encoding='latin-1', delimiter=';')
            df[0] = df[0].astype(str)
            df[1] = df[1].astype(str)
            df[2] = df[2].astype(str)
            # If cannot be cast to int, replace with 0
            df[3] = df[3].fillna(0).astype(int)
            # Replace commas with dots and convert to float
            df[4] = df[4].str.replace(',', '.')
            df[4] = df[4].astype(float)
            df[5] = df[5].astype(str)
            df[6] = df[6].fillna('').astype(str)
            df.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_' + file), index=False, header=False)
            print('Converted ' + file)

            del df

            # Remove the original file after converting
            os.remove(os.path.join(os.path.dirname(__file__), 'csv', file))
            print('Removed original file: ' + file)

except Exception as e:
    print(str(e))
    print('Could not convert file: Empresas.csv')


try:
    # Get all files that have "Estabelecimentos" in their name. This dataset doesnt have headers
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'csv')):
        if file.startswith('.'):
            continue
        if file.startswith('parsed_'):
            continue
        if 'Estabelecimentos' in file:
            print('Converting file: ' + file)
            df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', file), header=None, encoding='latin-1', delimiter=';')
            df[0] = df[0].astype(str).str.pad(8, side='left', fillchar='0')
            df[1] = df[1].astype(str).str.pad(4, side='left', fillchar='0')
            df[2] = df[2].astype(str).str.pad(2, side='left', fillchar='0')
            df[3] = df[3].astype(int)
            df[4] = df[4].fillna('').astype(str)
            df[5] = df[5].astype(int)
            df[6] = df[6].replace('0', pd.NaT)
            df[6] = pd.to_datetime(df[6], format='%Y%m%d', errors='coerce')
            df[7] = df[7].astype(int)
            df[8] = df[8].fillna('').astype(str)
            df[9] = df[9].fillna(0).astype(int)
            df[10] = df[10].replace('0', pd.NaT)
            df[10] = pd.to_datetime(df[10], format='%Y%m%d', errors='coerce')
            df[11] = df[11].astype(int)
            df[12] = df[12].astype(str)
            df[13] = df[13].astype(str)
            df[14] = df[14].astype(str)
            df[15] = df[15].astype(str)
            df[16] = df[16].astype(str)
            df[17] = df[17].astype(str)
            df[18] = df[18].astype(str)
            df[19] = df[19].astype(str)
            df[20] = df[20].astype(int)
            try:
                df[21] = df[21].fillna('').astype(str)
            except:
                df[21] = df[21].replace('**', '').astype(str)
            df[22] = df[22].fillna(0).astype(str)
            try:
                df[23] = df[23].fillna('').astype(str)
            except:
                df[23] = df[23].replace('**', '').astype(str)
            df[24] = df[24].fillna(0).astype(str)
            try:
                df[25] = df[25].fillna('').astype(str)
            except:
                df[25] = df[25].replace('**', '').astype(str)
            df[26] = df[26].fillna(0).astype(str)
            df[27] = df[27].astype(str)
            df[28] = df[28].fillna('').astype(str)
            df[29] = df[29].replace('0', pd.NaT)
            df[29] = pd.to_datetime(df[29], format='%Y%m%d', errors='coerce')
            df.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_' + file), index=False, header=False)
            print('Converted ' + file)

            del df

            # Remove the original file after converting
            os.remove(os.path.join(os.path.dirname(__file__), 'csv', file))
            print('Removed original file: ' + file)

except Exception as e:
    print(str(e))
    print('Could not convert file: Estabelecimentos.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Motivos.csv')
    motivos = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Motivos.csv'), header=None, encoding='latin-1', delimiter=';')
    motivos[0] = motivos[0].astype(int)
    motivos[1] = motivos[1].astype(str)
    motivos.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Motivos.csv'), index=False, header=False)
    print('Converted file: Motivos.csv')

    del motivos

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Motivos.csv'))
    print('Removed original file: ' + 'Motivos.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Motivos.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Municipios.csv')
    municipios = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Municipios.csv'), header=None, encoding='latin-1', delimiter=';')
    municipios[0] = municipios[0].astype(int)
    municipios[1] = municipios[1].astype(str)
    municipios.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Municipios.csv'), index=False, header=False)
    print('Converted file: Municipios.csv')

    del municipios

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Municipios.csv'))
    print('Removed original file: ' + 'Municipios.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Municipios.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Naturezas.csv')
    naturezas = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Naturezas.csv'), header=None, encoding='latin-1', delimiter=';')
    naturezas[0] = naturezas[0].astype(int)
    naturezas[1] = naturezas[1].astype(str)
    naturezas.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Naturezas.csv'), index=False, header=False)
    print('Converted file: Naturezas.csv')

    del naturezas

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Naturezas.csv'))
    print('Removed original file: ' + 'Naturezas.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Naturezas.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Países.csv')
    paises = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Paises.csv'), header=None, encoding='latin-1', delimiter=';')
    paises[0] = paises[0].astype(int)
    paises[1] = paises[1].astype(str)
    paises.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Paises.csv'), index=False, header=False)
    print('Converted file: Paises.csv')

    del paises

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Paises.csv'))
    print('Removed original file: ' + 'Paises.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Paises.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Qualificacoes.csv')
    qualificacoes = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Qualificacoes.csv'), header=None, encoding='latin-1', delimiter=';')
    qualificacoes[0] = qualificacoes[0].astype(int)
    qualificacoes[1] = qualificacoes[1].astype(str)
    qualificacoes.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Qualificacoes.csv'), index=False, header=False)
    print('Converted file: Qualificacoes.csv')

    del qualificacoes

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Qualificacoes.csv'))
    print('Removed original file: ' + 'Qualificacoes.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Qualificacoes.csv')


try:
    # Get Motivos.csv and change its first column from text to int. This dataset doesnt have headers
    print('Converting file: Simples.csv')
    simples = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', 'Simples.csv'), header=None, encoding='latin-1', delimiter=';')
    simples[0] = simples[0].astype(str)
    simples[1] = simples[1].astype(str)
    simples[2] = simples[2].replace('0', pd.NaT)
    simples[2] = pd.to_datetime(simples[2], format='%Y%m%d', errors='coerce')
    simples[3] = simples[3].replace('0', pd.NaT)
    simples[3] = pd.to_datetime(simples[3], format='%Y%m%d', errors='coerce')
    simples[4] = simples[4].astype(str)
    simples[5] = simples[5].replace('0', pd.NaT)
    simples[5] = pd.to_datetime(simples[5], format='%Y%m%d', errors='coerce')
    simples[6] = simples[6].replace('0', pd.NaT)
    simples[6] = pd.to_datetime(simples[6], format='%Y%m%d', errors='coerce')
    simples.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_Simples.csv'), index=False, header=False)
    print('Converted file: Simples.csv')

    del simples

    # Remove the original file after converting
    os.remove(os.path.join(os.path.dirname(__file__), 'csv', 'Simples.csv'))
    print('Removed original file: ' + 'Simples.csv')

except Exception as e:
    print(str(e))
    print('Could not convert file: Simples.csv')


try:
    # Get all files that have "Socios" in their name. This dataset doesnt have headers
    for file in os.listdir(os.path.join(os.path.dirname(__file__), 'csv')):
        if file.startswith('.'):
            continue
        if file.startswith('parsed_'):
            continue
        if 'Socios' in file:
            print('Converting file: ' + file)
            df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'csv', file), header=None, encoding='latin-1', delimiter=';')
            df[0] = df[0].astype(str)
            df[1] = df[1].astype(int)
            df[2] = df[2].astype(str)
            df[3] = df[3].astype(str)
            df[4] = df[4].astype(int)
            df[5] = df[5].replace('0', pd.NaT)
            df[5] = pd.to_datetime(df[5], format='%Y%m%d', errors='coerce')
            df[6] = df[6].fillna(0).astype(int)
            df[7] = df[7].astype(str)
            df[8] = df[8].fillna('').astype(str)
            df[9] = df[9].astype(int)
            df[10] = df[10].astype(int)
            df.to_csv(os.path.join(os.path.dirname(__file__), 'csv', 'parsed_' + file), index=False, header=False)
            print('Converted ' + file)

            del df

            # Remove the original file after converting
            os.remove(os.path.join(os.path.dirname(__file__), 'csv', file))
            print('Removed original file: ' + file)

except Exception as e:
    print(str(e))
    print('Could not convert file: Socios.csv')