
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

# Processar o shapefile do potencial de geração de crédito de carbono redd
# caminho_arquivo_potencial_geracao_credito_carbono_redd = 'M:\\Carbono\\01_Bases\\04_Environment\\06_Land Use and Vegetation Cover\\11_Potencial_Geracao_Credito_de_Carbono\\01_Shapefile\\02_Original\\pol_potencial_geracaoCC_REDDv02.shp'
# caminho_saida_potencial_geracao_credito_carbono_redd = 'M:\\Carbono\\01_Bases\\04_Environment\\06_Land Use and Vegetation Cover\\11_Potencial_Geracao_Credito_de_Carbono\\01_Shapefile\\04_Geoserver\\geo_pol_potencial_credito_carbono_redd.shp'
# processar_shapefile(caminho_arquivo_potencial_geracao_credito_carbono_redd , caminho_saida_potencial_geracao_credito_carbono_redd, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile da area de areas prioritárias
# caminho_arquivo_areas_prioritarias_importancia_biologica = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Habitats\\02_Areas_prioritarias\\01_Shapefile\\01_Manipulado\\04_Unificados\\pol_areas_prioritarias_v01.shp'
# caminho_saida_areas_prioritarias_importancia_biologica = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Habitats\\02_Areas_prioritarias\\01_Shapefile\\04_Geoserver\\geo_pol_areas_prioritarias.shp'
# processar_shapefile(caminho_arquivo_areas_prioritarias_importancia_biologica, caminho_saida_areas_prioritarias_importancia_biologica, campos_para_excluir=['objectid_1', 'objectid', 'nome_area', 'cod_area', 'acao_prin', 'acao_2', 'acao_3', 'shape_leng', 'shape_le_1', 'shape_area', 'acao', 'nome_ap', 'imp', 'prio', 'acprinc', 'ac2', 'ac3', 'acprincnom', 'n', 'id_ap', 'acprincdet', 'ac2det', 'ac3det', 'temaacprin', 'acaoprinc', 'acao2', 'acao3', 'layer', 'path', 'nome', 'estados', 'acao1', 'acao4', 'acaopriori', 'importbio_', 'prioridade', 'fid_1', 'acaoprinci'], coletor_info=coletor_info)

# Processar o shapefile das unidades de conservação
# caminho_arquivo_ucs_consolidadas = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\04_Legally Defined Areas\\01_Unidades_Conservacao\\01_Shapefile\\01_Manipulado\\01_Gerais\\pol_ucs_consolidadas_v00.shp'
# caminho_saida_ucs_consolidadas = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\04_Legally Defined Areas\\01_Unidades_Conservacao\\01_Shapefile\\01_Manipulado\\05_Geoserver\\geo_pol_ucs_consolidadas.shp'
# processar_shapefile(caminho_arquivo_ucs_consolidadas, caminho_saida_ucs_consolidadas, campos_para_excluir=['id_gis', 'ref'], coletor_info=coletor_info)

# Processar o shapefile de queimadas
# caminho_arquivo_queimadas = 'M:\\Carbono\\01_Bases\\04_Environment\\03_Climatology and Climate Change\\01_Queimadas\\01_Shapefile\\01_Manipulado\\QMD_ACUMULADO_MUN\\pol_qmd_mun.shp'
# caminho_saida_queimadas = 'M:\\Carbono\\01_Bases\\04_Environment\\03_Climatology and Climate Change\\01_Queimadas\\01_Shapefile\\04_Geoserver\\geo_pol_queimadas.shp'
# processar_shapefile(caminho_arquivo_queimadas, caminho_saida_queimadas, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de nascente
# caminho_arquivo_nascentes = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\03_Nascentes\\GEOFT_BHO_REF_PONTO_DRENAGEM\\GEOFT_BHO_REF_PONTO_DRENAGEM.shp'
# caminho_saida_nascentes = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\03_Nascentes\\Geoserver\\geo_pto_nascentes.shp'
# processar_shapefile(caminho_arquivo_nascentes, caminho_saida_nascentes, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de biomas
# caminho_arquivo_biomas = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Hable\\02_itats\\05_Biomas\\01_ShapefiOriginal\\Biomas_250mil\\lm_bioma_250.shp'
# caminho_saida_biomas = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Habitats\\05_Biomas\\01_Shapefile\\04_Geoserver\\geo_pol_biomas.shp'
# processar_shapefile(caminho_arquivo_biomas, caminho_saida_biomas, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile da verra
# caminho_arquivo_verra = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\05_Rights and Projects\\01_Projetos_Verra\\01_Shapefile\\01_Manipulado\\06_2024\\pol_dados_consolidados_v00.shp'
# caminho_saida_verra = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\05_Rights and Projects\\01_Projetos_Verra\\01_Shapefile\\04_Geoserver\\geo_pol_verra.shp'
# processar_shapefile(caminho_arquivo_verra, caminho_saida_verra, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de limites dos estados do Brasil
# caminho_arquivo_limites_estados_brasil = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\02_Limites_estados\\01_Shapefile\\02_Original\\UFEBRASIL.shp'
# caminho_saida_limites_estados_brasil = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\02_Limites_estados\\01_Shapefile\\04_Geoserver\\geo_pol_limites_estados_brasil.shp'
# processar_shapefile(caminho_arquivo_limites_estados_brasil, caminho_saida_limites_estados_brasil, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de rodovias estaduais
# caminho_arquivo_rodovias_estaduais = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\02_Original\\GEOFT_TRECHO_RODOVIARIO_ESTADUAL.shp'
# caminho_saida_rodovias_estaduais = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\04_Geoserver\\geo_lin_rodovias_estaduais.shp'
# processar_shapefile(caminho_arquivo_rodovias_estaduais, caminho_saida_rodovias_estaduais, campos_para_excluir=["snv_rdo_co" "shape_lenght"], coletor_info=coletor_info)

