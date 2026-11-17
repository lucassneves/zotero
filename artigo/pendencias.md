# Pendências Consolidadas do Artigo

Documento gerado automaticamente por varredura de marcadores `\pend{...}` em `main.tex` e `secoes/*.tex` (**0 ocorrências restantes**: todas as 18 pendências originais do texto foram resolvidas), integrado aos apontamentos do `Roteiro_do_Artigo.md`, de `dados/relatorio_integridade.md` e de `dados/metadados_estudos.csv`.

---

## 1. Marcadores `\pend{...}` no Texto LaTeX (por Seção)

### Cabeçalho e Autoria (`main.tex`)

- *(Sem marcadores `\pend{...}` restantes: autoria preenchida para a disciplina com `Lucas de Sousa Neves`, `Instituto de Informática -- UFG` e `lucass.neves17@discente.ufg.br`; nomes dos orientadores omitidos por enquanto.)*

### Seção 1 — Introdução (`secoes/01-introducao.tex`)

- *(Sem marcadores `\pend{...}` restantes: GQM vinculado ao protocolo de~\cite{fernandes_interoperability_2018}.)*

### Seção 3 — Método (`secoes/03-metodo.tex`)

- *(Sem marcadores `\pend{...}` restantes: pendências I2, I3, I4, I5, I6, B3, B4 e B5 resolvidas no texto e na Figura 1.)*

### Seção 4 — Resultados (`secoes/04-resultados.tex`)

- *(Sem marcadores `\pend{...}` restantes: pendência I1 resolvida com 0/29 de validação externa e explicação contida sobre~\cite{abioye_improving_2025} e os estudos multibase.)*

### Seção 6 — Conclusão (`secoes/06-conclusao.tex`)

- *(Sem marcadores `\pend{...}` restantes: decisão O2 registrada — planilha de extração não será disponibilizada externamente.)*
---

## 2. Itens do Roteiro para Decisão com Orientadores

| Código | Status Atual | Decisão / Ação Necessária |
| --- | --- | --- |
| **B1** | **Resolvido** | `sbc-template.sty` e `sbc.bst` obtidos e mantidos inalterados; codificação unificada em UTF-8 no `main.tex`. |
| **B6** | **Resolvido** | `Aceitos na Rapid Review.bib` exportado e convertido em `referencias.bib` clássico (`37` chaves citadas = `37` no `.bib` = `37` no `.bbl`, incluindo `garritty_cochrane_2021`, `fernandes_interoperability_2018`, `kapoor_leakage_2023`, `vandewiele_overly_2021` e `PhysioNet-parkinsons-disease-smartwatch-1.0.0`). |
| **B3** | **Resolvido** | Datas confirmadas (PADS: 05/01/2024 artigo / 25/03/2024 PhysioNet; busca 12/11/2026, consolidação até 13/11/2026), mapeamento 7/1/3/6, Scholar×Nature (69/77; 63 comum; 83 união), 11 sementes / 15 snowballing e 62 rejeições (31 CE1, 21 CE3, 10 CE2; 4 metadados e 58 texto completo) aplicados em `03-metodo.tex` e Figura 1. |
| **B4** | **Resolvido** | Justificativa declarada para manutenção dos 6 *preprints* (base recente de 2024, corpus revisado reduzido $n=23$, sem versões publicadas posteriores encontradas) com análise de sensibilidade na Seção 4.7; mantidos também `row_id=108` (Padilha et al., 2024; 2 pág. em anais revisados por pares) e `row_id=23` (Zannat, 2026; sinalizado como risco Alto). |
| **B5** | **Resolvido** | Metadados de publicação e veículo dos 29 estudos (`dados/metadados_estudos.csv`) conferidos pelo autor contra Zotero e primeira página dos PDFs (`11` periódicos, `12` anais, `6` preprints). |
| **I1** | **Resolvido** | Confirmado `0/29` de validação externa independente nos YAMLs e registrado em forma contida na Seção 4.4 (esclarecendo que `row_id=47` e os 11 multibase retreinaram/avaliaram internamente no PADS). |
| **I2** | **Resolvido** | Registrado na Seção 3.3 e na Seção 5.2 que a extração e a segunda rodada de conferência integral foram conduzidas por um único pesquisador (o autor), sem extração independente em duplicata nem cálculo de $\kappa$ (alinhado ao recorte de *rapid review* em `garritty_cochrane_2021`), omitindo menção a IA no texto por opção do autor. |
| **I3** | **Resolvido** | Ratificada QP1 com "veículo" (referente aos veículos de publicação dos 29 estudos analisados) e adaptada a QP5 para "lacunas e oportunidades de pesquisa na área". |
| **I4** | **Resolvido** | Formalizadas as faixas de QA ($\ge 80\%$, $50\%$--$79\%$, $<50\%$) e a exclusão de itens `N/A` do denominador proporcional (`nota_qa_pct`). |
| **I5** | **Resolvido** | Regra de classificação do risco de vazamento fundamentada na Seção 3.3 com `kapoor_leakage_2023`, `vandewiele_overly_2021` e `djemaa_quantifying_2026` (separação treino/teste, não independência de amostras por sujeito, pré-processamento e sobreamostragem pré-*split*). |
| **I6** | **Resolvido** | Referência de revisão rápida (`garritty_cochrane_2021`) combinada à estrutura de protocolo de mapeamento sistemático (`fernandes_interoperability_2018`, com adaptação prospectiva no *snowballing*); menção a PRISMA removida do texto. |
| **I7** | Mitigado em 5.2 | Avaliar necessidade de busca complementar apenas pelo termo PhysioNet/PADS ou manter o viés de cobertura declarado em Ameaças à Validade. |
| **O1** | Aplicado (compacto) | Definido formato condensado das Tabelas 1 e 4 para respeitar o orçamento de 10–12 páginas. |
| **O2** | **Resolvido** | Planilha `dados/extracao.xlsx` não será disponibilizada externamente; seus dados permanecem apenas descritos e sintetizados no artigo (registrado na Conclusão). |
| **O3** | Aplicado (3 revisões) | Selecionadas 3 revisões CE3 recentes na Seção 2.2 (`ouabd_overview_2026`, `pinto_neto_machine_2026`, `shokrpour_machine_2025`). |
| **O4** | Aplicado em 2.1 e 5.1 | Estudo-base (`varghese_machine_2024`) isolado como referência metodológica na Seção 2.1 e confrontado com os sucessores na Seção 5.1. |
| **O5** | **Resolvido (escopo disciplina)** | Autor, afiliação (`Instituto de Informática -- UFG`) e e-mail preenchidos em `main.tex`; orientadores omitidos para entrega da disciplina e menção a assistência de IA omitida do manuscrito por decisão do autor. |

