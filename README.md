# README - Processamento de Shapefiles

Este script Python é projetado para processar arquivos Shapefiles (.shp) utilizando a biblioteca `geopandas`. Ele lê o arquivo de entrada, realiza várias operações de processamento, e salva o arquivo Shapefile resultante. O script também normaliza os nomes das colunas e remove colunas específicas conforme necessário.

## Dependências

Certifique-se de que você tem as seguintes bibliotecas instaladas:

- `geopandas`
- `pandas`
- `unidecode`

Você pode instalar essas bibliotecas usando o `pip`:

```bash
pip install geopandas pandas unidecode
```

## Função `processar_shapefile`

A função principal do script é `processar_shapefile`, que executa as seguintes operações:

1. **Leitura do Shapefile**: Carrega o arquivo Shapefile de entrada utilizando `geopandas`.
2. **Exibição Inicial**: Imprime as primeiras linhas dos dados, os nomes das colunas e o sistema de referência de coordenadas (CRS).
3. **Verificação e Definição do CRS**: Se o CRS não estiver definido, o script o define para EPSG:4326.
4. **Normalização dos Nomes das Colunas**: Converte os nomes das colunas para minúsculas e substitui espaços por sublinhados.
5. **Decodificação de Bytes**: Converte colunas de bytes para strings UTF-8, se necessário.
6. **Remoção de Colunas**: Remove colunas especificadas e a coluna "gid" se existir.
7. **Coleta de Informações**: Adiciona informações sobre as colunas ao coletor de informações `coletor_info`.
8. **Salvamento do Shapefile**: Salva o arquivo Shapefile processado no caminho especificado.

### Parâmetros

- `caminho_entrada`: Caminho para o arquivo Shapefile de entrada.
- `caminho_saida`: Caminho onde o arquivo Shapefile processado será salvo.
- `campos_para_excluir`: Lista de colunas a serem excluídas do DataFrame. (opcional)
- `coletor_info`: Lista que coleta informações sobre as variáveis dos Shapefiles.

### Exemplo de Uso

Para processar um Shapefile dos municípios e salvar o resultado em um novo local, você pode usar o código comentado no final do script:

```python
caminho_arquivo_municipios = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\06_Municipios\\01_Shapefile\\02_Original\\BR_Municipios_2022\\BR_Municipios_2022.shp'
caminho_saida_municipios = 'M:\\Carbono\\01_Bases\\01_Administration_and_Economy\\02_Geographic Data\\06_Municipios\\01_Shapefile\\04_Geoserver\\geo_pol_municipios.shp'
processar_shapefile(caminho_arquivo_municipios, caminho_saida_municipios, campos_para_excluir=['campo_a_ser_excluido'], coletor_info=coletor_info)
```

### Observações

- O script inclui um bloco comentado para adicionar uma coluna "fid" se ela não existir. Este bloco está atualmente desativado, mas pode ser ativado se necessário.
- Certifique-se de ajustar os caminhos dos arquivos e os nomes das colunas conforme necessário para seus próprios dados.

## Autor

Francisco de Paula Ribeiro
