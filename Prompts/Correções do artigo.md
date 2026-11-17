# TAREFA: revisão técnica do artigo "Smartwatches e Doença de Parkinson: Um Mapeamento Rápido dos Estudos que Utilizam o Dataset PADS"

## Contexto
Artigo SBC (entrega de disciplina) com 29 estudos incluídos. Todos os arquivos estão nesta pasta: fonte do artigo (.tex/.bib ou equivalente), export do Parsifal e planilha de extração (38 campos). Identifique os arquivos antes de editar. Mapeamento rápido, revisor único, sem PRISMA (apenas Petersen et al. 2018 e Garritty et al. 2021), string de busca propositalmente restrita e planilha não publicada: são decisões do autor, só devem ser DECLARADAS, não alteradas.

## Regras gerais
1. Faça backup do original (uma cópia) antes de editar.
2. Nunca altere um número sem recomputá-lo a partir da planilha/export. Se não for possível recomputar, NÃO altere e liste o caso no relatório.
3. Toda alteração numérica deve ser propagada para texto, tabelas, figuras, abstract/resumo e conclusão. Mantenha o limite de páginas atual, se houver.
4. Não altere dados bibliográficos (autores, DOIs, títulos) nem o conteúdo de QA/risco por estudo, exceto onde indicado.
5. Prefira funções de bibliotecas existentes (pandas, matplotlib, LaTeX packages) a código novo.
6. Ao final, apague todos os arquivos intermediários e deixe apenas: artigo atualizado (fonte + PDF compilado), figuras regeneradas (se houver) e CHANGELOG.md.

## Etapa A — Terminologia (aplicar em título, abstract, resumo, Seção 1 e 3.1)
- Remover "sistemático/systematic" de "mapeamento sistemático rápido" → "mapeamento rápido" / "rapid mapping study". Manter o título da referência Fernandes et al. 2018 intacto.
- Não usar "revisão multivocal". Usar "inclusão deliberada de literatura cinzenta (preprints)".
- Parsifal: descrever como ferramenta de apoio, não como "registro de protocolo".

## Etapa B — Desvio de protocolo (Seções 3.3, 4.7, 5.2)
Manter "desvio declarado" e reescrever a justificativa: preprints foram mantidos porque (i) atendem CI1 e CI4, (ii) obtiveram QA ≥ 70% (todos os 6 entre 70% e 90%), e (iii) o objetivo é caracterizar como o PADS vem sendo usado, incluindo literatura recente ainda sem versão publicada. Declarar em 5.2 que os 10 registros excluídos por CE2 não passaram por QA, e que, portanto, o limiar de QA foi aplicado só aos preprints mantidos (limitação). Declarar também que os preprints vieram por citações e snowballing, sem busca ativa em arXiv/medRxiv (viés de cobertura na comparação da Tabela 6).

## Etapa C — Limitações a declarar (curtas, em 5.2; 1–2 frases cada)
- Revisor único na triagem e na extração, por ser trabalho de disciplina (já há menção à extração; incluir triagem).
- String restrita de propósito (dependente do termo "PADS"), para limitar o escopo inicial; pode omitir estudos que citam só o nome completo ou o PhysioNet.
- QA ad hoc: QA3 se sobrepõe ao risco de vazamento; cortes 80/50% sem validação externa.
- Risco de vazamento reflete o relato: "não reportado" não equivale a "ausente".
- Detalhamento metodológico será ampliado em versão posterior (sem prometer prazo).

