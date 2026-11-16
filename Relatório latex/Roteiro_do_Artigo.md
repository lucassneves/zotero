# Roteiro do Artigo — Mapeamento Rápido dos Estudos que Utilizam o Dataset PADS

Documento para (1) orientar a redação do artigo no modelo SBC e (2) apoiar a conversa com os orientadores sobre o que falta e o que pode mudar. A seção 6 reúne as **pendências e decisões**, em ordem de prioridade.

**Título provisório:** *Smartwatches e Doença de Parkinson: Um Mapeamento Rápido dos Estudos que Utilizam o Dataset PADS* (título do protocolo).

**Tipo de artigo:** mapeamento sistemático rápido (rapid review, descritivo), com avaliação de qualidade metodológica e de risco de vazamento de dados reportado.

**Contexto:** trabalho da disciplina de Metodologia de Pesquisa, em português, com 10 a 12 páginas (incluindo referências), no formato do modelo SBC e sem evento-alvo.

**Fontes dos dados:** protocolo (Parsifal), `extracao.xlsx` (29 estudos, 38 campos do formulário mais colunas derivadas) e referências do Zotero.

## 1. Mensagem central (hipótese de trabalho)

> O PADS passou a ser usado de forma crescente como base de aprendizado de máquina para Parkinson, mas os estudos diferem muito em cenário de classificação, recorte dos dados, protocolo de validação e métricas. O relato sobre separação por participante, balanceamento e pré-processamento é frequentemente incompleto, quase não há validação externa reportada e poucos estudos disponibilizam código ou dados. Isso limita a comparação entre resultados e a reprodutibilidade, e indica oportunidades para um protocolo de avaliação mais robusto.

Esta mensagem sai da prévia dos números atuais (seção 5) e **só deve ser mantida depois de resolvidas as pendências B3, B4 e I1** (seção 6).

## 2. Estrutura do artigo

O orçamento considera **11 páginas, incluindo referências** (faixa permitida: 10 a 12).

| Seção | Objetivo | Conteúdo | Fonte | Páginas |
| --- | --- | --- | --- | --- |
| Resumo / Abstract | Dizer o que foi feito e achado | Objetivo, método, 3 achados, implicação (até 10 linhas cada) | Resultados | 0,3 |
| 1. Introdução | Motivar e delimitar | Contexto (DP, diagnóstico, smartwatches, biomarcadores digitais); PADS como base aberta; problema (uso heterogêneo e sem consolidação); objetivo (GQM) e QP1 a QP5; contribuições; organização | Protocolo; Varghese et al. | 0,9 |
| 2. Contexto | Dar a base mínima | 2.1 PADS (469 participantes: 276 PD, 79 HC, 114 DD; tarefas, sensores, questionário PDNMS); 2.2 estudo-base de ML no PADS; 2.3 revisões relacionadas sobre sensores vestíveis em DP | Descritor do PADS; Zotero | 0,9 |
| 3. Método | Permitir replicar o mapeamento | 3.1 visão geral e diretrizes; 3.2 QP e PICOC; 3.3 busca (três rotas: citações do artigo-base, strings em 4 bases e snowballing); 3.4 seleção (CI/CE, fluxo e **desvio do protocolo: inclusão de preprints**); 3.5 avaliação de qualidade (QA1 a QA5, pontuação); 3.6 extração (38 campos), assistência de IA com revisão humana e regra do risco de vazamento | Protocolo; Parsifal | 1,8 |
| 4. Resultados | Responder às QP | 4.1 panorama (QP1, com tipo de publicação e veículo); 4.2 tarefas e recortes (QP2); 4.3 técnicas (QP3); 4.4 validação, métricas e desempenho reportado (QP4); 4.5 qualidade e reprodutibilidade; 4.6 lacunas (QP5); **4.7 literatura cinzenta (preprints)** | `extracao.xlsx`; metadados | 3,7 |
| 5. Discussão | Interpretar com cautela | Achados principais; implicações para quem usa o PADS (boas práticas de avaliação); estudo-base como referência; efeito dos preprints; ameaças à validade | Resultados | 1,5 |
| 6. Conclusão | Fechar e apontar o futuro | Síntese; lacunas; trabalhos futuros (ligação com a dissertação) | Resultados | 0,4 |
| Referências | — | Estudos incluídos, PADS, método | Zotero (`.bib`) | 1,5 |