# Processar o shapefile de rodovias federais snv
# caminho_arquivo_rodovias_federais_snv  = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\02_Original\\[jun23]_Rodoviario_federal\\rodo_snv.shp'
# caminho_saida_rodovias_federais_snv  = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\04_Geoserver\\geo_lin_rodovias_federais_snv.shp'
# processar_shapefile(caminho_arquivo_rodovias_federais_snv , caminho_saida_rodovias_federais_snv , campos_para_excluir=["vl_br" , "sg_tipo_tr", "vl_codigo", "vl_km_inic", "vl_km_fina", "vl_extensa", "ds_obra", "ds_coinc", "ds_siperfi", "versao_snv", "id_versao", "marcador" , "inline_fid", "simlnflag", "maxsimptol", "minsimptol", "shape_lenght", "ds_superfi"], coletor_info=coletor_info)

# Processar o shapefile de rodovias federais geoft
# caminho_arquivo_rodovias_federais_geoft  = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\02_Original\\[2016]_GEOFT_TRECHO_RODOVIARIO_FEDERAL\\GEOFT_TRECHO_RODOVIARIO_FEDERAL.shp'
# caminho_saida_rodovias_federais_geoft  = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\01_Rodovias\\01_Shapefile\\04_Geoserver\\geo_lin_rodovias_federais_geoft.shp'
# processar_shapefile(caminho_arquivo_rodovias_federais_geoft , caminho_saida_rodovias_federais_geoft , campos_para_excluir=["vl_br" ,"vl_codigo", "desc_coinc", "sg_tipo_tr", "vl_km_inic", "vl_km_fina", "ds_obra", "ds_coinc", "id_versao", "marcador", "ds_superfi"], coletor_info=coletor_info)

# Processar o shapefile de potencial de geração de crédito de carbono CC
# caminho_arquivo_potencial_carbono  = 'M:\\Carbono\\01_Bases\\04_Environment\\06_Land Use and Vegetation Cover\\11_Potencial_Geracao_Credito_de_Carbono\\01_Shapefile\\02_Original\\pol_potencial_geracaoCC_v01.shp'
# caminho_saida_potencial_carbono   = 'M:\\Carbono\\01_Bases\\04_Environment\\06_Land Use and Vegetation Cover\\11_Potencial_Geracao_Credito_de_Carbono\\01_Shapefile\\04_Geoserver\\geo_pol_potencial_credito_carbono_cc.shp'
# processar_shapefile(caminho_arquivo_potencial_carbono  , caminho_saida_potencial_carbono, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de embargos
# caminho_arquivo_embargos  = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\03_Legal Penalty\\01_Embargos_Infracoes\\01_Shapefile\\02_Original\\06_2024\\adm_embargo_ibama_a.shp'
# caminho_saida_embargos   = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\03_Legal Penalty\\01_Embargos_Infracoes\\01_Shapefile\\04_Geoserver\\geo_pol_embargos.shp'
# processar_shapefile(caminho_arquivo_embargos, caminho_saida_embargos, campos_para_excluir=["serie_tad", "dat_embarg", "dat_impres", "num_long_1", "num_lat_1", "dat_ult_1", "wkt_code" "cpf_cnpj_s", "cpf_cnpj_c", "qt_area_d", "des_tipo_b" , "nom_operac", "dat_ult_1", "sit_desemb", "dat_desemb", "termo", "sit_termo", "tipo_pesso", "enquadra_1", "enquadra_2", "wkt_code", "des_auto_i", "tipo_infra", "cpf_agente", "nom_autuan", "origem_reg", "codigo_ori"], coletor_info=coletor_info)

