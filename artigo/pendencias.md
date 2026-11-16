# Pendências Consolidadas do Artigo

Documento gerado automaticamente por varredura de marcadores `\pend{...}` em `main.tex` e `secoes/*.tex` (**18 ocorrências**), integrado aos apontamentos do `Roteiro_do_Artigo.md`, de `dados/relatorio_integridade.md` e de `dados/metadados_estudos.csv`.

---

## 1. Marcadores `\pend{...}` no Texto LaTeX (por Seção)

### Cabeçalho e Autoria (`main.tex`)

- *(Sem marcadores `\pend{...}` restantes: autoria preenchida para a disciplina com `Lucas de Sousa Neves`, `Instituto de Informática -- UFG` e `lucass.neves17@discente.ufg.br`; nomes dos orientadores omitidos por enquanto.)*

### Seção 1 — Introdução (`secoes/01-introducao.tex`)

- **Linha 26**: `referência de GQM no Zotero`

### Seção 3 — Método (`secoes/03-metodo.tex`)

- **Linha 7**: `referências metodológicas no Zotero para mapeamento sistemático e PRISMA`
- **Linha 18**: `confirmar adaptação da QP5 (``para a dissertação'') e inclusão de ``veículo'' na QP1 (pendência I3)`
- **Linha 35**: `informar data de execução e corte da busca`
- **Linha 43**: `confirmar interseção Scholar $\times$ Nature`
- **Linha 46**: `confirmar mapeamento 7/1/3/6 por base`
- **Linha 49**: `confirmar lista dos \nSementesSnowballing\ sementes e \nSnowballing\ de forward snowballing`
- **Linha 53**: `data de lançamento do PADS`
- **Linha 62**: `discriminar rejeições por etapa e por CE1--CE6`
- **Linha 82**: `etapas e CE1--CE6`
- **Linha 103**: `validar justificativa para preprints e verificar versões publicadas posteriores (CE4)`
- **Linha 108**: `decidir manutenção de~\cite{padilha_parkinsons_2024} frente a CI3 e sensibilidade sobre~\cite{zannat_label-efficient_2026}`
- **Linha 119**: `formalizar faixas de QA e tratamento N/A (pendência I4)`
- **Linha 127**: `detalhar quem realizou a revisão humana e campos conferidos`
- **Linha 129**: `conferir tabela de metadados de veículo`
- **Linha 131**: `justificar regra de vazamento com literatura no Zotero (pendência I5)`

### Seção 4 — Resultados (`secoes/04-resultados.tex`)

- **Linha 94**: `revisar critério em~\cite{abioye_improving_2025} e multi-base --- pendência I1`

### Seção 6 — Conclusão (`secoes/06-conclusao.tex`)

- **Linha 10**: `decidir se a planilha de extração será anexada, disponibilizada ou apenas descrita`
---

## 2. Itens do Roteiro para Decisão com Orientadores

| Código | Status Atual | Decisão / Ação Necessária |
| --- | --- | --- |
| **B1** | **Resolvido** | `sbc-template.sty` e `sbc.bst` obtidos e mantidos inalterados; codificação unificada em UTF-8 no `main.tex`. |
| **B6** | **Resolvido** | `Aceitos na Rapid Review.bib` exportado e convertido em `referencias.bib` clássico (34 chaves citadas = 34 no `.bib` = 34 no `.bbl`, incluindo `garritty_cochrane_2021` e `PhysioNet-parkinsons-disease-smartwatch-1.0.0`). |
| **B3** | Parcial (com `\pend`) | Informar no Parsifal/texto: data de execução e corte da busca (**O6**), data oficial de lançamento do PADS (CI2), divisão das 62 rejeições por etapa e por CE1–CE6, confirmação da interseção Scholar×Nature (63 comum / 6 só Scholar / 14 só Nature), mapeamento 7/1/3/6 nas bases por string e lista dos 11 estudos-semente e 15 de snowballing. |
| **B4** | Declarado na Seção 4.7 | Confirmar justificativa para inclusão dos 6 *preprints* (CI3/CE2), checar se algum já possui versão revisada por pares publicada (CE4), decidir manutenção de `row_id=108` (Padilha et al., 2024; 2 pág.) frente a CI3, do estudo-semente `row_id=70` (*Incerto*) e sobre o *preprint* `row_id=23` (*não confiável*). |
| **B5** | Preenchido em CSV | Conferir manualmente `dados/metadados_estudos.csv` (especialmente classificação de veículos, DOIs e volume antecipado 2027 de `row_id=79`). |
| **I1** | Destacado em 4.4 e 5.2 | Revisar critério de `Validação externa do Modelo` no `row_id=47` (Abioye et al., 2025; `Papel=Validação externa-generalização`, mas divisão interna no PADS) e nos 11 estudos multibase antes de afirmar `0/29`. |
| **I2** | Declarado em 3.3 e 5.2 | Detalhar quem executou a conferência humana sobre os **138 pontos da aba `revisao`** e se haverá dupla extração em amostra (por exemplo, 5 artigos). |
| **I3** | Adaptado nas QPs | Ratificar inclusão de **veículo** na QP1 e adaptação da QP5 (remoção da menção "para a dissertação"). |
| **I4** | Provisório em 3.3 | Formalizar no protocolo as faixas de QA ($\ge 80\%$, $50\%$--$79\%$, $<50\%$) e a exclusão de itens `N/A` do denominador proporcional. |
| **I5** | Definido em 3.3 | Inserir referências da literatura de engenharia de dados/ML para justificar a regra de classificação do relato de risco de vazamento. |
| **I6** | Parcial (revisão rápida citada) | Referência Cochrane para revisão rápida incluída (`garritty_cochrane_2021`); inserir e citar referências metodológicas para mapeamento sistemático e PRISMA. |
| **I7** | Mitigado em 5.2 | Avaliar necessidade de busca complementar apenas pelo termo PhysioNet/PADS ou manter o viés de cobertura declarado em Ameaças à Validade. |
| **O1** | Aplicado (compacto) | Definido formato condensado das Tabelas 1 e 4 para respeitar o orçamento de 10–12 páginas. |
| **O2** | Pendente na Conclusão | Decidir com orientadores se `dados/extracao.xlsx` será anexada como material suplementar, disponibilizada em repositório ou apenas descrita (scripts construtores permanecem privados por decisão prévia). |
| **O3** | Aplicado (3 revisões) | Selecionadas 3 revisões CE3 recentes na Seção 2.2 (`ouabd_overview_2026`, `pinto_neto_machine_2026`, `shokrpour_machine_2025`). |
| **O4** | Aplicado em 2.1 e 5.1 | Estudo-base (`varghese_machine_2024`) isolado como referência metodológica na Seção 2.1 e confrontado com os sucessores na Seção 5.1. |
| **O5** | Parcial (autoria preenchida) | Autor, afiliação (`Instituto de Informática -- UFG`) e e-mail preenchidos em `main.tex`; orientadores omitidos por enquanto (trabalho da disciplina); checar declaração de uso de IA e agradecimentos. |

