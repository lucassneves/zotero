# Auditoria da Triagem Rapid Review — Estudos que usam o PADS

Análise de `relatório_final.md` e `triagem_resultado.xlsx` (115 registros, 49 colunas).

## Objetivo

Auditar a triagem de Rapid Review sobre estudos que utilizam o dataset PADS, verificando consistência numérica, inconsistências de classificação e riscos metodológicos.

## Passos

1. Leitura do `.md` e das abas `Triagem` (115×49) e `Resumo`.
2. Recontagem de `Decisao_IA`, `Criterio_determinante` e `source` com `pandas`, e checagem de unicidade de `row_id`.
3. Agrupamento por DOI para auditar as duplicatas (CE4).
4. Cruzamento de CI/CE com a decisão, e revisão de `Relevancia_QP`, `Alertas` e QP1–QP5 dos 22 aceitos.
5. Nenhum arquivo intermediário foi criado.

## Resultado

### 1. Consistência numérica: OK

Tudo bate com o relatório:

- 22 Aceitos, 91 Rejeitados e 2 Incertos, totalizando 115.
- Rejeitados por critério determinante: CI1 31, CE4 23, CE3 21 e CE2 16.
- `row_id` é único e a tabela `source × Decisao_IA` fecha.

### 2. Funil de seleção

- 115 registros − 23 duplicatas (CE4) = **92 únicos**.
- Desses 92: 22 aceitos, 68 rejeitados e 2 incertos.
- Os 2 incertos são o artigo-semente (Varghese) e sua duplicata no PMC (`row_id` 70 e 78), mantidos pela Regra 9. Na prática, equivalem a 1 estudo.

### 3. Pontos que divergem ou merecem correção

- **O relatório diz "6 preprints que usam o PADS" rejeitados por CE2, mas são 7 registros com CI1 = Atende.** O sétimo é o `row_id` 82, um pôster de congresso (ACRM 2025, *Archives of PM&R*, e121), classificado como literatura cinza.
- **`row_id` 78 é duplicata do 70 (mesmo DOI), mas não recebeu CE4.** A exceção está documentada, mas deixa a contagem de "registros" diferente da de "estudos" e precisa de nota de rodapé.
- **`row_id` 79 tem `year` = 2027 no metadado.** DOI e copyright indicam 2026. Isso distorce a distribuição temporal se alguém agrupar por `year`.
- **`language` é inconsistente** (`English`, `en`, `EN`, `pt`, 8 vazios). Vale normalizar na tabela de caracterização.

### 4. Aceitos com inclusão frágil

- **`row_id` 47 e 54** têm relevância Baixa. No 47 o PADS é só um teste de generalização, e no 54 é uma análise suplementar de um estudo PPMI. Ambos satisfazem CI1 de forma mínima e são candidatos a revisão manual de elegibilidade.
- **`row_id` 89 e 108** usam só o questionário de sintomas não motores, sem sensor. A Regra 8 os mantém, mas isso deve ficar explícito na síntese ou virar uma subcategoria.
- **`row_id` 108** é um artigo curto de 2 páginas. Vale confirmar se passa em CI3, que exige artigo completo.
- **`row_id` 47 reporta Acc = 100%.** Os próprios autores levantam preocupação de vazamento de dados.
- **`row_id` 85** não explicita a divisão treino/teste nem se o *up-sampling* ficou restrito ao treino.

### 5. Perfil dos 22 aceitos

- **Ano:** 3 em 2024, 10 em 2025 e 8 em 2026 (mais 1 com ano 2027 no metadado). Há 1 artigo em português (`row_id` 105).
- **Relevância QP:** 19 Alta, 3 Média e 2 Baixa.
- **Confiança:** 8 dos 115 registros têm confiança Média (nenhum Baixa).
- **Rendimento por base:** Google Scholar 8/84 (\~10%), Nature Citations 4/14 (\~29%), Scopus 6/6, IEEE 3/7 e ScienceDirect 1/3.
- **Sobreposição de bases:** todos os 6 aceitos do Scopus têm duplicata no Scholar. O Scholar sozinho cobre a maior parte do corpus, o que ajuda a justificar o snowballing manual.

### 6. Riscos metodológicos para a escrita

- **Dependência de uma única IA:** toda a triagem é feita por IA, sem revisão humana. Sugestão: dupla triagem manual de uma amostra (os 8 de confiança Média, mais \~15–20% dos rejeitados por CI1/CE2) e cálculo de Cohen's κ.
- **Exclusão de preprints (CE2):** é coerente com a orientação do prof. Valdemar sobre literatura cinza. Mas 6 desses preprints executam experimentos próprios no PADS. Um deles (`row_id` 2) trata de **data leakage em augmentation no PADS**, muito relevante para a replicação de ML. Sugestão: análise de sensibilidade (22 → 28 com preprints) ou ao menos citá-los na discussão.    
- **Resultados não comparáveis entre estudos:** as amostras variam (355 vs 469 sujeitos, tarefas isoladas vs todas) e as validações também (CV 5-fold, LOSO, 80/20 por sujeito). Tratar como ameaça à validade em QP4 e QP5.
- **Campos vazios:** `affiliation`, `selection_criteria` e `comments` estão 100% vazios, e `abstract` falta em 2 registros. Não afeta a decisão, mas deve constar nas limitações.

## Próximo passo sugerido

Gerar a tabela de caracterização dos 22 aceitos (ano, tarefa, técnica, validação, métrica) em `.xlsx` ou Markdown para o protocolo.