# Processar o shapefile de infrações
# caminho_arquivo_infracoes  = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\03_Legal Penalty\\01_Embargos_Infracoes\\01_Shapefile\\01_Manipulado\\pto_infracoes_v00.shp'
# caminho_saida_infracoes   = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\03_Legal Penalty\\01_Embargos_Infracoes\\01_Shapefile\\04_Geoserver\\geo_pto_infracoes.shp'
# processar_shapefile(caminho_arquivo_infracoes, caminho_saida_infracoes, campos_para_excluir=["seq_notifi", "cod_unidad", "seq_infrac", "seq_unidad", "cod_unid_1", "qtd_area_d", "seq_tipo_a", "cod_status", "seq_operac", "sit_public", "des_justif", "seq_tipo_o", "seq_ocorre", "dat_cienci", "dat_primei", "dat_transi", "dat_segund", "dat_tercei","seq_acao_f","forma_entr", "patrimonio", "patrimon_1", "gravidade", "num_boleto", "des_outros", "dat_publiv", "sit_publi_1", "sit_public"], coletor_info=coletor_info)

# Processar o shapefile de aeroportos
# caminho_arquivo_aeroportos  = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\04_Aeroportos\\01_Shapefile\\02_Original\\aeroportos\\fc_aero_aerodromos_publicos.shp'
# caminho_saida_aeroportos   = 'M:\\Carbono\\01_Bases\\05_Infrastructure\\02_Transport and Logistics\\04_Aeroportos\\01_Shapefile\\04_Geoserver\\geo_pto_aeroportos.shp'
# processar_shapefile(caminho_arquivo_aeroportos, caminho_saida_aeroportos, campos_para_excluir=["ciad", "municíp_1", "ufservido", "latgeopoin", "longeopon", "longeopoin", "altitude", "operaç_1" , "designa_1", "designa_12", "largura", "designa_13", "designa_14" , "designa_15", "comprime_1", "largura2" , "resistê_", "superfí_1", "superfí_1", "resiste_1", "rodadas" , "rodadas_co"], coletor_info=coletor_info)

# Processar o shapefile de zonas utm
# caminho_arquivo_zonas_utm = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\03_Zonas_UTM\\01_Shapefile\\02_Original\\Fusos_alternativo\\Zonas_UTM.shp'
# caminho_saida_zonas_utm = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\03_Zonas_UTM\\01_Shapefile\\04_Geoserver\\geo_pol_zonas_utm.shp'
# processar_shapefile(caminho_arquivo_zonas_utm, caminho_saida_zonas_utm, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)

# Processar o shapefile de direito minerario (Via QGIS)
# caminho_arquivo_direito_minerario = 'M:\\Carbono\\01_Bases\\06_Mining\\01_Available areas for mining\\01_Direito_minerario\\01_Shapefile\\02_Original\\05_24\\BRASIL.shp'                             
# caminho_saida_direito_minerario = 'M:\\Carbono\\01_Bases\\06_Mining\\01_Available areas for mining\\01_Direito_minerario\\01_Shapefile\\04_Geoserver\\geo_pol_direito_minerario.shp'
# processar_shapefile(caminho_arquivo_direito_minerario, caminho_saida_direito_minerario, campos_para_excluir=['numero', 'ano'], coletor_info=coletor_info)

# Processar o shapefile de cavidades
# caminho_arquivo_cavidades = 'M:\\Carbono\\01_Bases\\04_Environment\\02_Geology and Soil\\02_Cavidades\\01_Shapefile\\02_Original\\06_2024\\cav_canie_geral123_19122022.shp'
# caminho_saida_cavidades = 'M:\\Carbono\\01_Bases\\04_Environment\\02_Geology and Soil\\02_Cavidades\\01_Shapefile\\04_Geoserver\\geo_pto_cavidades.shp'
# processar_shapefile(caminho_arquivo_cavidades, caminho_saida_cavidades, campos_para_excluir=["grau_de_re", "gps", "errogps", "qtd__satel", "qtd_satel", "litotipo", "desenvolvi", "projecao", "projeção", "altitude", "desnivel_f"], coletor_info=coletor_info)

