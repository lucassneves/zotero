# Prompt — Construção do Artigo em LaTeX (modelo SBC)

Prompt para uma IA com acesso a arquivos (IDE ou agente) montar o **projeto completo e compilável** do artigo, em LaTeX, a partir da planilha de extração e do protocolo. O resultado é um **rascunho** para discutir com os orientadores, com as pendências visíveis no texto.

## 1. Arquivos que a IA precisa receber

| Arquivo | Para quê |
| --- | --- |
| `extracao.xlsx` | Dados dos 29 estudos (abas `extracao`, `evidencias`, `qa`, `revisao`, `dicionario`). |
| Protocolo (`.docx` exportado do Parsifal) | Objetivo GQM, PICOC, QP, strings, fontes, critérios CI/CE, QA e formulário. |
| `Roteiro_do_Artigo.md` | Estrutura, mapa QP → campos → artefatos, orçamento de páginas e pendências conhecidas. |
| `sbc-template.tex` (já recebido) e **`sbc-template.sty` e `sbc.bst` (ainda necessários)** | Formatação oficial. O `.tex` carrega `\usepackage{sbc-template}` e depende do `.sty`; a bibliografia usa `sbc.bst`. O `sbc_template.odt` serve de especificação de estilo. |
| `referencias.bib` (exportado do Zotero) | Única fonte de referências (29 estudos, PADS e método). |
| Acesso ao Zotero (ou aos PDFs) dos 29 estudos | Para obter tipo de publicação, veículo e DOI (passo 2b); sem isso, esses campos ficam "indeterminado". |
| Descritor do PADS e artigo de ML no PADS (PDFs do projeto) | Base factual da seção de contexto. |

Sem `sbc-template.sty`/`sbc.bst` e sem o `.bib`, o prompt ainda funciona: a IA gera um `main.tex` provisório com preâmbulo de contingência e marca as referências como pendentes. Mas o resultado é provisório.

## 2. Prompt