**Linhas de redação:**
- Cada parágrafo de resultados responde a uma QP e traz o denominador (n/29, ou n/27 quando há "não se aplica").
- Mapeamento é descritivo: sem ranquear estudos por desempenho e sem comparar acurácias de cenários, métricas ou validações diferentes.
- O risco de vazamento é uma **classificação do relato** dos autores, não prova de vazamento.

## 3. Mapa QP → campos → análise → artefato

As QP vêm do protocolo e **estruturam os resultados** (ver pendência I3). Os nomes de campo são os do Parsifal.

| QP | Pergunta (protocolo) | Campos / colunas | Análise | Artefato |
| --- | --- | --- | --- | --- |
| QP1 | Quais estudos usam o PADS e como se distribuem por ano, veículo e tipo de contribuição? | Ano de Publicação, Tipo de Contribuição (e Outra), Papel do PADS, Datasets (e Outros); **tipo de publicação e veículo: `dados/metadados_estudos.csv`**, obtidos pela IA no Zotero e no PDF (pendência B5) | Contagens por ano, contribuição, papel e outras bases | Figura 2; Tabela 1 |
| QP2 | Quais tarefas de classificação e recortes (grupos, movimentos, sensores, punhos)? | Modalidade, Tarefas (e Quais), Sensores, Punho(s), N° de participantes, N° por classe, Cenários de classificação | Contagens e cruzamento cenário × modalidade | Tabela 2 |
| QP3 | Quais pré-processamentos, atributos e modelos? | Representação de entrada, Família do Algoritmo, Espeçificação do Algoritmo, Balanceamento/augmentation, Detalhes do balanceamento | Contagens; cruzamento cenário × família | Figura 3 |
| QP4 | Quais validações e métricas, e qual o desempenho reportado? | Estratégia de Validação, Unidade de particionamento, Separação por participante, Balanceamento (momento), `aux_preproc_apenas_treino`, `risco_vazamento`, Validação externa, Métricas, Melhor resultado, Demais valores | Contagens; risco por unidade e separação; lista descritiva de desempenho por cenário | Figura 4; Tabelas 3 e 4 |
| QP5 | Quais lacunas e oportunidades? | Código/dados disponíveis, Limitações Reportadas, Lacuna identificada, QA1 a QA5, `nota_qa_pct`, `faixa_qa` | Contagens; síntese temática dos textos livres | Figura 5; Tabela 5 |

**Artefatos (todos gerados por script a partir da planilha):**
- Figura 1: fluxo de seleção (numeração parcial; faltam as rejeições por etapa e por critério, B3).
- Figura 2: estudos por ano, empilhados por tipo de contribuição.
- Figura 3: cenário × família de algoritmo.
- Figura 4: risco de vazamento por unidade de particionamento e separação por participante.
- Figura 5: QA1 a QA5 (Yes, Partially, No, N/A).
- Tabela 1: estudos incluídos (compacta; candidata a material suplementar se o limite apertar).
- Tabela 2: recorte do PADS.
- Tabela 3: validação e vazamento.
- Tabela 4: desempenho reportado, em ordem de `row_id` (sem ranking).
- Tabela 5: lacunas.
- Tabela 6: preprints × revisados por pares (compacta, em 4.7).

Figuras em preto e branco ou tons de cinza (exigência do modelo SBC), e tabelas sem cor.

## 4. Como o método será descrito (pontos de atenção)