# Processar o shapefile de sitios arqueoçogicos
# caminho_arquivo_sitios_arqueologicos = 'M:\\Carbono\\01_Bases\\02_Archaeology\\01_Archaeological Sites and Artifacts\\01_Sitios_arqueologicos\\01_Shapefile\\01_Manipulado\\pto_sitios_v00.shp'
# caminho_saida_sitios_arqueologicos = 'M:\\Carbono\\01_Bases\\02_Archaeology\\01_Archaeological Sites and Artifacts\\01_Sitios_arqueologicos\\01_Shapefile\\04_Geoserver\\geo_pto_sitios_arqueologicos.shp'
# processar_shapefile(caminho_arquivo_sitios_arqueologicos, caminho_saida_sitios_arqueologicos, campos_para_excluir=["no_logrado" , "nu_logrado"], coletor_info=coletor_info)

# Processar o shapefile de hidrografia (Campos deletados postgres)
# caminho_arquivo_hidrografia = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\01_Curso_d_agua\\GEOFT_BHO_REF_RIO.shp'
# caminho_saida_hidrografia = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\06_Geoserver\\geo_pol_hidrografia.shp'
# processar_shapefile(caminho_arquivo_hidrografia, caminho_saida_hidrografia, campos_para_excluir=["campo_a_ser_excluido"], coletor_info=coletor_info)

# Processar o shapefile de massa d agua (Campos deletados postgres)
# caminho_arquivo_massa_d_agua = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\01_Curso_d_agua\\geoft_bho_massa_dagua_v2019.shp'
# caminho_saida_massa_d_agua = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\06_Geoserver\\geo_pol_massa_d_agua.shp'
# processar_shapefile(caminho_arquivo_massa_d_agua, caminho_saida_massa_d_agua, campos_para_excluir=["gid" , "esp_cd" , "cod_snisb" , "cod_sar" , "nm_ligacao" ,  "nuperimkm" , "numareakm2" , "nuareaha" , "nucompgeom" , "Salinidade" , "nmriocomp" , "desatelite" , "deversao" , "nuvzreg" , "nuvzlago", "nuvzflu" , "cdtipooper" , "detipooper", "fovzlago" , "fovzdeflu", "fovzreg", "cobarprin" , "cotrecho" , "nuvzrecebe", "nuvztransf" , "deobsvazao" , "cocda2013" , "cocda2017"], coletor_info=coletor_info)

# Processar o shapefile de bacias hidrograficas
# caminho_arquivo_bacias_hidrograficas = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\02_Bacias\\02_Sub_bacias_Principais\\micro_RH\\micro_RH.shp'
# caminho_saida_bacias_hidrograficas = 'M:\\Carbono\\01_Bases\\04_Environment\\05_Hydrography and Water Resources\\01_Hidrografia\\01_Shapefile\\02_Original\\02_Bacias\\04_Geoserver\\geo_pol_bacias_hidrograficas.shp'
# processar_shapefile(caminho_arquivo_bacias_hidrograficas, caminho_saida_bacias_hidrograficas, campos_para_excluir=["campo_a_ser_excluido"], coletor_info=coletor_info)

# Processar o shapefile de pedologia
# caminho_arquivo_pedologia = 'M:\\Carbono\\01_Bases\\04_Environment\\02_Geology and Soil\\01_Pedologia\\01_Shapefile\\02_Original\\pedo_area\\pedo_area.shp'
# caminho_saida_pedologia = 'M:\\Carbono\\01_Bases\\04_Environment\\02_Geology and Soil\\01_Pedologia\\01_Shapefile\\04_Geoserver\\geo_pol_pedologia.shp'
# processar_shapefile(caminho_arquivo_pedologia, caminho_saida_pedologia, campos_para_excluir=["cd_fcim", "nom_unidad", "val_ncompo" , "erosão" , "pedregosid" , "rochosidad", "component1", "component2", "component3", "inclu_p1" , "inclu_p2", "inclu_p3", "leg_ordem", "legenda_2", "cd_ord_id", "cd_leg2_id"], coletor_info=coletor_info)

