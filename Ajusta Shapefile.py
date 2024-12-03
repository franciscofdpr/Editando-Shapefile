
import geopandas as gpd
import pandas as pd
from unidecode import unidecode

# Função para processar o shapefile
def processar_shapefile(caminho_entrada, caminho_saida, campos_para_excluir, coletor_info):

    # Ler o shapefile
    dados = gpd.read_file(caminho_entrada)
    print(dados.head())
    
    # Imprimir nomes das colunas e CRS
    print(dados.columns)
    print(dados.crs)
    
     # Verificar se o CRS está definido, caso contrário, definir para EPSG:4326
    if dados.crs is None:
        dados.set_crs('EPSG:4326', inplace=True)
    
    # Converte CRS para EPSG:4326
    dados = dados.to_crs('EPSG:4326')
    
    # Normaliza nomes das colunas (Coloca em minusculo e substitui espaço por "_")
    dados.columns = [unidecode(col).replace(' ', '_').lower() for col in dados.columns]

    # Converter colunas de bytes para strings e econding para utf-8
    for col in dados.columns:
        if dados[col].dtype == 'object':
           if any(isinstance(val, bytes) for val in dados[col]):
               dados[col] = dados[col].apply(lambda x: x.decode('utf-8') if isinstance(x, bytes) else x)

    # Transformar cria "fid" se não existir
    # if 'fid' not in dados.columns:
    #     dados.insert(0, 'fid', range(1, len(dados) + 1))
    # else:
    #     # Reposicionar a coluna 'fid' para ser a primeira
    #     cols = list(dados.columns)
    #     cols.insert(0, cols.pop(cols.index('fid')))
    #     dados = dados[cols]
    
    print(dados.columns)

    # Adicionar informações das colunas ao coletor_info
    for col in dados.columns:
        coletor_info.append([col, caminho_entrada])

    # Excluir campos especificados
    if campos_para_excluir:
        dados = dados.drop(columns=campos_para_excluir, errors='ignore')

    # Excluir campos com o nome "gid"
    if 'gid' in dados.columns:
        dados = dados.drop(columns=['gid'], errors='ignore')
    
    print(dados.columns)
    
    # Salvar o shapefile processado
    dados.to_file(caminho_saida, encoding='utf-8')

# Lista para coletar informações sobre as variáveis dos shapefiles
coletor_info = []

# Processar o shapefile dos municípios
# caminho_arquivo_municipios = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\06_Municipios\\01_Shapefile\\02_Original\\BR_Municipios_2022\\BR_Municipios_2022.shp'
# caminho_saida_municipios = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\06_Municipios\\01_Shapefile\\04_Geoserver\\geo_pol_municipios.shp'
# processar_shapefile(caminho_arquivo_municipios, caminho_saida_municipios, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile das comunidades quilombolas
# caminho_arquivo_areas_quilombolas = 'M:\\Carbono\\01_Bases\\07_Social\\02_Lands and Communities\\03_Comunidades_Quilombolas\\01_Shapefile\\02_Original\\Area_de_Quilombolas\\areas_quilombolas.shp'
# caminho_saida_areas_quilombolas = 'M:\\Carbono\\01_Bases\\07_Social\\02_Lands and Communities\\03_Comunidades_Quilombolas\\01_Shapefile\\04_Geoserver\\geo_pol_areas_quilombolas.shp'
# processar_shapefile(caminho_arquivo_areas_quilombolas , caminho_saida_areas_quilombolas, campos_para_excluir=['cd_quilomb','dt_publica','nr_area_ha','nr_perimet','ob_descric','st_titulad','dt_decreto','tp_levanta','nr_escalao,perimetro_'], coletor_info=coletor_info)

# Processar o shapefile das terras indigenas
# caminho_arquivo_terras_indigenas = 'M:\\Carbono\\01_Bases\\07_Social\\02_Lands and Communities\\01_Terras_indigenas\\01_Shapefile\\02_Original\\tis_poligonais_portariasPolygon\\tis_poligonais_portariasPolygon.shp'
# caminho_saida_terras_indigenas = 'M:\\Carbono\\01_Bases\\07_Social\\02_Lands and Communities\\01_Terras_indigenas\\01_Shapefile\\04_Geoserver\\geo_pol_terras_indigenas.shp'
# processar_shapefile(caminho_arquivo_terras_indigenas, caminho_saida_terras_indigenas, campos_para_excluir=['superficie','reestudo_t','faixa_fron','data_em_es','tit_em_est','data_delim','tit_delimi','data_decla','tit_declar','data_homol','tit_homolo','res_em_est','res_delimi','res_declar','res_homolo','res_regula','undadm_cod','fillcolor','fillopacit','strokecolo','strokeopac','strokewidt'], coletor_info=coletor_info)

# Salvar as informações coletadas em um arquivo Excel
# df_info = pd.DataFrame(coletor_info, columns=['Variavel', 'Shapefile'])
# caminho_arquivo_excel = 'C:\\Users\\RibeiroF\\OneDrive - AECOM\\Francisco\\Área de Trabalho\\Atividades\\Carbono\\Shapes Ajustados\\variaveis_shapefiles.xlsx'
# df_info.to_excel(caminho_arquivo_excel, index=False)