- **Diretrizes:** mapeamento sistemático rápido, com objetivo GQM, PICOC, QP, strings por base e critérios CI1 a CI4 e CE1 a CE6, conforme o protocolo.
- **Fontes:** Google Scholar e Nature Citations (manuais), IEEE Xplore, PubMed Central, ScienceDirect e Scopus.
- **Preprints (literatura cinzenta):** o protocolo (CE2 e CI3) os exclui, mas foram incluídos. O artigo declara o desvio, informa quantos são, compara descritivamente seus achados com os dos estudos revisados por pares e refaz os resultados principais sem eles (análise de sensibilidade). Sem testes inferenciais, por causa do n pequeno.
- **Busca em três rotas e números informados pelo autor (a confirmar):**
  - **Rota 1, citações do artigo-base do PADS:** Google Scholar, 69 registros; Nature Citations (Dimensions), 77 citações recuperadas, das quais 14 só nela (63 em comum com o Google Scholar e 6 só no Google Scholar). União: 83.
  - **Rota 2, strings nas bases:** IEEE Xplore 7, PubMed Central 1, ScienceDirect 3 e Scopus 6 (17 no total; mapeamento por base a confirmar).
  - **Rota 3, snowballing:** 15 estudos, registrados no balde do Google Scholar (84 = 69 + 15), a partir das citações de 11 estudos carregados, sem duplicatas e incluindo o artigo-base.
  - **Total importado:** 115 = 69 + 14 + 15 + 17.
  - **Seleção no Parsifal:** 115 importados → 24 duplicados → 91 triados → 62 rejeitados → **29 aceitos** (24 + 62 + 29 = 115). Faltam a divisão das rejeições por etapa e por critério e a data da busca (B3).
- **Extração:** 38 campos do formulário, com assistência de IA e revisão humana. O texto precisa dizer qual modelo, quem revisou e o que foi conferido (I2). Não houve dupla extração nem cálculo de concordância.
- **Qualidade:** QA1 a QA5 com Yes = 1,0, Partially = 0,5 e No = 0,0. Perguntas não aplicáveis (N/A) ficam fora do cálculo, e a nota é proporcional (`nota_qa_pct`). As faixas (Alta ≥ 80%, Média 50 a 79%, Baixa < 50%) são provisórias (I4).
- **Risco de vazamento:** regra própria sobre unidade de particionamento, separação por participante, momento do balanceamento e pré-processamento só no treino. Precisa de justificativa (I5).

## 5. Prévia dos números atuais (planilha `extracao.xlsx`, n = 29)

Valores **antes da validação final**; servem para discutir a história do artigo e para testar os artefatos.

| Tema | Resultado atual |
| --- | --- |
| Ano | 2024: 4; 2025: 10; 2026: 15 |
| Tipo de contribuição | Novo modelo 17; estudo comparativo 8; análise estatística 2; plataforma/sistema 1; outro 1 |
| Papel do PADS | Principal 25; análise suplementar 3; validação externa/generalização 1 |
| Outras bases | 11 estudos usam o PADS junto com outra base (9 públicas, 5 privadas; há sobreposição) |
| Modalidade | Série temporal (IMU) 27; questionário PDNMS 9; metadados 8 |
| Sensores | Giroscópio 25; acelerômetro 24 |
| Tarefas | Todas 14; subconjunto 7; não reportado 6; não se aplica 2 |
| Punhos | Ambos 16; não reportado 9; esquerdo 1; direito 1; não se aplica 2 |
| N de participantes | Reportado em 21 de 29 (234 a 469) |
| Cenários (multirrótulo) | PD×HC 20; PD×DD 15; 3 classes 7; DD×HC 2; outro 5 |
| Representação | Série bruta 20; atributos manuais 14; tempo-frequência 4; outro 4 |
| Família do algoritmo | Deep learning 22; ML clássico 18; híbrido/ensemble 5; generativo 3; auto-supervisionado 3; outro 2 |
| Balanceamento/augmentation | Nenhum 9; outro 9; SMOTE 6; GAN 2; não se aplica 2; não reportado 1 |
| Estratégia de validação | k-fold 24; hold-out 9; CV aninhada 6; LOSO 1; não reportado 3; outra 1 |
| Unidade de particionamento | Participante 22; não reportado 5; não se aplica 2 |
| Separação por participante | Sim, explícita 16; sim, inferida 6; pouco claro 5; não se aplica 2 |
| Momento do balanceamento | Só no treino 11; antes do split 4; não reportado 2; não se aplica 12 |
| Validação externa | **Não em 29 de 29** (ver I1) |
| Métricas (multirrótulo) | F1 25; accuracy 23; sensibilidade 20; precisão 15; AUC 11; balanced accuracy 11; especificidade 7; MCC 1 |
| Código/dados | Código 3; ambos 1; nenhum 12; não reportado 13 (apenas 4 de 29 disponibilizam algo) |
| Risco de vazamento (27 aplicáveis) | Baixo 10; moderado 10; alto 5; indeterminado 2 |
| QA | Média de 64% (`nota_qa_pct`); faixa alta 9, média 17, baixa 3 |
| Status de triagem | Aceito 22; com ressalvas 5; com ressalvas e não confiável 1; "Incerto – texto completo" 1 |
| Fluxo de seleção (Parsifal) | 115 importados; 24 duplicados; 62 rejeitados; 29 aceitos |