````text
PAPEL E OBJETIVO
Você é coautor técnico e revisor de um artigo científico de computação aplicada à saúde. Sua tarefa é CONSTRUIR O PROJETO COMPLETO, em LaTeX, de um artigo no modelo da SBC (Sociedade Brasileira de Computação) sobre uma rapid review (mapeamento sistemático rápido) dos estudos que usam o dataset PADS, escrita como trabalho da disciplina de Metodologia de Pesquisa (não há evento-alvo) (Parkinson's Disease Smartwatch dataset). O resultado é um RASCUNHO COMPLETO E COMPILÁVEL, com texto, tabelas e figuras gerados a partir dos dados, que o autor vai discutir com os orientadores. Pendências conhecidas devem aparecer explícitas no texto e em uma lista; nunca as esconda nem as preencha com suposições.

PARÂMETROS (já definidos pelo autor)
IDIOMA_DO_ARTIGO: pt (resumo em português e abstract em inglês)
CONTEXTO: trabalho da disciplina de Metodologia de Pesquisa; rapid review conforme o protocolo; sem evento-alvo (o modelo SBC é apenas o formato)
LIMITE_DE_PAGINAS: 10 a 12 páginas, incluindo referências (meta: 11)
AUTORES_E_AFILIACOES: placeholder, até o autor informar

ARQUIVOS DE ENTRADA (use somente estes; não use conhecimento externo sobre os estudos)
- extracao.xlsx: aba "extracao" (1 linha por estudo; colunas com os nomes exatos do Parsifal, mais aux_*, risco_vazamento, QA1 a QA5, nota_qa, nota_qa_max, nota_qa_pct, faixa_qa); abas "evidencias", "qa", "revisao" e "dicionario" para conferência. Campos Select Many vêm separados por "; ".
- Protocolo (docx), ROTEIRO_DO_ARTIGO.md, sbc-template.tex, sbc-template.sty, sbc.bst (e o guia .odt), referencias.bib, PDFs do PADS.

FLUXO DE SELEÇÃO (fornecido pelo autor; use exatamente estes números e não derive outros)
- Registros importados no Parsifal: 115 = 69 (citações do artigo-base do PADS no Google Scholar) + 14 (citações do artigo-base que estavam só na Nature Citations) + 15 (snowballing: citações de 11 estudos-semente, sem duplicatas, incluindo o artigo-base; o protocolo os conta dentro de "Google Scholar: 84") + 17 (buscas por string: IEEE Xplore 7, PubMed Central 1, ScienceDirect 3, Scopus 6; o mapeamento por base segue a ordem do protocolo e está a confirmar). A composição dos 15 do snowballing e dos 11 estudos-semente também está a confirmar.
- Nature Citations recuperou 77 citações do artigo-base; 14 não estavam no Google Scholar. Derivado, a confirmar pelo autor: 63 em comum, 6 só no Google Scholar e união de 83 (use \pend{confirmar} ao citar esses três números).
- Resultado no Parsifal: 24 duplicados, 62 rejeitados e 29 aceitos (24 + 62 + 29 = 115). Triados após remover duplicatas: 91.
- NÃO informados (use \pend): data da busca; data de lançamento do PADS (CI2); rejeições por etapa (título e resumo × texto completo) e por critério (CE1 a CE6).
- Descreva as fontes em 3.3 e 3.4 por ORIGEM (citações do artigo-base, buscas por string e snowballing), e não pelo rótulo do protocolo, que mistura citações diretas e snowballing. Inclua uma \pend pedindo ao autor a confirmação desta composição.
- A rota principal é por citações do artigo-base: descreva isso no método e como ameaça à validade (estudos que não citam o artigo-base e não foram recuperados pelas strings podem ter ficado de fora).

REGRAS INEGOCIÁVEIS
1. Dados: todo número, contagem e percentual vem de extracao.xlsx, do protocolo ou do bloco FLUXO DE SELEÇÃO. Nunca use valores "plausíveis", de memória ou de outros artigos.
2. Números por script: crie scripts/gerar_artefatos.py (bibliotecas prontas: pandas, openpyxl, matplotlib; sem reinventar funções) que leia dados/extracao.xlsx e gere (a) numeros.tex, com macros \newcommand para todo número usado no texto; (b) tabelas/*.tex; (c) figuras/*.pdf. O texto usa as macros, não números digitados à mão. Rode o script e confira.
3. Denominadores explícitos: informe n/29, ou n/27 quando houver "Não se aplica" (por exemplo, risco de vazamento). Mostre "Não reportado" e "Não se aplica" como categorias, sem escondê-las. Campos multirrótulo: informe que a soma passa de 100%.
4. Referências: use somente as de referencias.bib. Associe os 29 estudos pelo título (aux_titulo) e pela chave do Zotero (aux_zotero_key); se não houver correspondência exata, não invente autor, ano, DOI nem veículo: escreva \pend{referência do row_id N} e registre na lista de pendências. Nunca fabricar citações.
5. Pendências: defina \newcommand{\pend}[1]{\textbf{[PENDÊNCIA: #1]}} (sem cor; o modelo SBC é preto e branco). Gere pendencias.md varrendo \pend{...} em secoes/*.tex (módulo re), agrupado por seção. Onde faltarem dados (por exemplo, data da busca, rejeições por etapa e por critério, procedimento de validação da extração), use \pend, nunca um valor inventado.
6. Rigor do mapeamento: é um estudo descritivo. Não ranqueie estudos por desempenho. Não compare acurácias entre cenários, métricas ou validações diferentes. Apresente "melhor resultado reportado" sempre com cenário, métrica e tipo de validação, em ordem de row_id. Sem afirmações causais. Use "reportado" e "relatado". O risco de vazamento é uma CLASSIFICAÇÃO DO RELATO dos autores, não prova de vazamento.
7. Transparência sobre IA: a extração foi assistida por IA com revisão humana. Declare isso na seção de método e na discussão de ameaças. Os detalhes (modelo usado, quem revisou, o que foi conferido) devem ser fornecidos pelo autor: use \pend onde faltarem. Não afirme dupla extração, concordância entre avaliadores ou kappa, porque não foram feitos.
8. Fidelidade ao protocolo: reproduza GQM, PICOC, QP1 a QP5, strings, fontes, CI1 a CI4, CE1 a CE6, QA1 a QA5 e o formulário como estão no docx, resumindo só para caber. Se os dados contradisserem o protocolo (por exemplo, um preprint incluído apesar do CE2, ou o status "Incerto – texto completo"), NÃO corrija em silêncio: registre em pendencias.md.
9. Direitos autorais: parafraseie. Não copie trechos de artigos de terceiros; citação literal só se indispensável, curta e com referência.
10. Estilo: português científico claro (ou inglês, conforme IDIOMA_DO_ARTIGO), voz impessoal ou primeira pessoa do plural, de forma consistente; frases curtas; siglas definidas na primeira ocorrência (PD, HC, DD, IMU, PDNMS, QA, QP); sem adjetivos promocionais. Cada parágrafo de resultados responde a uma QP e começa pela mensagem principal.
11. Limite de páginas: 10 a 12 páginas, incluindo referências (meta 11). Não fique abaixo de 10 nem acima de 12. Se estourar, nesta ordem: (a) condense a tabela dos 29 estudos (colunas essenciais ou fonte menor), (b) reduza trabalhos relacionados, (c) condense figuras. Não há material suplementar nesta entrega: o conteúdo precisa caber no artigo. Registre o corte em pendencias.md.
12. Scripts de uso interno: scripts/ e o README servem só para reconstruir o PDF e NÃO serão publicados. O artigo não deve citar repositório de scripts nem prometer disponibilizá-los; descreva o método no texto. Sobre a planilha de extração, escreva \pend{decidir se a planilha será anexada, disponibilizada ou apenas descrita}.
13. Literatura cinzenta (preprints): o protocolo (CE2 e CI3) exclui preprints e literatura cinzenta, mas o autor optou por INCLUIR os preprints encontrados. O artigo deve: (a) declarar isso como desvio consciente do protocolo, com a justificativa fornecida pelo autor (use \pend no que faltar; argumento candidato, a validar: o PADS é recente e boa parte da produção de 2025 e 2026 pode ainda não ter versão revisada por pares); (b) informar quantos dos 29 são preprints, a partir de dados/metadados_estudos.csv; (c) descrever os achados de forma DESCRITIVA, comparando preprints e estudos revisados por pares em ano, tipo de contribuição, cenário, família de algoritmo, separação por participante, risco de vazamento, faixa de QA e código/dados; (d) fazer análise de sensibilidade dos resultados principais com e sem preprints; (e) tratar o tema em 3.4 (método), 4.7 (resultados), na discussão e nas ameaças à validade. Sem testes inferenciais (n pequeno) e sem afirmar que preprints são melhores ou piores.
14. Metadados de publicação: veículo e tipo de publicação NÃO estão na planilha e o autor não os conhece. Obtenha-os do registro do Zotero (tipo de item, título da publicação, repositório, DOI) e da primeira página do PDF, nunca de memória. Registre evidência e confiança; use "indeterminado" quando não puder confirmar. Esses dados são provisórios e devem ser conferidos pelo autor.

ESTRUTURA DO ARTIGO
Siga o ROTEIRO_DO_ARTIGO.md: Resumo/Abstract (até 10 linhas cada); 1 Introdução; 2 Contexto (PADS, estudo-base de ML no PADS, revisões relacionadas); 3 Método (inclui o desvio do protocolo sobre preprints em 3.4); 4 Resultados (4.1 a 4.6, na ordem das QP, mais qualidade e reprodutibilidade; e 4.7 Literatura cinzenta: preprints); 5 Discussão (achados, implicações, ameaças à validade); 6 Conclusão; Referências. Use o mapa QP → campos → artefatos do roteiro:
- Figuras (preto e branco ou tons de cinza, com hachuras; vetoriais em PDF; legenda em Helvetica 10 negrito): 1 fluxo de seleção (TikZ, com os números do bloco FLUXO DE SELEÇÃO; etapas sem número ficam como \pend), 2 estudos por ano e tipo de contribuição, 3 cenário × família de algoritmo, 4 risco de vazamento por unidade de particionamento e separação por participante, 5 QA1 a QA5.
- Tabelas (legenda antes da tabela; sem cor, sem fundo sombreado, sem molduras desnecessárias; booktabs): 1 estudos incluídos (compacta), 2 recorte do PADS, 3 validação e vazamento, 4 desempenho reportado (ordem de row_id), 5 lacunas, 6 preprints × revisados por pares (compacta).
- Mensagem central do roteiro = hipótese de trabalho: só a mantenha se os dados a sustentarem; caso contrário, reescreva e avise.
- Em 4.6 (lacunas), sintetize por tema os textos livres de "Limitações Reportadas" e "Lacuna identificada pelos autores" (sem citar frases literais) e relacione com os campos de código/dados e com o QA.
- Em 4.7 (literatura cinzenta), siga a regra 13: situação, contagem, comparação descritiva, análise de sensibilidade e implicações, em cerca de meia página.

FORMATAÇÃO SBC
- TEMPLATE RECEBIDO: o arquivo sbc-template.tex é a base de main.tex. Ele carrega \usepackage{sbc-template} (arquivo sbc-template.sty, que define \inst, \address, \nextinstitute, \email e o ambiente resumo) e usa \bibliographystyle{sbc} (sbc.bst). Preserve a estrutura: \documentclass[12pt]{article}, \usepackage{sbc-template}, \sloppy, \title, \author com \inst{n}, \address com \nextinstitute e \email, \maketitle, ambiente abstract e, em português, ambiente resumo.
  a) Substitua TODO o texto de instruções do meta-artigo pelo conteúdo do artigo; remova as figuras e a tabela de exemplo (fig1.jpg, fig2.jpg, table.jpg) e as chaves de exemplo (knuth:84, boulic:91, smith:99).
  b) Codificação: o arquivo está em UTF-8, mas declara \usepackage[utf8]{inputenc} e depois \usepackage[latin1]{inputenc}, o que conflita e quebra os acentos. Mantenha apenas \usepackage[utf8]{inputenc} e registre a alteração no README.md.
  c) Idioma: \usepackage[brazil]{babel} para pt. Para en, use \usepackage[english]{babel} e remova o ambiente resumo.
  d) Bibliografia: troque \bibliography{sbc-template} por \bibliography{referencias}; compile com latexmk -pdf (usa bibtex) e use os comandos de citação do template (\cite).
  e) Não altere sbc-template.sty nem sbc.bst, e não adicione pacotes que mudem margens, fontes, títulos ou legendas.
- Se sbc-template.sty ou sbc.bst NÃO estiverem disponíveis, o main.tex original não compila. Nesse caso, gere um main.tex PROVISÓRIO com o preâmbulo de contingência abaixo (que reimplementa \inst, \address, \nextinstitute, \email, \maketitle, abstract e resumo), use natbib com \citep e \bibliographystyle{plainnat}, e escreva no README.md e em pendencias.md: "formatação provisória; trocar pelo template oficial (sbc-template.sty e sbc.bst)".
- Especificação (do guia da SBC): A4, coluna única; margens superior 3,5 cm, inferior 2,5 cm, laterais 3,0 cm; sem cabeçalho, rodapé nem número de página; fonte Times 12 pt com 6 pt antes de cada parágrafo; título centralizado, 16 pt negrito, 12 pt antes; autores centralizados, 12 pt negrito, na mesma linha, separados por vírgulas; endereços centralizados, 12 pt; e-mails em Courier 10 pt; resumo/abstract em 12 pt, recuo de 0,8 cm nos dois lados, com a palavra Resumo/Abstract em negrito; títulos de seção em negrito 13 pt, alinhados à esquerda, 12 pt antes; subseções em negrito 12 pt; primeiro parágrafo de cada seção sem recuo e os seguintes com 1,27 cm; legendas em Helvetica 10 pt negrito, centralizadas se couberem em uma linha, senão justificadas com recuo de 0,8 cm; legenda de tabela antes da tabela; referências em 12 pt, 6 pt antes de cada uma, primeira linha sem recuo e demais com 0,5 cm; citações no formato [Autor Ano] ou Autor (Ano).
- Preâmbulo de contingência (compilado em teste, exceto o idioma brasileiro do babel, que não existia no ambiente de teste; se faltar, instale o pacote de português do TeX ou ajuste o idioma):
  \documentclass[12pt,a4paper]{article}
  \usepackage[T1]{fontenc} \usepackage[utf8]{inputenc} \usepackage[english,brazilian]{babel}
  \usepackage{mathptmx} \usepackage[scaled=.92]{helvet} \usepackage{courier}
  \usepackage[top=3.5cm,bottom=2.5cm,left=3cm,right=3cm]{geometry}
  \usepackage{titlesec} \usepackage{indentfirst} \usepackage{booktabs,graphicx,natbib}
  \usepackage[labelfont={bf,sf},textfont={bf,sf},font=small,justification=justified,singlelinecheck=true,margin=0.8cm,skip=6pt]{caption}
  \pagestyle{empty} \setlength{\parindent}{1.27cm} \setlength{\parskip}{6pt}
  \titleformat{\section}{\bfseries\fontsize{13}{15}\selectfont}{\thesection}{0.6em}{} \titlespacing*{\section}{0pt}{12pt}{6pt}
  \titleformat{\subsection}{\bfseries\fontsize{12}{14}\selectfont}{\thesubsection}{0.6em}{} \titlespacing*{\subsection}{0pt}{12pt}{6pt}
  \makeatletter
  \newcommand{\inst}[1]{\textsuperscript{#1}} \newcommand{\nextinstitute}{\par\vspace{6pt}\noindent}
  \newcommand{\email}[1]{{\ttfamily\fontsize{10}{12}\selectfont #1}} \def\address#1{\gdef\@address{#1}}
  \renewcommand{\maketitle}{\begin{center}\vspace{12pt}{\bfseries\fontsize{16}{19}\selectfont \@title\par}\vspace{12pt}{\bfseries \@author\par}\vspace{12pt}{\@address\par}\vspace{12pt}\end{center}}
  \makeatother
  \renewenvironment{abstract}{\list{}{\leftmargin0.8cm\rightmargin0.8cm}\item[]\textbf{Abstract.} }{\endlist}
  \newenvironment{resumo}{\list{}{\leftmargin0.8cm\rightmargin0.8cm}\item[]\textbf{Resumo.} }{\endlist}
  Nesse caso, o primeiro parágrafo de cada seção deve usar \noindent.

ESTRUTURA DO PROJETO (crie exatamente)
  artigo/
    main.tex  sbc-template.sty  sbc.bst  referencias.bib  numeros.tex  pendencias.md  README.md
    secoes/ (resumo, 01-introducao, 02-contexto, 03-metodo, 04-resultados, 05-discussao, 06-conclusao)
    tabelas/  figuras/  dados/extracao.xlsx  dados/metadados_estudos.csv  scripts/gerar_artefatos.py (uso interno)

PROCESSO (siga a ordem)
0. Inventário: liste os arquivos recebidos e diga o que falta (template LaTeX oficial, .bib, parâmetros). Continue com contingência quando possível.
1. Leia o protocolo, o roteiro, todas as abas da planilha, os dados do PADS e a especificação SBC.
2. Integridade dos dados ANTES de escrever. Verifique: 29 linhas; row_id únicos; rótulos dentro das opções do dicionário; soma de N° por classe = N° de participantes quando ambos existem; Papel do PADS = "Validação externa-generalização" com "Validação externa do Modelo" = Não; estudos com mais de uma base e nenhuma validação externa; totais do fluxo de seleção (115 importados × 80 + 24 + 29); status de triagem fora de Aceito / Aceito, mas com Ressalvas / Aceito, mas com Ressalvas, não confiável; anos fora do intervalo esperado. Grave dados/relatorio_integridade.md. NÃO altere a planilha; trate cada achado como pendência.
2b. Metadados de publicação (regra 14): crie dados/metadados_estudos.csv (pandas) com row_id, aux_zotero_key, titulo, tipo_publicacao (periódico | anais de conferência | preprint | outro | indeterminado), veiculo, repositorio, doi, evidencia, confianca. Use-o em 4.1 (veículo e tipo) e 4.7 (preprints). Não altere a planilha.
3. Crie a estrutura do projeto.
4. Escreva e rode scripts/gerar_artefatos.py (numeros.tex, tabelas, figuras).
5. Escreva as seções, uma por arquivo, seguindo o roteiro e usando as macros.
6. Compile com latexmk -pdf; corrija erros e avisos (overfull hbox, referências e figuras indefinidas), exceto as citações marcadas como pendentes.
7. REVISÃO INTERNA OBRIGATÓRIA antes de entregar:
   a) todo número do texto vem de uma macro e confere com a planilha (reabra 5 números ao acaso);
   b) toda \cite resolve no .bib; nenhuma referência inventada;
   c) toda figura e tabela é citada no texto e a legenda está no padrão SBC;
   d) cada QP é respondida em 4.x com denominador explícito;
   e) nenhuma afirmação de ranking, causalidade ou "melhor modelo";
   f) nenhuma afirmação sobre dupla extração, kappa ou validação externa que a planilha não sustente;
   g) o número de páginas respeita o limite; resumo com no máximo 10 linhas;
   h) pendencias.md lista todos os \pend, os cortes e os achados de integridade.
   i) a seção 4.7 existe, com contagem vinda de metadados_estudos.csv e sem juízo de valor sobre preprints;
   j) o texto não promete publicar scripts nem cita repositório.
8. Limpeza: apague arquivos intermediários (.aux, .log, .bbl, .blg, .out, .fls, .fdb_latexmk, .synctex.gz, __pycache__, rascunhos). Mantenha só o projeto, main.pdf, pendencias.md e dados/relatorio_integridade.md.
9. Escrita em arquivos: grave apenas dentro de artigo/. Não altere a planilha, o protocolo nem o roteiro. Se artigo/ já existir, não sobrescreva: pare e avise.

RESPOSTA FINAL (curta)
Objetivo do pedido; passos executados; resultado (arquivos gerados, número de páginas, número de pendências por seção, achados de integridade mais importantes); e o que o autor precisa decidir com os orientadores. Termos técnicos, de forma resumida.

ENTRADA
IDIOMA_DO_ARTIGO: pt
CONTEXTO: trabalho da disciplina de Metodologia de Pesquisa (rapid review), sem evento-alvo
LIMITE_DE_PAGINAS: 10 a 12 (meta 11), incluindo referências
AUTORES_E_AFILIACOES: placeholder
````

## 3. Como usar

1. Coloque numa pasta única: `extracao.xlsx`, o protocolo, `Roteiro_do_Artigo.md`, `sbc-template.tex`, `sbc-template.sty`, `sbc.bst`, o `referencias.bib` e os PDFs do PADS.
2. Os parâmetros já estão preenchidos (português, disciplina de Metodologia de Pesquisa, 10 a 12 páginas). Falta só informar autores e afiliações no final do prompt.
3. Peça à IA que rode tudo (script, compilação e revisão) e devolva `main.pdf` e `pendencias.md`.
4. Leve `pendencias.md` e a seção 6 do roteiro para a conversa com os orientadores.
5. Quando as pendências forem resolvidas, atualize a planilha e rode de novo `scripts/gerar_artefatos.py`: os números do texto se atualizam pelas macros.

## 4. Cuidados

- **Template:** o `sbc-template.tex` foi recebido, mas depende de `sbc-template.sty` e `sbc.bst`. Baixe-os do mesmo pacote da SBC; até lá, o preâmbulo de contingência garante uma formatação aproximada.
- **Codificação:** o `sbc-template.tex` está em UTF-8, mas declara também `\usepackage[latin1]{inputenc}`, o que conflita com o `utf8` e quebra acentos. O prompt manda manter só `utf8`.
- **Referências:** é fundamental exportar o `.bib` do Zotero. Sem ele, o rascunho terá marcas de pendência no lugar das citações.
- **Números:** a planilha precisa estar validada antes da versão final; o script reproduz qualquer ajuste.
- **IA no texto:** a redação feita por IA precisa de revisão do autor. A conferência dos números e das citações (passo 7) não substitui a leitura crítica.
- **Preprints:** foram incluídos apesar do CE2 e do CI3. O artigo os trata como desvio declarado do protocolo, em seção própria. Peça aos orientadores a validação da justificativa.
- **Veículo e tipo de publicação:** obtidos pela IA no Zotero e no PDF, e portanto provisórios; confira os casos "indeterminado".
- **Scripts:** não serão publicados; o texto não deve citar repositório.
- **Política da disciplina:** verifique as regras sobre uso de IA na redação e na extração, e declare-o quando exigido.