---

## 3. Apontamentos de Integridade dos Dados (`dados/relatorio_integridade.md`)

- **Divergências de contagem no PADS v1.0.0 (`276 PD; 79 HC; 114 DD`)**: `row_id=2` reporta `295/71/103`, `row_id=23` reporta `291/79/99` e `row_id=90` apresenta inversão `HC=114; DD=79`.
- **Divergências de ano (Planilha vs. Zotero/PDF)**: `row_id=79` (2026 na planilha/DOI vs. 2027 no volume Zotero), `row_id=40` (2025 no Zotero/planilha vs. 2026 no PDF) e `row_id=49` (2025 no Zotero/planilha vs. 2024 no cabeçalho do PDF).
- **Campos específicos e inconsistências**: `row_id=76` indica IMU com `Sensores` em branco; `row_id=101` declara "IMU de 6 canais" (`Outro`); `row_id=109` tem `Balanceamento = Só no treino` e `aux_preproc_apenas_treino = Não` (resultando em risco `Alto`); `row_id=49` e `row_id=54` são estatísticos (`risco_vazamento = N/A`).
- **Auditoria e revisão humana**: aba `auditoria` está vazia (todos os 1.102 pares nos YAMLs de auditoria foram `CONCORDA`), porém os **138 itens da aba `revisao`** seguem marcados como não resolvidos (`0` resolvidos).
- **Metadados de veículo (`dados/metadados_estudos.csv`)**: 29/29 classificados (`11` periódicos, `12` anais de conferência, `6` preprints, `0` indeterminado), todos com confiança `alta` a partir do Zotero e primeira página dos PDFs.

---

## 4. Ajustes e Cortes por Orçamento de Páginas (Resultado: 12 Páginas)

Para atender estritamente à faixa de **10 a 12 páginas** do modelo SBC sem suprimir achados nem omitir estudos:
1. **Condensação das Tabelas 1 e 4 (Regra 11a / O1)**: Tabela 1 manteve os 29 estudos em ~1 linha por estudo; Tabela 4 reporta apenas o melhor resultado principal de cada estudo em ordem de `row_id`, com abreviação de validação (`HO`, `Anin.`).
2. **Recorte da Seção 2.2 (Regra 11b / O3)**: incluídas 3 revisões relacionadas (`ouabd_overview_2026`, `pinto_neto_machine_2026`, `shokrpour_machine_2025`), excluindo uma quarta candidata para evitar transbordamento das referências para a página 13.
3. **Ajustes visuais e textuais**: largura das Figuras 2 a 5 ajustada (`0.50`–`0.52\textwidth`), colunas da Tabela 1 balanceadas para evitar quebra dupla nas linhas 105 e 109, eliminação de duplicidade `Autor [Autor Ano]` em prosa, revisão narrativa das Seções 4 a 6 com síntese analítica nas tabelas e enxugamento de `Abstract` ($\le 10$ linhas) e `Resumo` (**9 linhas**) na página 1.