**Leituras possíveis (a confirmar):**
- O uso do PADS cresce rapidamente: 4, 10 e 15 estudos nos três anos.
- O foco é PD×HC e deep learning, mas cerca de metade dos estudos também faz PD×DD.
- Só 10 de 27 estudos aplicáveis têm risco de vazamento baixo.
- Quase não há validação externa e o compartilhamento de código é raro.

## 6. Pendências e pontos para discutir com os orientadores

### 6.0 Decisões já tomadas

- Artigo da disciplina de Metodologia de Pesquisa (rapid review conforme o protocolo), sem evento-alvo; modelo SBC como formato.
- Idioma: português. Extensão: 10 a 12 páginas, incluindo referências.
- Preprints incluídos, apesar do CE2 e do CI3, e tratados em seção própria (4.7).
- Scripts de construção do artigo não serão publicados.
- A extração foi feita a partir do texto original de cada artigo (Key in Zotero), sem usar as QP como guia.

### 6.1 Bloqueantes (resolver antes de fechar o texto)

| # | Pendência | Por que importa | Como resolver |
| --- | --- | --- | --- |
| B1 | **Arquivos de estilo do template SBC.** O `sbc-template.tex` foi recebido, mas carrega `\usepackage{sbc-template}` e usa `\bibliographystyle{sbc}`; faltam `sbc-template.sty` e `sbc.bst`. O `.tex` também declara `latin1` e `utf8` ao mesmo tempo (conflito de codificação). | Sem o `.sty` e o `.bst`, o `.tex` não compila e a formatação vira aproximação. | Baixar `sbc-template.sty` e `sbc.bst` do mesmo pacote da SBC. O conflito de codificação é corrigido no projeto (mantendo só `utf8`). |
| B3 | **Fluxo de seleção: etapas intermediárias.** Os números fecham: 115 importados, 24 duplicados, 62 rejeitados e 29 aceitos. Faltam a divisão das rejeições por etapa (título e resumo × texto completo) e por critério (CE1 a CE6), a data da busca e a data de lançamento do PADS (CI2). | A Figura 1 precisa das etapas intermediárias, e o leitor precisa poder repetir a busca. | Obter no Parsifal (ou nos registros de rejeição) os motivos e as etapas, se foram registrados. Confirmar o mapeamento 7/1/3/6 por base, a lista dos 11 estudos-semente e o artigo-base. Sem esses números, as etapas ficam como `\pend`. |
| B4 | **Preprints incluídos × protocolo.** O CE2 exclui preprints e literatura cinzenta e o CI3 exige revisão por pares, mas os preprints foram incluídos. | É um desvio do protocolo: precisa ser declarado e justificado, e o tratamento (seção própria e análise de sensibilidade) precisa do aval dos orientadores. | Identificar quais dos 29 são preprints (Zotero/PDF), registrar a justificativa e verificar se algum tem versão publicada posterior (CE4). Decidir também sobre o estudo "Incerto – texto completo" e os 6 com ressalvas (sensibilidade) e confirmar o idioma (CI4). |
| B5 | **Veículo e tipo de publicação (QP1).** Não estão na planilha e o autor não os conhece. | A QP1 pergunta pelo veículo e a seção de preprints depende do tipo de publicação. | A IA obtém no registro do Zotero e na primeira página do PDF (`dados/metadados_estudos.csv`, com evidência e confiança); o autor confere os casos "indeterminado". |
| B6 | **Arquivo `.bib` do Zotero.** | Sem ele, não há referências confiáveis e a IA não pode inventá-las. | Exportar os 29 estudos, o PADS e as referências de método, com chaves estáveis (ideal: chave do Zotero igual à citekey). |

