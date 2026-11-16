# Relatório de Integridade dos Dados (`dados/extracao.xlsx`)

Verificação executada antes da redação do artigo (sem alterações na planilha original).

## 1. Verificações Estruturais e de Dicionário
- **Total de estudos (linhas na aba `extracao`)**: 29 (esperado: 29).
- **Unicidade de `row_id`**: 29/29 únicos (`[2, 13, 21, 23, 32, 40, 44, 47, 49, 51, 54, 70, 76, 77, 79, 80, 81, 83, 85, 87, 89, 90, 92, 99, 101, 104, 105, 108, 109]`).
- **Rótulos fora do dicionário (`aba dicionario`)**: 0 ocorrências.
- **Alertas automáticos (`aba alertas`)**: 0 linhas.
- **Divergências de auditoria (`aba auditoria`)**: 0 linhas (todos os 1.102 pares estudo×campo nos YAMLs de auditoria constam como `CONCORDA`; não houve dupla extração humana).
- **Pontos de revisão humana (`aba revisao`)**: 138 pontos registrados, com 0 marcados como resolvidos.

## 2. Verificações de Amostra e Classes
- **Soma de `N° por classe` igual a `N° de participantes` (quando ambos preenchidos)**: 0 divergências aritméticas.
- **Divergências semânticas em relação ao tamanho oficial do PADS v1.0.0 (`PD=276; HC=79; DD=114`)**:
  - `row_id=2` (Djemaa et al., 2026): reporta `PD=295; HC=71; DD=103` (soma 469).
  - `row_id=23` (Zannat, 2026): reporta `PD=291; HC=79; DD=99` (soma 469).
  - `row_id=90` (Vu et al., 2026): reporta `PD=276; HC=114; DD=79` na Tabela 1 do artigo (inversão aparente entre HC e DD).
- **Completude de amostra**: 21/29 informam `N° de participantes` e 18/29 detalham `N° por classe`.

## 3. Validação Externa e Múltiplas Bases (Pendência I1)
- **`Papel do PADS = "Validação externa-generalização"` com `Validação externa do Modelo = "Não"`**: `[47]` (`row_id=47`, Abioye et al., 2025, que reaplica o pipeline de ensemble em divisão interna 70/30 de 3 classes do PADS e reporta acurácia de 100% com balanceamento pré-split).
- **Estudos com mais de uma base (`Datasets` multirrótulo) e `Validação externa do Modelo = "Não"`**: 11/29 (`row_id` `[32, 44, 47, 51, 54, 76, 77, 80, 99, 101, 104]`). Todos os 29 estudos constam com `Validação externa do Modelo = "Não"`.

## 4. Fluxo de Seleção e Status de Triagem
- **Totais do fluxo informados pelo autor**: 115 registros importados (`69` citações no Google Scholar + `14` exclusivas da Nature Citations + `15` via snowballing contabilizados no balde Scholar [84] + `17` por string [IEEE Xplore 7, PubMed Central 1, ScienceDirect 3, Scopus 6]) → `24` duplicados → `91` triados → `62` rejeitados → `29` aceitos (`24 + 62 + 29 = 115`).
  - *Nota de conferência*: a verificação `80 + 24 + 29 = 133` não fecha com os `115` importados porque o fluxo consolidado após inclusão dos preprints possui `62` rejeitados (e não `80`), fechando exatamente `24 + 62 + 29 = 115`. Faltam as contagens intermediárias por etapa (título/resumo vs. texto completo) e por critério (CE1–CE6), a data da busca e a data de lançamento do PADS.
- **Distribuição de `aux_status_triagem`**: `{'Aceito': 22, 'Aceito, mas com Ressalvas': 5, 'Aceito, mas com Ressalvas, não confiável': 1, 'Incerto - texto completo': 1}`.
  - Fora dos três rótulos padrão de aceitação: **`row_id=70`** (Varghese et al., 2024, `Incerto - texto completo`, artigo-semente incluído pela Regra 9).
  - Preprints incluídos em desvio consciente ao protocolo (CE2/CI3): 6 estudos (`row_id` 2, 13, 23, 44, 99, 101), sendo `row_id=23` marcado como `"Aceito, mas com Ressalvas, não confiável"`.
  - Uso exclusivo de questionário PDNMS sem sensores IMU: 2 estudos (`row_id=89` e `row_id=108`, sendo `row_id=108` um artigo curto de 2 páginas).

## 5. Anos de Publicação e Outras Inconsistências de Campo
- **`Ano de Publicação` na planilha**: `{2024: 4, 2025: 10, 2026: 15}` (todos entre 2024 e 2026).
  - *Divergência com metadados do Zotero/PDF*: `row_id=79` (Zeebaree & AlFaqi) consta com data `2027-02-28` no Zotero (volume antecipado de 2027, DOI/copyright 2026); `row_id=40` (Zhang et al.) consta como `2025-12-20` no Zotero e `2026, 18:3` no PDF; `row_id=49` (Abola & Jabishvili) consta como `2025-07-01` (`11(3)`) no Zotero/SAGE e `2024, 9(2)` no cabeçalho do PDF.
- **Campos de sensores em estudos IMU**: `row_id=76` possui `Modalidade = Série temporal (IMU)` mas `Sensores` vazio (não especifica acelerômetro/giroscópio); `row_id=101` usa `Sensores = Outro` (`"IMU de 6 canais"`).
- **Análises estatísticas sem avaliação preditiva**: `row_id=49` e `row_id=54` possuem `risco_vazamento = "Não se aplica"`; `row_id=54` não possui cenário de classificação (`QA1`, `QA3`, `QA4` = N/A).
- **`row_id=109` (Lobo et al., 2025)**: embora `Balanceamento = "Só no treino"`, `aux_preproc_apenas_treino = "Não"` devido à seleção iterativa de subconjuntos de atributos sobre o mesmo 5-fold CV, resultando em `risco_vazamento = "Alto"`.