## Etapa D — Coerência interna (recomputar a partir da planilha)
1. Seção 4.5 está rotulada QP5, mas QP5 = lacunas. Ajustar o rótulo/mapeamento (QA e risco de vazamento atendem QP4) e conferir se a Seção 3.1 e os títulos de seção ficam coerentes.
2. Seção 3.3 / Tabela 1: Ren et al. aparece com 0%(B), mas a regra diz que itens N/A saem da nota_qa_pct. NÃO ALTERAR: calcular e reportar no relatório (a) o impacto na média (64,6%) e mediana (70,0%) e na distribuição Alta/Média/Baixa se Ren fosse excluído da nota; (b) se Abola também está tratado de forma coerente.
3. Seção 3.2: "recorte de 84 do Scholar" vs. 69 no Scholar. Reconciliar os números da Rota 1 (69, 14, 77, 63, 83, 6) e da Rota 3 com a planilha/Parsifal; reescrever o parágrafo para ficar sem ambiguidade e confirmar que o total 115 fecha.
4. Seção 4.2: "Entre quem usa IMU" usa denominadores /29; corrigir para /27 onde couber e recalcular (tarefas, punho, sensores).
5. Seção 5.1: o texto cita quatro critérios do artigo-base (CV aninhada, acurácia balanceada, código aberto, PD×DD) mas só três contagens (6, 11, 4). Incluir 15/29 para PD×DD na ordem correta e conferir cada contagem.
6. Seção 5.1: a afirmação de que falta controle de vazamento explica desempenhos 92–100% não se sustenta com a Tabela 4 (há risco Baixo com 95,3% e 93,2%, e Zannat, risco Alto, AUROC 0,963, fora da lista). Calcular, a partir da planilha, melhor métrica por nível de risco e cenário (PD×HC, PD×DD, 3 classes) e reescrever o trecho de forma descritiva e cautelosa ("estudos com risco alto/moderado reportam valores máximos mais altos" SOMENTE se os dados confirmarem). Incluir Zannat. Se não for possível estratificar, suavizar para "desempenhos não comparáveis entre protocolos".
7. Abstract/Seção 4.7: "picture unchanged"/"mesmo sem preprints" → "conclusões qualitativas mantidas", citando o que muda (2026: 15→9; risco baixo 37,0%→28,6%; PD×DD 51,7%→60,9%; código aberto 13,8%→8,7%).
8. Tabela 5: separar "limitação declarada pelos autores" (15/29) de "validação externa observada" (0/29), em colunas ou linhas distintas. Remover/reescrever "Menor acurácia em PD vs. DD" para não contradizer o aviso de não comparabilidade (ex.: "limitação reportada pelos autores").
9. Tabela 6: linha "QA faixa Alta (Média QA)" mistura contagem com média. Separar em duas linhas ("QA Alta: n/N" e "QA média: %"), conferindo 60,6% (revisados), 80,0% (preprints) e 64,6% (total).
10. Zeebaree: padronizar o ano em 2026 (data de DOI/early access) na citação, Tabela 1 e texto, mantendo a nota na referência. Atualizar a chave .bib se necessário.

## Etapa E — Tabela 4 e Tabela 1 (forma e padronização)
- Padronizar rótulos de cenário na Tabela 4 ("PL vs. PD", "DP vs CO", "6 grupos", "PD vs. non-PD", "PD vs. No PD", "Correl. NMS-IMU") mapeando para as categorias da Tabela 1 (PD×HC, PD×DD, 3 classes, DD×HC, Outro, N/A), com o rótulo original entre parênteses só quando necessário.
- Padronizar separador decimal (ponto, em todo o artigo, ou vírgula; escolher um só), casas decimais coerentes (ex.: 0.972868 → 97,29% ou 0.973) e formato de desvio-padrão (±).
- Tabela 4 está estourando a margem: ajustar largura (tabularx/adjustbox/resizebox ou reduzir fonte).
- Tabela 1: reposicionar para não quebrar o parágrafo da Seção 3.3 (float [t]/[!t] ou mover). Ordenar por ano e depois por autor, em vez de row_id (manter coluna ID só se necessário, mantendo consistência com a Tabela 4).
- Adicionar legenda das siglas da Tabela 1 (Vaz., Contrib., Princ./Supl./Val. ext., 3-cl, Mod./Indet., N/A).
- Figuras 2, 4 e 5: rótulos sobrepostos/ilegíveis e hachuras que prejudicam a leitura. Regenerar (se o script existir na pasta) com matplotlib, ajustando tamanho de fonte, separação de rótulos e padrões de hachura distinguíveis (e também em escala de cinza). Se o script não existir, listar o problema no relatório sem recriar do zero.
- Abstract: verificar "peerreviewed" (hífen perdido); conferir hifenização e acentuação no PDF final.

## Etapa F — APENAS SINALIZAR (não editar; o autor conferirá nos PDFs)
Liste no relatório, com evidência da planilha, para cada caso:
1. Abioye et al. 2025: título cita "vocal biomarkers" (o PADS não tem voz) e acurácia 100%. Checar se CI1 se sustenta e o que a planilha registra como modalidade.
2. Ren et al. 2026: coorte cognitiva com análises digitais em amostras independentes. Checar CI1 e o motivo do QA 0%.
3. Padilha et al. 2024 (risco Moderado) vs. Ouabd et al. 2026a (risco Baixo): ambos usam só o PDNMS (uma linha por sujeito). Mostrar os valores de QA3, risco e campos de pré-processamento de cada um e apontar a inconsistência.
4. Padilha 2024/2025 e Lobo 2025 (ERI-GO): verificar coautoria em comum entre si e com o autor do artigo, para declaração em 5.2, se existir.
5. Quaisquer outras divergências numéricas texto × tabela × planilha encontradas durante a recomputação.

## Entrega
1. Artigo atualizado (fonte + PDF compilado sem warnings de overfull/undefined references).
2. CHANGELOG.md com: objetivo, passos executados, lista de alterações (seção, antes → depois, fonte do número), números recomputados, e a seção "Itens sinalizados (Etapa F)" e "Pendências/dúvidas".
3. Nenhum outro arquivo novo. Remova scripts, logs e arquivos temporários.
Responda ao final com um resumo curto: o que mudou, o que ficou pendente e qualquer número que não pôde ser verificado.