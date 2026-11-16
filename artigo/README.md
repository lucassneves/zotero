# Projeto LaTeX — Mapeamento Rápido do Dataset PADS

Projeto compilável no modelo oficial da SBC (`sbc-template.sty` e `sbc.bst`).

## Estrutura
- `main.tex`: documento principal (carrega `sbc-template.sty`, `numeros.tex` e as seções em `secoes/`).
- `referencias.bib`: referências dos 29 estudos incluídos (convertidas de `Aceitos na Rapid Review.bib` para BibTeX clássico compatível com `sbc.bst`), 3 revisões relacionadas (excluídas por CE3), 1 referência metodológica (`garritty_cochrane_2021`) e o registro do dataset no PhysioNet.
- `secoes/`: arquivos individuais por seção (`resumo.tex`, `01-introducao.tex` a `06-conclusao.tex`).
- `tabelas/` e `figuras/`: artefatos LaTeX e figuras vetoriais P&B gerados automaticamente por `scripts/gerar_artefatos.py`.
- `dados/`: cópia preservada de `extracao.xlsx`, tabela auxiliar `metadados_estudos.csv` e relatório de integridade `relatorio_integridade.md`.
- `pendencias.md`: lista automática de todas as marcações `\pend{...}`, desvios/cortes e achados de integridade para revisão com os orientadores.
- `scripts/gerar_artefatos.py`: script interno de reprodução (não citado nem publicado com o artigo).

## Alterações em relação ao `sbc-template.tex` original
- Mantido apenas `\usepackage[utf8]{inputenc}` (acompanhado de `\usepackage[T1]{fontenc}`), removendo a declaração conflitante `\usepackage[latin1]{inputenc}` que quebrava acentos em UTF-8.
- Substituídos os exemplos do meta-artigo pelas seções reais, `\bibliography{referencias}`, `booktabs` e `tikz` (para o fluxo de seleção), sem alterar `sbc-template.sty`, `sbc.bst`, margens, fontes, títulos ou legendas.

## Como reconstruir
1. Gerar macros, tabelas e figuras:
   ```bash
   python scripts/gerar_artefatos.py
   ```
2. Compilar o PDF (via `latexmk` com Perl ou sequência `pdflatex` + `bibtex`):
   ```bash
   latexmk -pdf main.tex
   ```
   ou:
   ```bash
   pdflatex main.tex
   bibtex main
   pdflatex main.tex
   pdflatex main.tex
   ```
