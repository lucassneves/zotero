# Relatório Final (v2 Consolidada — Análise com Texto Completo via Zotero Storage + Nature Citations)

## Objetivo
Expandir e consolidar a triagem sistemática rápida (*Rapid Review*) sobre estudos que utilizam o dataset **PADS** (*Parkinson's Disease Smartwatch dataset*, Varghese et al.), unificando os registros de [articles com Snowballing.xls](file:///c:/Users/lucas.sneves/Zotero/Relat%C3%B3rio%20anal%C3%ADtico/articles%20com%20Snowballing.xls) e [articles com Snowballing - Nature.xlsx](file:///c:/Users/lucas.sneves/Zotero/Relat%C3%B3rio%20anal%C3%ADtico/articles%20com%20Snowballing%20-%20Nature.xlsx) — com o ajuste de reclassificação de +3 artigos (`row_id` 103, 111 e 113) para `(Manual) Google Scholar` (passando de 81 para **84** em Google Scholar e de 98 para **101** no conjunto Base + Scholar) e −3 artigos em `(Manual) Nature Citations` (passando de 17 para **14** registros) — totalizando **115 artigos** (`row_id` 1 a 115), com verificação integral nos textos completos da pasta `storage` do Zotero a partir da coluna `Key in zotero`.

Entregáveis atualizados:
- Planilha principal (115 registros): [triagem_resultado.xlsx](file:///c:/Users/lucas.sneves/Zotero/Relat%C3%B3rio%20anal%C3%ADtico/triagem_resultado.xlsx)
- Cópia sincronizada na raiz: [triagem_resultado.xlsx](file:///c:/Users/lucas.sneves/Zotero/triagem_resultado.xlsx)
- Relatório analítico e handoff: [relatório_final.md](file:///c:/Users/lucas.sneves/Zotero/Relat%C3%B3rio%20anal%C3%ADtico/relat%C3%B3rio_final.md) e [relatório_final.md](file:///c:/Users/lucas.sneves/Zotero/relat%C3%B3rio_final.md)

---

## Passos Executados
1. **Unificação preservando metadados originais e ajuste de `source` (+3 Google Scholar / −3 Nature Citations)**:
   - Carregamento das duas planilhas (`115` linhas no total) via `pandas.read_excel`, preservando intactas as 26 colunas originais e atribuindo `row_id` sequencial de `1` a `115` como primeira coluna.
   - Reclassificação de `source` de `(Manual) Nature Citations` para `(Manual) Google Scholar` nos 3 registros solicitados (`row_id` **103** / `H29I8TDV`, `row_id` **111** / `JS893BZF` e `row_id` **113** / `3BL7E3ZZ`), resultando em **84 artigos** em `(Manual) Google Scholar` (**101 artigos** somando o lote base `1–98` + os 3 reclassificados) e **14 artigos** em `(Manual) Nature Citations`.
2. **Verificação cruzada de duplicatas (`CE4`)**: comparação exata e normalizada de `doi`, `title` e `Key in zotero` entre todos os 115 registros, confirmando **zero duplicatas** entre os 17 registros adicionados (`row_id` 99–115) e os 98 registros originais (`row_id` 1–98), bem como zero duplicatas internas entre `row_id` 99–115.
3. **Mapeamento `Key in zotero` → `storage` e leitura do texto completo**:
   - Nos 101 registros do conjunto Base + 3 reclassificados para Google Scholar (`row_id` 1–98, 103, 111 e 113): **99 de 101** possuem PDF e cache de texto completo (`.zotero-ft-cache`) em `C:\Users\lucas.sneves\Zotero\storage` (**CE5 = "Não"**); apenas 2 registros (`row_id` 33 e 55) não possuem PDF (**CE5 = "Sim"**).
   - Nos 14 registros de `(Manual) Nature Citations` (`row_id` 99–102, 104–110, 112, 114 e 115): **12 de 14** possuem subpasta e PDF integral diretamente em `C:\Users\lucas.sneves\Zotero\storage\<Key in zotero>` (**CE5 = "Não"**); apenas **2 capítulos de livro da Springer** (`row_id` 110 e `row_id` 115) têm `Key in zotero` vazio e não possuem PDF em `storage` (**CE5 = "Sim"**).
   - No total consolidado: **111 de 115 registros (96,5%)** tiveram o texto completo inspecionado.
4. **Aplicação literal dos critérios de inclusão (CI1–CI4), exclusão (CE1–CE6) e extração das Questões de Pesquisa (QP1–QP5)** com enriquecimento a partir do texto completo (identificado pela tag `[Texto completo]`).
5. **Geração da planilha `.xlsx` com `openpyxl`, execução das 5 verificações obrigatórias e remoção imediata de scripts/arquivos temporários**.

---

## Resultado Geral Consolidado (115 Artigos)

| Decisao_IA | Conjunto Base + 3 Scholar (`n = 101`)* | `(Manual) Nature Citations` (`n = 14`)** | Total Consolidado (`1–115`) |
|---|---:|---:|---:|
| **Aceito** | 18 | **4** | **22** |
| **Rejeitado** | 81 *(78 + 3)* | **10** *(13 − 3)* | **91** |
| **Incerto - texto completo** | 2 | **0** | **2** |
| **Total** | **101** *(98 + 3)* | **14** *(17 − 3)* | **115** |

*\*Nota 1: o conjunto de 101 artigos compreende os 98 artigos originais (`row_id` 1–98) mais os 3 artigos reclassificados para `(Manual) Google Scholar` (`row_id` 103, 111 e 113, todos Rejeitados por CI1/CE1).*
*\*\*Nota 2: o conjunto `(Manual) Nature Citations` compreende exatamente os 14 artigos restantes da segunda planilha (`row_id` 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 114 e 115).*

### Síntese da Triagem de `(Manual) Nature Citations` (14 Artigos) e dos 3 Reclassificados para `(Manual) Google Scholar`
- **4 Artigos "Aceitos" em `(Manual) Nature Citations` (`CI1 = Atende`, revisão por pares confirmada, todos os `CE = Não`)**:
  - **`row_id` 104** (`storage/6ALP5R4U`, Haque et al., 2026, *Information Fusion*): propõe o framework **Eco-xPD** com adaptação de domínio relacional cruzada (**xReDA**), transferindo conhecimento de neuroimagem (DaTscan) durante o treino para sensores de baixo custo na inferência; na modalidade smartwatch, avalia o **PADS** (355 sujeitos: 276 PD vs 79 HC, 11 tarefas), alcançando **Acc 89,92% ± 2,02%** e **F1 93,60% ± 1,03%**.
  - **`row_id` 105** (`storage/RD5LYQ4W`, Padilha et al., 2025, *Anais da ERI-GO / SBC*, pp. 175–184, em português): artigo completo de conferência (10 páginas) que extrai **8 características harmônicas via FFT** (495 atributos/sujeito) dos sinais de giroscópio do **PADS** (469 sujeitos: 276 DP, 79 CO, 114 DD) e avalia SVM, Extra Trees, LightGBM e XGBoost em três cenários (DP vs CO: Acc 84,05%, BalAcc 68,33%; DP vs DD: Acc 73,52%, BalAcc 60,26%; e o cenário inédito DD vs CO: Acc 74,64%, BalAcc 73,43%).
  - **`row_id` 108** (`storage/HEUSS8MW`, Padilha, Felix & Salvini, 2024, *Anais da ERI-GO / SBC*, pp. 251–252, em inglês): avalia SVM linear e Random Forest em amostra estratificada de 234 participantes do **PADS** (82 PD, 82 DD, 70 HC) utilizando **exclusivamente o questionário de 30 sintomas não motores** (HC vs PD: BalAcc 87%; DD vs PD: BalAcc 75%). Mantido como `Aceito` com alerta obrigatório da **Regra 8 (`usa PADS sem dados de sensor`)** e alerta de extensão (`pp. 251-252`).
  - **`row_id` 109** (`storage/S399Z5MS`, Lobo et al., 2025, *Anais da ERI-GO / SBC*, pp. 344–347, em inglês): extrai **924 atributos estatísticos temporais** (eixos X, Y, Z e magnitude M de acelerômetro e giroscópio) dos 469 participantes do **PADS** com balanceamento SMOTE e classificadores baseados em árvores (Random Forest, Extra Trees, XGBoost e LightGBM), obtendo BalAcc de 74,31% (PD×CO com LightGBM), 67,37% (PD×DD com LightGBM) e 82,48% (DD×CO com Extra Trees).
- **10 Artigos "Rejeitados" em `(Manual) Nature Citations`**:
  - **2 Preprints que USAM o PADS (`CI1 = Atende`), mas foram "Rejeitados" por `CE2 = Sim` (`CI3 = Não atende`)**:
    - **`row_id` 99** (`storage/WBUNUL6I`, Win et al., 2026, *JMIR Preprints*, `10.2196/preprints.109459`): retreina e valida seu modelo *Conv1D-BiLSTM* no **PADS** (355 participantes: 276 PD, 79 HC; ROC AUC 0,8417 em *Rest Tremor* e 0,8384 em *Postural Tremor*), mas é um preprint (*JMIR Preprints*).
    - **`row_id` 101** (`storage/DUU5E6Q5`, *SGC-RML*, 2026, *arXiv*, `10.48550/ARXIV.2605.08302`): valida o framework *SGC-RML* (*PatchTST* + roteamento seletivo de 4 ações e calibração conformal) nos 469 sujeitos do **PADS** (AUC 0,805 em CV 5-fold de 419 sujeitos e AUC 0,825 na coorte cega de 50 sujeitos), mas é um preprint do *arXiv*.
  - **3 Rejeitados por Literatura Cinza / Capítulo de Livro (`CE2 = Sim`) que também não usam PADS**:
    - **`row_id` 107** (`storage/NRWZU92C`, preprint no *Research Square* que usa *UCI Telemonitoring Voice Dataset*).
    - **`row_id` 110** (capítulo de livro da *Springer*, sem PDF em `storage`, que usa dataset de voz de 31 indivíduos).
    - **`row_id` 115** (capítulo de livro de revisão da *Springer*, sem PDF em `storage`, `CE2 = Sim` e `CE3 = Sim`).
  - **5 Rejeitados em `(Manual) Nature Citations` por não usarem o PADS (`CI1 = Não atende`, `CE1 = Sim`)**:
    - **`row_id` 100** (`storage/WBV9MMNA`, apresenta o aplicativo *MoveMetrics*), **`row_id` 102** (`storage/Q9KW9SLD`, usa *ALAMEDA PD tremor dataset*), **`row_id` 106** (`storage/EQ526NS9`, usa *PhysioNet Gait* e *UCI Voice*), **`row_id` 112** (`storage/FSJL799I`, sensores neurais invasivos em roedores/primata) e **`row_id` 114** (`storage/QLU5A3PI`, usa dados de voz com Otimização por Colônia de Formigas).
- **3 Artigos Reclassificados para `(Manual) Google Scholar` ("Rejeitados" por `CI1 = Não atende`, `CE1 = Sim`)**:
  - **`row_id` 103** (`storage/H29I8TDV`, *IEEE Sensors Journal*, 2026): *A Hybrid Multimodal Deep Learning Framework for Robust Diagnosis of Parkinson’s Disease Using Hand Tremor Analysis* — usa *Dryad*, *MPU-9250* e *PD Motor Severity*; cita PADS `[22]` apenas na introdução.
  - **`row_id` 111** (`storage/JS893BZF`, *IEEE Access*, 2026): *Parkinson’s Disease Severity Classification Under Non-IID Clients via Support-Calibrated Personalized Federated Learning* — usa *UCI Telemonitoring Voice Dataset* (42 clientes); cita PADS `[10],[11]` apenas na introdução.
  - **`row_id` 113** (`storage/3BL7E3ZZ`, *IEEE Access*, 2025): *Real-World Parkinson’s Hand Tremor Detection Using Ensemble Learning Techniques* — usa *PD-BioStampRC21* (33 sujeitos); cita Varghese `[43]` apenas na introdução.

---

## Distribuição por Base (`source`) e Lista Completa dos 22 Aceitos

| Source | Aceito | Incerto - texto completo | Rejeitado | Total |
|---|---:|---:|---:|---:|
| **(Manual) Google Scholar** | 8 | 1 | **75** *(72 + 3)* | **84** *(81 + 3)* |
| **(Manual) Nature Citations** | 4 | 0 | **10** *(13 − 3)* | **14** *(17 − 3)* |
| **IEEE Xplore** | 3 | 0 | 4 | 7 |
| **Scopus** | 6 | 0 | 0 | 6 |
| **Sciece Direct** | 1 | 0 | 2 | 3 |
| **PubMed Central** | 0 | 1 | 0 | 1 |
| **Total** | **22** | **2** | **91** | **115** |

### Lista Completa dos 22 Aceitos
| row_id | Key in zotero | Pasta PDF (`storage`) | Ano | Source | Título |
|---:|---|---|---:|---|---|
| 21 | `7L9HHAFF` | `XQBPGDPF` | 2026 | (Manual) Google Scholar | Early Detection and Differential Diagnosis of a Progressive Neurodegenerative Disorder Using Wearable Sensor Data and Machine Learning |
| 32 | `E7ZRIVPY` | `IHVQDZ9B` | 2025 | (Manual) Google Scholar | Self-Supervised Anomaly Detection for Parkinson’s Disease in Free-Living Environment |
| 40 | `CNUX42CD` | `8E6I5YL5` | 2025 | (Manual) Google Scholar | A Generative Adversarial Network-Based Method for Synthesizing Tremor Data in Parkinson’s Disease |
| 47 | `ZP6R6QZ7` | `7U443XI4` | 2025 | (Manual) Google Scholar | Improving Parkinson’s Diagnosis: A Stacked Ensemble Learning with Vocal Biomarkers and Data Balancing |
| 49 | `325RXTR4` | `JRGU3234` | 2025 | (Manual) Google Scholar | Differentiating Movement Disorders Using Smartwatch-Derived Motor Variability and Non-Motor Symptom Profiles |
| 51 | `JB6XBHBW` | `6TLX77WC` | 2024 | (Manual) Google Scholar | Adaptive Domain-Adversarial Multi-Instance Learning for Wearable-Sensor-Based Parkinson’s Disease Severity Assessment |
| 54 | `MTN6Z5IL` | `RHRNWLBA` | 2026 | (Manual) Google Scholar | Baseline mood and non-motor symptom burden are associated with cognitive progression in Parkinson’s disease: an interpretable follow-up cohort analysis with separate neuroimaging, molecular, and digital analyses in independent samples |
| 76 | `GNT5T8YH` | `ZLWPYPPZ` | 2025 | Scopus | ASA-DSNet: A Dual-Stage Framework with Ambiguous Sample Augmentation for Robust Parkinson's Disease Identification |
| 77 | `QH3ZXBBE` | `QH3ZXBBE` | 2026 | IEEE Xplore | NeuroLens: A Multimodal Mobile Platform for Early Parkinson's Disease Screening Using TinyML and Cross-Modal Feature Fusion |
| 79 | `Q7E9QHNT` | `G7BME278` | 2027* | Scopus | Three-Class Parkinson's disease screening from smartwatch motion signals: A comparison of physics-informed handcrafted features and deep embeddings with patient-level validation |
| 80 | `TRJRVQSJ` | `MHDPD75V` | 2025 | Scopus | Multi-Scale Frequency-Aware Adversarial Network for Parkinson's Disease Assessment Using Wearable Sensors |
| 81 | `WKHH536I` | `WXI924XR` | 2026 | IEEE Xplore | Energy Optimized Feature Engineering for Parkinson's Disease Detection Using Wearable Sensor Data |
| 83 | `LEAQMNA6` | `LEAQMNA6` | 2026 | Sciece Direct | Blockchain-enabled hybrid CNN–Transformer framework with Integrated Gradients for Parkinson’s disease detection |
| 85 | `PA53H2JA` | `5YFLDAXW` | 2025 | IEEE Xplore | Smartwatch-Based IMU Analysis of Motor Tasks for Parkinson's Disease Screening |
| 87 | `RDFTW55M` | `5DPEEEQZ` | 2025 | Scopus | Parkinson’s Disease Detection Using Multiscale Frequency-Sharing Channel Attention Network With Smartwatch Movement Recordings |
| 89 | `TIZP8P7E` | `TSIEMXD7` | 2026 | Scopus | Parkinson's Disease Classification from Smartwatch Non-Motor Symptom Questionnaires in the PADS Dataset |
| 90 | `DN9TWI94` | `WTVMP8PU` | 2026 | Scopus | A Simple and Reproducible Machine Learning Pipeline for Parkinson’s Disease Detection Using Smartwatch-Based Inertial Signals |
| 92 | `85VJWA6S` | `UMKA3MVR` | 2024 | (Manual) Google Scholar | Improved Deep Learning for Parkinson’s Diagnosis Based on Wearable Sensors |
| **104** | `6ALP5R4U` | `6ALP5R4U` | 2026 | (Manual) Nature Citations | Eco-xPD: Enhancing deep learning based Parkinson’s disease detection with domain adaptive knowledge distillation from high-cost imaging to low-cost modalities |
| **105** | `RD5LYQ4W` | `RD5LYQ4W` | 2025 | (Manual) Nature Citations | Identificação da Doença de Parkinson através da Análise de Dados Coletados por Smartwatch |
| **108** | `HEUSS8MW` | `HEUSS8MW` | 2024 | (Manual) Nature Citations | Parkinson’s Disease Classification Employing a Questionnaire of Non-motor Symptoms and Machine Learning Methods |
| **109** | `S399Z5MS` | `S399Z5MS` | 2025 | (Manual) Nature Citations | Parkinson’s Disease Classification Using Inertial Signals from Smartwatches and Tree-Based Classifiers |

*\*Nota: `row_id` 79 possui `year = 2027` no metadado, mas DOI (`10.1016/j.bspc.2026.111448`) e copyright (`© 2026`) confirmam publicação antecipada em 2026.*

---

## Verificações Obrigatórias (115 Registros)
| Verificação | Detalhe | Status |
|---|---|---|
| Aceito + Rejeitado + Incerto = total de linhas | 22 + 91 + 2 = 115 | ✅ OK |
| Soma por `source` = total de linhas | 84 (Google Scholar) + 14 (Nature Citations) + 7 (IEEE Xplore) + 6 (Scopus) + 3 (Sciece Direct) + 1 (PubMed Central) = 115 | ✅ OK |
| Soma por `Criterio_determinante` dos Rejeitados = total de Rejeitados | 31 (CI1) + 23 (CE4) + 21 (CE3) + 16 (CE2) = 91 | ✅ OK |
| Lista de Aceitos na aba Resumo = contagem de Aceitos | 22 linhas listadas = 22 Aceitos | ✅ OK |
| Nenhuma linha perdida/duplicada; valores originais intactos | 115 linhas (`101 Base+Scholar + 14 Nature`), `row_id` único (`1..115`), 26 colunas originais 100% idênticas | ✅ OK |

---

## Principais Critérios de Rejeição (91 Rejeitados)
1. **CI1 / CE1 (Não usa dados do PADS; cita apenas como trabalho relacionado — 31 registros)**: 26 registros de `(Manual) Google Scholar` / bases primárias (23 do lote inicial + 3 reclassificados para Google Scholar: `row_id` 103, 111 e 113) + 5 registros de `(Manual) Nature Citations` (`row_id` 100, 102, 106, 112 e 114).
2. **CE4 (Duplicata — 23 registros)**: 13 grupos de artigos repetidos entre bases no lote inicial (DOI idêntico); nenhuma duplicata adicional entre `row_id` 99–115.
3. **CE3 (Revisão / Survey / Estudo secundário — 21 registros)**: revisões sistemáticas, narrativas ou de escopo (`row_id` 1, 19, 20, 27, 30, 46, 57, 58, 60, 61, 62, 64, 65, 67, 68, 72, 94, 95, 96, 97, 98).
4. **CE2 (Literatura cinza / Sem revisão por pares — 16 registros)**: 11 registros do lote inicial + 5 registros de `(Manual) Nature Citations` (`row_id` 99, 101, 107, 110 e 115).
   - *Destaque importante*: ao todo, **6 preprints usam experimentalmente os dados do PADS (`CI1 = Atende`)**, mas foram rejeitados estritamente por **CE2**: `row_id` 2 (`Research Square`, duplicata no `row_id` 42), `row_id` 13 (`medRxiv`, duplicata no `row_id` 18), `row_id` 23 (`arXiv:2604.18372`), `row_id` 44 (`arXiv:2609.16768`), **`row_id` 99** (`JMIR Preprints 109459`) e **`row_id` 101** (`arXiv:2605.08302`, *SGC-RML*).

---

## Colunas Vazias nas Planilhas Originais (115 linhas) e Registros sem Resumo
- **100% vazias (115/115)**: `affiliation`, `selection_criteria`, `comments`.
- **Parcialmente vazias**: `author_keywords` (109), `document_type` (108), `updated_by` (98), `note` (91), `publisher` (72), `language` (63), `volume` (60), `journal` (53), `issn` (43), `pages` (23), `keywords` (23), `url` (10), `doi` (3), `Key in zotero` (3 — `row_id` 55, 110 e 115), `abstract` (2), `author` (1), `year` (1).
- **Registros sem resumo na planilha original (por `source`)**:
  - `(Manual) Google Scholar` (84 registros): **1** (`row_id` 29 — lido via PDF em `storage/83XAWIVI`).
  - `PubMed Central` (1 registro): **1** (`row_id` 78 — duplicata do artigo-semente `row_id` 70).
  - `(Manual) Nature Citations` (14 registros): **0** (todos os 14 registros possuem resumo).

---

## 10 Casos de Menor Confiança / Atenção para Revisão Manual
Com a leitura de 111 PDFs, **nenhum registro ficou com confiança Baixa** (107 têm confiança **Alta** e 8 têm confiança **Média**). Abaixo estão os **10 casos prioritários** para revisão humana:

1. **`row_id` 47 (Aceito — Confiança Média, Relevância QP Baixa)**: propõe ensemble para biomarcadores de voz e reporta aplicação ao PADS (100% de acurácia em 3 classes com 83 amostras cada), sem especificar quais variáveis do PADS alimentaram o pipeline.
2. **`row_id` 54 (Aceito — Confiança Média, Relevância QP Baixa)**: estudo focado no PPMI que realiza análise estatística suplementar no PADS relacionando amplitude motora no punho à carga de sintomas não motores, sem treinar classificador diagnóstico no PADS.
3. **`row_id` 77 (Aceito — Confiança Média, Relevância QP Média)**: plataforma *NeuroLens* em que apenas o módulo vestível (1D-CNN TinyML) foi treinado no PADS (355 sujeitos, AUC 0,732).
4. **`row_id` 85 (Aceito — Confiança Média, Relevância QP Alta)**: analisa as 11 tarefas motoras do PADS separadamente, mas não explicita a divisão treino/teste nem se o *up-sampling* foi restrito ao treino.
5. **`row_id` 89 e `row_id` 108 (Aceitos — Alerta de Escopo da Regra 8: `usa PADS sem dados de sensor`)**: ambos utilizam exclusivamente o questionário de 30 sintomas não motores (PDNMS) do PADS (`row_id` 89 com 469 sujeitos no IEEE IRASET 2026; `row_id` 108 com 234 sujeitos em artigo curto de 2 páginas na ERI-GO/SBC 2024).
6. **`row_id` 70 e `row_id` 78 (Incertos — Confiança Média — Regra 9)**: o artigo-semente de Varghese et al. (2024) e sua duplicata no PubMed Central, mantidos como `Incerto - texto completo` por determinação expressa da Regra 9.
7. **`row_id` 33 (Rejeitado por CE2/CE3 — Confiança Média)**: capítulo de livro da Springer com resumo truncado e única chave (`V4LVBXYN`) sem PDF em `storage`.
8. **`row_id` 55 (Rejeitado por CE2/CE3 — Confiança Média)**: livro da CRC Press sem `Key in zotero` e sem PDF em `storage`.
9. **`row_id` 110 e `row_id` 115 (Rejeitados por CE2 — Confiança Alta, sem PDF)**: os únicos dois registros de `(Manual) Nature Citations` sem `Key in zotero` e sem PDF em `storage`, ambos capítulos de livros da Springer (`10.1007/978-3-032-15395-1_3` e `10.1007/978-3-032-06520-9_1`).
10. **`row_id` 2, 13, 23, 44, 99 e 101 (Rejeitados por CE2 — Alta Relevância Técnica)**: os 6 preprints (*Research Square*, *medRxiv*, *arXiv* e *JMIR Preprints*) que **executam experimentos próprios no PADS** (`CI1 = Atende`), incluindo os dois de `(Manual) Nature Citations` (`row_id` 99 com Conv1D-BiLSTM e `row_id` 101 com PatchTST + calibração conformal no *SGC-RML*).

---

## Relatório de Execução e Handoff Técnico (Para Continuidade em Outro Computador / Outro Antigravity)

### 1. Contexto e Estado Atual do Projeto (100% Concluído até a Etapa Atual)
- **Tarefa**: Mapeamento Sistemático Rápido (*Rapid Review*) sobre estudos que utilizam o dataset **PADS** (*Parkinson's Disease Smartwatch dataset*, Varghese et al., 2024) para detecção/classificação da Doença de Parkinson (DP) com dados de smartwatch.
- **Evolução das Versões**:
  - **v1**: Triagem automatizada baseada exclusivamente nos metadados da planilha inicial (`articles com Snowballing.xls`, 98 linhas) → havia resultado em 13 Aceitos, 70 Rejeitados e 15 Incertos.
  - **v2 (Texto Completo)**: Inclusão da coluna `Key in zotero` e leitura integral dos PDFs/caches na pasta `storage` do Zotero para as 98 linhas → resolveu todos os 13 casos incertos não-semente, resultando em 18 Aceitos, 78 Rejeitados e 2 Incertos (as duas entradas do artigo-semente de Varghese et al., `row_id` 70 e 78).
  - **v2 Consolidada (Atual — 115 linhas)**: Inclusão dos 17 artigos extras de `articles com Snowballing - Nature.xlsx` (`row_id` 99 a 115) e ajuste de `source` de 3 artigos (`row_id` 103, 111 e 113) de `(Manual) Nature Citations` para `(Manual) Google Scholar`. Resultado final consolidado: **22 Aceitos**, **91 Rejeitados** e **2 Incertos - texto completo** (`Total = 115`).

### 2. Estrutura de Diretórios e Arquivos-Chave no Workspace (`Zotero`)
- **Diretório raiz do workspace**: `<Zotero_Root>` (no computador anterior: `C:\Users\lucas.sneves\Zotero`)
- **Arquivos de Entrada**:
  1. `<Zotero_Root>\Relatório analítico\articles com Snowballing.xls` (98 linhas, `row_id` 1 a 98, 26 colunas originais incluindo `Key in zotero`).
  2. `<Zotero_Root>\Relatório analítico\articles com Snowballing - Nature.xlsx` (17 linhas, `row_id` 99 a 115, mesmas 26 colunas originais; já atualizada com `source = "(Manual) Google Scholar"` nas linhas correspondentes a `row_id` 103, 111 e 113, e `source = "(Manual) Nature Citations"` nas demais 14 linhas).
- **Arquivos de Saída (Sincronizados em Dois Locais)**:
  1. `<Zotero_Root>\Relatório analítico\triagem_resultado.xlsx` e `<Zotero_Root>\triagem_resultado.xlsx`
     - **Aba `Triagem`**: 115 linhas × 49 colunas (`row_id` como 1ª coluna + 26 colunas originais intactas + 22 colunas de triagem e QP: `CI1, CI2, CI3, CI4, CE1, CE2, CE3, CE4, CE5, CE6, Decisao_IA, Criterio_determinante, Evidencia, Confianca, Pendencias, Alertas, QP1_Tipo_contribuicao, QP2_Tarefa_e_recorte, QP3_Tecnicas, QP4_Validacao_e_metricas, QP5_Possivel_lacuna, Relevancia_QP`).
     - **Aba `Resumo`**: Tabelas consolidadas de contagem por `Decisao_IA`, por `Criterio_determinante`, por `source`, tabela cruzada `source x Decisao_IA`, tabela das 5 verificações obrigatórias (todas `OK = 1`) e lista completa dos 22 artigos `Aceito` (`row_id`, `Key in zotero`, `title`, `year`, `source`).
  2. `<Zotero_Root>\Relatório analítico\relatório_final.md` e `<Zotero_Root>\relatório_final.md` (este documento).
- **Banco de Dados e Textos Completos do Zotero**:
  - Banco SQLite: `<Zotero_Root>\zotero.sqlite`
  - Pasta de anexos: `<Zotero_Root>\storage\<attachment_key>\` (contém o arquivo `.pdf` e o texto indexado em `.zotero-ft-cache`, que pode ser lido diretamente em UTF-8).

### 3. Como Mapear `Key in zotero` para a Pasta `storage`
- **Para `row_id` 1 a 98**: na maioria das linhas, `Key in zotero` é a chave do **item-pai** no Zotero (`items.key`), enquanto a subpasta dentro de `storage\` usa a chave do **item-anexo** (`itemAttachments`). Para resolver via Python sem bloquear o Zotero:
  1. Copie `zotero.sqlite` para um arquivo temporário (ex.: `ztmp.sqlite`) e apague-o ao terminar.
  2. Execute a query SQL:
     ```sql
     SELECT i_parent.key AS parent_key, i_att.key AS att_key
     FROM items i_parent
     JOIN itemAttachments ia ON ia.parentItemID = i_parent.itemID
     JOIN items i_att ON i_att.itemID = ia.itemID
     ```
  3. Em alguns registros de `1–98` e em **todos os 15 registros com PDF de `99–115`**, o valor em `Key in zotero` já é diretamente o nome da subpasta `storage\<Key in zotero>`.
- **Os únicos 4 registros (de 115) sem PDF em `storage` (`CE5 = "Sim"`)**:
  - `row_id` 33 (`Key in zotero = V4LVBXYN`, capítulo da Springer sem anexo).
  - `row_id` 55 (`Key in zotero` vazio, livro da CRC Press).
  - `row_id` 110 (`Key in zotero` vazio, capítulo da Springer).
  - `row_id` 115 (`Key in zotero` vazio, capítulo da Springer).

### 4. Regras de Negócio e Convenções Estritas da Planilha (Para Novas Inclusões ou Ajustes)
1. **Imutabilidade dos Metadados**: nunca alterar valores das 26 colunas originais (`status`, `selection_criteria`, `comments`, `note` etc.), a menos que o usuário peça explicitamente uma correção de classificação (como o ajuste de `source` feito nos `row_id` 103, 111 e 113).
2. **Convenção de `Criterio_determinante` (usada nas verificações automáticas)**:
   - Para `Decisao_IA == "Aceito"`: usar exatamente `"CI1 atendido (Aceito)"`.
   - Para `Decisao_IA == "Incerto - texto completo"`: usar `"Regra 9 (artigo-semente)"` (casos `row_id` 70 e 78).
   - Para `Decisao_IA == "Rejeitado"`: usar um único código determinante principal (`"CE4"` para duplicatas, `"CE3"` para revisões/surveys, `"CE2"` para preprints/livros/capítulos/teses/pôsteres, ou `"CI1"` para artigos primários que não usam o PADS).
3. **Regras Especiais do Protocolo**:
   - **Regra 8 (`usa PADS sem dados de sensor`)**: artigos que usam apenas o questionário não motor (PDNMS de 30 itens) do PADS sem sinais inerciais (`row_id` 89 e `row_id` 108) recebem `CI1 = Atende`, `Decisao_IA = Aceito` e registro obrigatório `"usa PADS sem dados de sensor"` em `Alertas`.
   - **Regra 9 (`artigo-semente`)**: o artigo original do PADS (Varghese et al., 2024, `row_id` 70 e sua duplicata na PMC `row_id` 78) recebe `Decisao_IA = "Incerto - texto completo"` e `Alertas = "artigo-semente"`.
   - **Tag `[Texto completo]` nas colunas `QP1` a `QP5`**: nas colunas de Questões de Pesquisa, manter o que veio do resumo e prefixar com `[Texto completo]` os detalhes metodológicos, recortes amostrais e métricas extraídos da leitura do PDF.
   - **Limpeza obrigatória**: sempre apagar quaisquer scripts Python ou bancos temporários criados durante o processamento, mantendo apenas os arquivos finais.