### 6.2 Importantes (afetam as conclusões)

| # | Pendência | Observação |
| --- | --- | --- |
| I1 | **Possível incoerência em "Validação externa do Modelo".** Está "Não" nos 29, mas o estudo 47 tem papel "Validação externa-generalização" e 11 estudos usam mais de uma base. | Rever o campo antes de afirmar que nenhum estudo reportou validação externa. Definir o critério (treinar em uma base e testar em outra). |
| I2 | **Procedimento de validação da extração.** A extração foi assistida por IA, mas a aba `auditoria` da planilha enviada está vazia e não houve dupla extração. | Descrever o que foi feito (modelo, revisor, campos conferidos) e declarar a limitação, ou fazer dupla extração em uma amostra (por exemplo, 5 artigos) e relatar a concordância. |
| I3 | **QP do protocolo.** A extração foi feita sem usar as QP, mas o artigo será organizado por elas. | Confirmar com os orientadores o mapa da seção 3. A QP1 (veículo) e a QP5 ("lacunas para a dissertação") precisam de ajuste de redação para o artigo. |
| I4 | **Faixas da avaliação de qualidade.** Os limites de 80% e 50% são provisórios, e o Parsifal não tem resposta N/A (há estudos com N/A em QA1, QA3 e QA4). | Formalizar no protocolo e descrever o tratamento de N/A. |
| I5 | **Regra do risco de vazamento.** É uma regra própria baseada no relato. | Justificar com literatura e apresentar como classificação do relato. |
| I6 | **Nomenclatura e referências de método.** "Mapeamento sistemático rápido" e as diretrizes citadas. | Definir quais diretrizes de mapeamento sistemático, de revisões rápidas e de fluxo de seleção serão citadas (confirmar os dados no Zotero). |
| I7 | **Viés de seleção da busca.** A rota principal parte das citações do artigo-base (Google Scholar e Nature Citations), e 3 das 6 fontes tiveram poucos registros. | Estudos que usam o PADS sem citar o artigo-base e que as strings não recuperaram podem ter ficado de fora. | Declarar como ameaça à validade e, se houver tempo, fazer uma busca complementar por strings. |

### 6.3 Decisões de escopo (opcionais)

- **O1.** Tabela dos 29 estudos completa no corpo ou condensada, conforme o limite de 10 a 12 páginas.
- **O2.** Disponibilidade: os scripts não serão publicados; decidir se a planilha de extração será anexada, disponibilizada ou apenas descrita.
- **O3.** Escolher 3 a 5 revisões sobre sensores vestíveis em Parkinson para os trabalhos relacionados. Elas foram excluídas do corpus por CE3, mas servem de contexto.
- **O4.** Tratar à parte o estudo-base de ML no PADS (autores do dataset) na discussão.
- **O5.** Autoria, declaração de uso de IA (verificar a política da disciplina) e agradecimentos.
- **O6.** Data de corte da busca, já que 2026 ainda está em andamento.

### 6.4 Mudanças possíveis a propor

- Incluir no formulário os campos veículo, tipo de publicação e país.
- Reformular a QP5 para não depender da dissertação.
- Fazer uma busca complementar (por exemplo, por snowballing) se a data da busca ficar defasada.

## 7. Ordem sugerida de fechamento

1. Resolver B1 (arquivos de estilo) e B6 (arquivo `.bib`).
2. Fechar B3, B4 e B5 (fluxo de seleção, preprints e metadados) e I1 (validação externa).
3. Rodar o script de artefatos e revisar tabelas e figuras com os orientadores.
4. Redigir com a IA, seção por seção, seguindo este roteiro e o prompt.
5. Revisar o rascunho contra a planilha (todo número do texto vem de macro gerada pelo script).
6. Decidir I2 a I6 e atualizar método e ameaças à validade.
7. Fechar a versão final (10 a 12 páginas, referências e autoria).