# Processar o shapefile de centrais geradoras hidrelétricas CGH
# caminho_arquivo_centrais_geradoras_hidreletricas = 'M:\\Carbono\\01_Bases\\03_Energy\\02_Renewable Energy\\01_Hidreletricas\\01_Shapefile\\02_Original\\06_2024\\Aproveitamento_Hidrelétricos_-_AHE.shp'
# caminho_saida_centrais_geradoras_hidreletricas = 'M:\\Carbono\\01_Bases\\03_Energy\\02_Renewable Energy\\01_Hidreletricas\\01_Shapefile\\04_Geoservergeo_pol_aproveitamento_hidreletricos_ahe.shp'
# processar_shapefile(caminho_arquivo_centrais_geradoras_hidreletricas, caminho_saida_centrais_geradoras_hidreletricas, campos_para_excluir=["munic_cf" , "uf_cf", "munic_2" , "uf_2", "lat_eixo_g" , "long_eixo_" , "lat_cf_gms" , "long_cf_gm" , "rend_nom_t" , "rend_nom_g" , "tx_eq_inds" , "inds_prog" , "perd_hid_n" , "na_max_max" , "na_max_mon" , "na_min_mon" , "na_nor_jus" , "area_na_ma" , "area_na_mi" , "lat_eixo_d", "long_eixo1" , "reg_mens" , "rn_696_15" , "tpo", "tipo_ahe"], coletor_info=coletor_info)

# Processar o shapefile de aproveitamento eletrico
# caminho_arquivo_aproveitamento_eletrico = 'M:\\Carbono\\01_Bases\\03_Energy\\02_Renewable Energy\\01_Hidreletricas\\01_Shapefile\\02_Original\\06_2024\\Centrais_Geradoras_Hidrelétricas-CGH.shp'
# caminho_saida_aproveitamento_eletrico = 'M:\\Carbono\\01_Bases\\03_Energy\\02_Renewable Energy\\01_Hidreletricas\\01_Shapefile\\04_Geoserver\\geo_pol_centrais_geradoras_hidreletricas_ahe.shp'
# processar_shapefile(caminho_arquivo_aproveitamento_eletrico, caminho_saida_aproveitamento_eletrico, campos_para_excluir=["munic_cf" , "uf_cf" , "munic_2" , "uf_2", "lat_eixo_g" , "long_eixo_" , "lat_cf_gms" , "long_cf_gm", "rend_nom_t" , "rend_nom_g" , "tx_eq_inds" , "inds_prog" , "perd_hid_n" , "na_max_max" , "na_max_mon" , "na_min_mon" , "na_nor_jus" , "area_na_ma" , "area_na_mi" , "lat_eixo_d", "long_eixo1" , "reg_mens" , "rn_696_15" , "tpo", "tipo_ahe"], coletor_info=coletor_info)

# Processar o shapefile de especies ameacadas
# caminho_arquivo_especies_ameacadas = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Habitats\\03_Especies_ameacadas\\01_Shapefile\\01_Manipulado\\03_Brasil_06_24\\pto_esp_ameacadas_v01.shp'
# caminho_saida_especies_ameacadas = 'M:\\Carbono\\01_Bases\\04_Environment\\04_Species and Habitats\\03_Especies_ameacadas\\01_Shapefile\\01_Manipulado\\02_Geoserver\\geo_pto_especies_ameacadas.shp'
# processar_shapefile(caminho_arquivo_especies_ameacadas, caminho_saida_especies_ameacadas, campos_para_excluir=["campo_a_ser_excluido"], coletor_info=coletor_info)

# Processar o shapefile de certificadora tero
# caminho_arquivo_certificadora_tero = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\05_Rights and Projects\\04_Projetos_Tero\\01_Shapefile\\01_Manipulado\\pol_tero_unificados_v00.shp'
# caminho_saida_certificadora_tero = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\05_Rights and Projects\\04_Projetos_Tero\\01_Shapefile\\04_Geoserver\\geo_pol_certificadora_tero.shp'
# processar_shapefile(caminho_arquivo_certificadora_tero, caminho_saida_certificadora_tero, campos_para_excluir=["campo_a_ser_excluido"], coletor_info=coletor_info)

# Salvar as informações coletadas em um arquivo Excel
# df_info = pd.DataFrame(coletor_info, columns=['Variavel', 'Shapefile'])
# caminho_arquivo_excel = 'C:\\Users\\RibeiroF\\OneDrive - AECOM\\Francisco\\Área de Trabalho\\Atividades\\Carbono\\Shapes Ajustados\\variaveis_shapefiles.xlsx'
# df_info.to_excel(caminho_arquivo_excel, index=False)