---

## 3. Apontamentos de Integridade dos Dados (`dados/relatorio_integridade.md`)

- **Divergências de contagem no PADS v1.0.0 (`276 PD; 79 HC; 114 DD`)**: `row_id=2` reporta `295/71/103`, `row_id=23` reporta `291/79/99` e `row_id=90` apresenta inversão `HC=114; DD=79`.
- **Divergências de ano (Planilha vs. Zotero/PDF)**: `row_id=79` (2026 na planilha/DOI vs. 2027 no volume Zotero), `row_id=40` (2025 no Zotero/planilha vs. 2026 no PDF) e `row_id=49` (2025 no Zotero/planilha vs. 2024 no cabeçalho do PDF).
- **Campos específicos e inconsistências**: `row_id=76` indica IMU com `Sensores` em branco; `row_id=101` declara "IMU de 6 canais" (`Outro`); `row_id=109` (`Lobo et al., 2025`) teve `risco_vazamento` revisado para `Moderado` (e `QA3=0,5`) por separar participantes e restringir `SMOTE` ao treino, omitindo apenas o escopo do *z-score*; `row_id=49` e `row_id=54` são estatísticos (`risco_vazamento = N/A`).
- **Auditoria e revisão humana**: aba `auditoria` está vazia (todos os 1.102 pares nos YAMLs de auditoria foram `CONCORDA`), porém os **138 itens da aba `revisao`** seguem marcados como não resolvidos (`0` resolvidos).
- **Metadados de veículo (`dados/metadados_estudos.csv`)**: 29/29 classificados (`11` periódicos, `12` anais de conferência, `6` preprints, `0` indeterminado), todos com confiança `alta` a partir do Zotero e primeira página dos PDFs.

---

## 4. Ajustes e Cortes por Orçamento de Páginas (Resultado: 12 Páginas)

Após fechar todas as pendências (`0` `\pend` restantes) e compilar `main.pdf` localmente via TinyTeX (`pdflatex` + `bibtex`, com `0` erros e `0` avisos), o manuscrito foi ajustado para fechar estritamente em **12 páginas** sem perda de dados nem corte de estudos:
1. **Condensação das Tabelas 1, 4 e 5 (Regra 11a / O1)**: Tabela 1 mantida em `0.98\textwidth` (`tabular*`) em página compartimentada; Tabela 4 alargada para `0.98\textwidth` reduzindo quebras multilinhas; Tabela 5 com `2` citações representativas por tema (`e +N`) e rótulos concisos.
2. **Recorte da Seção 2.2 (Regra 11b / O3)**: mantidas as 3 revisões relacionadas (`ouabd_overview_2026`, `pinto_neto_machine_2026`, `shokrpour_machine_2025`).
3. **Figuras 2--5 e Tabela 6 padronizadas**: todas as figuras de dados (2 a 5) e a Tabela 6 padronizadas em `0.78\textwidth` (com proporções ajustadas em Matplotlib nas Figuras 2--5 e fluxo da Figura 1 corrigido para desviar do bloco de incluídos), mantendo alta legibilidade e equilíbrio visual.
4. **Enxugamento textual sem perda factual**: condensação de redundâncias nas Seções 1, 2, 3, 4.3–4.7, 5 e 6, preservando todos os números por macro, a síntese de pré-processamento `QP3` e as `37` referências bibliográficas até a página 12.
