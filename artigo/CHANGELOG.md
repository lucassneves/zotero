# Changelog — Revisão de Manuscrito

Registro das alterações aplicadas ao artigo *Smartwatches e Doença de Parkinson: Um Mapeamento Rápido dos Estudos que Utilizam o Dataset PADS*, mantendo inalterados os valores quantitativos (`numeros.tex`), o limite de **12 páginas** (`sbc-template.sty`) e a ausência de travessões (`---`) e ponto e vírgula (`;`) na prosa.

## Coesão terminológica (Etapa G)

Varredura lexical por expressões regulares sobre `main.tex`, `secoes/*.tex`, `tabelas/*.tex` e `scripts/gerar_artefatos.py`, garantindo que siglas, categorias e termos técnicos recebam qualificação ou definição curta antes ou na sua primeira ocorrência.

| Termo | Primeira ocorrência | Onde é definido | Ação |
| --- | --- | --- | --- |
| `PD` (*Parkinson's disease*) | Abstract / Resumo / 1. Introdução | Abstract / Resumo / 1. Introdução (por extenso) | sem alteração |
| `DD` (*differential diagnoses*) | Abstract / Resumo / 1. Introdução | Abstract / Resumo / 1. Introdução (por extenso; removida repetição redundante no 2º parágrafo de 1) | padronizado |
| `HC` (*healthy controls*) | Abstract / Resumo / 1. Introdução | Abstract / Resumo (controles saudáveis) / 1. Introdução (*healthy controls*) | qualificado |
| `IMU` (*inertial measurement unit*) | 1. Introdução | 1. Introdução (por extenso) | sem alteração |
| `PDNMS` (questionário não motor) | 1. Introdução | 1. Introdução (por extenso) | sem alteração |
| `ML` (*machine learning*) | 1. Introdução | 1. Introdução (por extenso) | sem alteração |
| `DL` / *deep learning* | Abstract / Resumo / 1. Introdução | 1. Introdução (aprendizado profundo, DL); corpo unificado em `DL` (4.3, 4.7, 5.1, 6); rótulo `Deep Learning` na Tab. 6 e Fig. 3 | padronizado |
| `risco baixo/moderado/alto` (`low data leakage risk`) | Abstract / Resumo / 1. Introdução | Abstract/Resumo (qualificados na ocorrência); 1. Introdução remete à Seção 3.3 (`\label{sec:desvio_qa}`), onde são definidos os 5 níveis (`N/A`, `Alto`, `Baixo`, `Moderado`, `Indeterminado`); qualificador `"de vazamento"` aplicado em 3.3, 4.4, 4.7, 5.1, 5.2, 6, Tab. 1 (`Vaz.`) e Tab. 4 (`Vaz.`) | qualificado |
| `QA` / `QA1–QA5` / `nota_qa_pct` / `faixa Alta/Média/Baixa` | 1. Introdução | 1. Introdução (`qualidade metodológica (QA)`); definido em 3.3 (5 critérios `QA1–QA5`, exclusão de `N/A`, escore proporcional `nota_qa_pct` distinto do risco de vazamento e cortes `Alta >= 80%`, `Média 50%–79%`, `Baixa < 50%`); qualificado em 4.5, 5.2, Tab. 1 e Tab. 6 | qualificado |
| `PD×HC` | 2.1 (e Abstract/Resumo por extenso) | Abstract (`PD vs. healthy controls`), Resumo (`PD contra controles saudáveis`) e 2.1 (`PD contra HC (PD×HC)`); padrão `\times` mantido em todo o corpo, Tab. 1, 2, 4, 6 e Fig. 3 | padronizado |
| `PD×DD` | 2.1 (e Abstract/Resumo por extenso) | Abstract (`PD vs. DD`), Resumo (`PD contra DD`) e 2.1 (`PD contra DD (PD×DD)`); padrão `\times` mantido no corpo, Tab. 1, 2, 4, 5, 6 e Fig. 3 | padronizado |
| `DD×HC` | Tabela 1 (p. 5) | Definido por extenso em 4.2 (`DD contra HC (DD×HC)`, p. 5, logo abaixo da Tabela 1; `DD`, `HC` e `×` já definidos em 1 e 2.1) | definido |
| `CV` / `CV aninhada` | Abstract / 2.1 | Abstract (`cross-validation`); 2.1 (`validação cruzada (cross-validation - CV) aninhada 5×5 por sujeito (dobras internas e externas...)`); legenda da Tab. 4 (`Anin. = CV aninhada`) | definido |
| `BOSS` (*Bag-of-SFA-Symbols*) | 2.1 | 2.1 (`Bag-of-SFA-Symbols - BOSS`) | definido |
| `Bal. Acc.` (acurácia balanceada) | 2.1 | 2.1 (`acurácia balanceada (Bal. Acc.)`) | definido |
| `validação externa` | 2.2 | 2.2 (`validação externa (avaliação em base independente da de treino)`); Tab. 1 legenda (`*Val. ext. = validação externa sem teste independente`) | definido |
| `N/A` (não se aplica) | 3.1 | 3.1 (`Comparison (não se aplica, N/A)`); qualificado em 3.3 (estatísticos/sem modelo preditivo) e legenda da Tab. 1 (`N/A = não se aplica`) | definido |
| `AUC` (área sob a curva ROC) | 3.1 | 3.1 (`AUC - área sob a curva ROC`) | definido |
| `literatura cinzenta` | 3.2 | 3.2 (`CE2: literatura cinzenta (sem revisão formal: preprints, livros e resumos)`); padronizado de `cinza` (3.2, 3.3) para `cinzenta` alinhado a 4.7 | padronizado |
| `preprint` | Abstract / Resumo / 1. Introdução | 1. Introdução (`manuscritos sem revisão formal`); sentido único mantido em 3.2, 3.3, 4.1, 4.7, Tab. 6, 5.1, 5.2 e 6 | definido |
| `desvio de protocolo` | Abstract / Resumo | 3.3 (`Desvio declarado e casos limítrofes: apesar de CE2 e CI3 excluírem literatura cinzenta, mantivemos os 6 preprints...`) | sem alteração |
| `janelamento` | 3.3 | 3.3 (`janelamento, segmentação temporal das séries, dependente de classe`) | definido |
| `pré-split` (`balanceamento pré-split`) | 1. Introdução (conceitual) / 3.3 | 1. Introdução (etapas cruzando treino e teste); definido em 3.3 (`pré-split, anteriores à divisão treino/teste`) | definido |
| `Princ./Supl./Val. ext.` (Papel do PADS) | 4.1 / Tabela 1 | 4.1 (`fonte principal... suplementar... e declarado como validação externa`) e legenda da Tabela 1 (`Papel = uso do PADS (Princ./Supl. = principal/suplementar, *Val. ext. = validação externa sem teste independente)`) | qualificado |
| `3 classes` / `3-cl` | Tabela 1 (p. 5) | Legenda da Tabela 1 (`3-cl = 3 classes (PD/DD/HC)`) e 4.2 (`3 classes (classificação simultânea PD, DD e HC)`) | definido |
| `Outro` | 4.1 / Tabela 1 | 4.1 (`artigo-base (categoria Outro na Figura 2)`); 4.2 (`outros recortes (Outro, 5/29)` e `"IMU de 6 canais"`); Tab. 4 detalha sub-rótulos entre parênteses | qualificado |
| `Todas` / `Subconjunto` (tarefas motoras) | 4.2 (p. 5) / Tabela 2 (p. 6) | 4.2 (`todas as 11 tarefas motoras` e `apenas um subconjunto`) precede a Tabela 2 | qualificado |
| `Série bruta` | 4.3 | 4.3 (`séries temporais (categoria "Série bruta" do formulário...)`, seguida da explicitação de que reuniu sinais puros e pré-processados) | qualificado |
| `SSL` (auto-supervisionados) | 4.3 | 4.3 (`auto-supervisionados (SSL, 3)`) antes da Figura 3 (`Auto-sup. (SSL)`) | sem alteração |
| `k-fold` | Abstract / Resumo / 4.4 | Abstract/Resumo (`k-fold cross-validation`); corpo em 4.4 (`k-fold (validação cruzada em k dobras)`) antes das Tabelas 3 e 4 | definido |
| `hold-out` / `HO` | 4.4 | 4.4 (`hold-out (partição fixa treino/teste)`) e legenda da Tab. 4 (`HO = hold-out`) | definido |
| `LOSO` / `LOTO` | 4.4 | 4.4 (`LOSO (leave-one-subject-out)`) e legenda da Tab. 4 (`LOTO = leave-one-task-out`) | definido |
| `XAI` (explicabilidade) | 4.6 | 4.6 (`explicabilidade (XAI)`) antes da Tabela 5 | sem alteração |
| Frase-modelo da Seção 5.1 | 5.1 | 5.1 adaptada exatamente para os números via macros (`\nFamDL/\nTotal`, `\nRiscoBaixo/\nAplicaveisVaz`) e definição operacional de risco baixo de vazamento | padronizado |

### Termos não resolvidos ou mantidos sem expansão pelo limite de 12 páginas (para decisão do autor)

1. **`MCC` (Seção 5.1, p. 9)**: mantido apenas como sigla em `Bal. Acc./F1-macro/MCC` para não expandir o texto além das 12 páginas (a página 12 fecha próximo à margem inferior). Sugestão opcional: grafar *Matthews correlation coefficient* (MCC) caso haja espaço em versão futura.
2. **`SMOTE` e `GANs` (Seção 4.3 e Tabela 4)**: utilizados sem o nome por extenso (*Synthetic Minority Over-sampling Technique* e *Generative Adversarial Networks*) por economia de linhas em 4.3 e por serem acrônimos consagrados da área.
3. **`AUROC` e `ROC AUC` vs. `AUC` (Tabela 4 e Seção 5.1)**: `3.1` define `AUC - área sob a curva ROC`, enquanto a Tabela 4 (e 5.1 para `[Zannat 2026]`) preservam literalmente `AUROC` (row 23) e `ROC AUC` (row 99) conforme reportados nos artigos originais. Decidir se deseja unificar tudo como `AUC`.
4. **`F1` / `F1-macro` vs. `F1-score` (Seções 3.1, 4.4, Tabela 4 e 5.1)**: manteve-se `F1-score` no PICOC e na Tab. 4 (row 104), `F1` agregado em 4.4 e `F1-macro` na recomendação de 5.1.
5. **Uso de `vs.` no *Abstract* em inglês e em sub-rótulos da Tabela 4**: optou-se por `PD vs. healthy controls` / `PD vs. DD` no *Abstract* (inglês idiomático) e por manter os sub-rótulos originais entre parênteses na Tabela 4 (`Outro (PD vs. non-PD)`, `Outro (PL vs. PD)`, `Outro (PD vs. No PD)`, `PD×HC (DP vs. CO)`), reservando `PD×HC`, `PD×DD` e `DD×HC` para todos os cenários padronizados do corpo, tabelas e Figura 3. Decidir se prefere `$\times$` também no *Abstract*.
6. **`Deep Learning` (Tabela 6 e Figura 3) vs. `DL` (corpo do texto)**: mantido `Deep Learning` por extenso em rótulos nominais de tabela/eixo e no *Abstract/Resumo* (onde a sigla `DL` não se repete), e `DL` no corpo após a definição na Introdução.
7. **`DD×HC` e `Outro` na Tabela 1 antes de 4.2 (p. 5)**: na diagramação final, a Tabela 1 fica no topo da p. 5 e a Seção 4.2 logo abaixo define `DD contra HC (DD×HC)` e `outros recortes (Outro)`; a legenda da Tabela 1 omitiu glosa extra de `DD×HC` e `Outro` para não adicionar uma 6ª linha de legenda.
8. **Nomes próprios de métodos e arquiteturas na Tabela 4 e `2.1`/`4.3`**: siglas de modelos (`CNN`, `BiLSTM`, `LSTM`, `FCN`, `SVM`, `RF`, `LR`, `XGB-LGBM`, `TinyML`, `PatchTST`, `XceptionTime`, `CatBoost`, `z-score`, `$\ell_1$-trend filtering`) e escalas clínicas na Tabela 5 (`UPDRS/H&Y` para `MDS-UPDRS` e `Hoehn & Yahr`, já citados em `2.1`) foram mantidas no formato técnico padrão sem expansão adicional.
