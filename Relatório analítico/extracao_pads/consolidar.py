#!/usr/bin/env python3
"""consolidar.py: consolida raw/*.yaml (extração da IA) em extracao.xlsx.

Uso:
    python consolidar.py
Se existir a pasta auditoria/ (saída do modo AUDITORIA), adiciona a aba 'auditoria' com os
campos em que a auditoria discorda ou não consegue verificar.
Requer: pip install pyyaml pandas openpyxl
"""
import re
from pathlib import Path

import pandas as pd
import yaml

RAW, AUDITORIA, SAIDA, SEP = Path("raw"), Path("auditoria"), Path("extracao.xlsx"), "; "

# (id, chave, nome no Parsifal, tipo)  tipo: int | str | one | many | bool
CAMPOS = [
    (1, "row_id", "ID do Registro (row_id)", "int"),
    (2, "ano_publicacao", "Ano de Publicação", "str"),
    (3, "tipo_contribuicao", "Tipo de Contribuição", "one"),
    (4, "outra_contribuicao", "Outra Contribuição", "str"),
    (5, "papel_pads", "Papel do PADS", "one"),
    (6, "datasets", "Datasets", "many"),
    (7, "outros_datasets", "Outros Datasets", "str"),
    (8, "modalidade_pads", "Modalidade do PADS", "many"),
    (9, "tarefas_pads", "Tarefas do PADS", "one"),
    (10, "quais_tarefas_pads", "Quais tarefas PADs", "str"),
    (11, "sensores", "Sensores", "many"),
    (12, "outros_sensores", "Outros Sensores", "str"),
    (13, "punhos", "Punho(s) usado(s)", "one"),
    (14, "n_participantes", "N° de participantes", "int"),
    (15, "n_por_classe", "N° por classe: PD / HC / DD", "str"),
    (16, "cenarios_classificacao", "Cenários de classificação", "many"),
    (17, "outro_cenario", "Outro Cenários de classificação", "str"),
    (18, "representacao_entrada", "Representação de entrada", "many"),
    (19, "outra_representacao", "Outra Representação de entrada", "str"),
    (20, "familia_algoritmo", "Família do Algoritmo", "many"),
    (21, "outra_familia", "Outra Família do Algoritmo", "str"),
    (22, "especificacao_algoritmo", "Espeçificação do Algoritmo", "str"),
    (23, "balanceamento_augmentation", "Balanceamento/augmentation", "one"),
    (24, "estrategia_validacao", "Estratégia de Validação", "many"),
    (25, "outra_estrategia_validacao", "Outra Estratégia de Validação", "str"),
    (26, "unidade_particionamento", "Unidade de particionamento (partitioning unit)", "one"),
    (27, "separacao_participante", "Separação por participante (subject-level separation)", "one"),
    (28, "momento_balanceamento", "Balanceamento", "one"),
    (29, "detalhes_balanceamento", "Detalhes do balanceamento (Caso Aplicado)", "str"),
    (30, "validacao_externa", "Validação externa do Modelo", "bool"),
    (31, "metricas", "Métricas de avaliação", "many"),
    (32, "outras_metricas", "Outras Métricas de avaliação", "str"),
    (33, "melhor_resultado", "Melhor resultado (Evaluation Values)", "str"),
    (34, "demais_valores", "Demais valores", "str"),
    (35, "codigo_dados", "Código/dados disponíveis", "one"),
    (36, "limitacoes", "Limitações Reportadas", "str"),
    (37, "lacuna", "Lacuna identificada pelos autores", "str"),
    (38, "notas_revisor", "Notas do revisor", "str"),
]

OPCOES = {
    "tipo_contribuicao": ["Análise estatística", "Estudo comparativo", "Novo modelo", "Outro", "Plataforma-sistema"],
    "papel_pads": ["Análise suplementar", "Principal", "Validação externa-generalização"],
    "datasets": ["Outro público", "PADS", "Privado-próprio"],
    "modalidade_pads": ["Metadados demográficos-clínicos", "Questionário (PDNMS)", "Série temporal (IMU)"],
    "tarefas_pads": ["Não reportado", "Não se aplica", "Subconjunto", "Tarefa única", "Todas"],
    "sensores": ["Acelerômetro", "Giroscópio", "Outro"],
    "punhos": ["Ambos", "Direito", "Esquerdo", "Não reportado", "Não se aplica"],
    "cenarios_classificacao": ["3 classes (Mult-Class)", "DD×HC", "Outro", "PD×DD", "PD×HC"],
    "representacao_entrada": ["Atributos manuais (handcrafted)", "Outro", "Série bruta",
                              "Tempo-frequência (espectrograma, wavelet)"],
    "familia_algoritmo": ["Auto-supervisionado", "Classical ML", "Deep Learning", "Generativo-augmentation",
                          "Hybrid-Ensemble", "Outro"],
    "balanceamento_augmentation": ["Dados sintéticos (GAN)", "Nenhum", "Não reportado", "Não se aplica", "Outro",
                                   "SMOTE-oversampling"],
    "estrategia_validacao": ["CV aninhada", "Hold-out", "Leave-one-subject-out", "Não reportado", "Outra",
                             "k-fold CV"],
    "unidade_particionamento": ["Gravação-sessão", "Janela/segmento", "Misto", "Não reportado", "Não se aplica",
                                "Participante"],
    "separacao_participante": ["Não", "Não se aplica", "Parcial", "Pouco claro", "Sim – explícita",
                               "Sim – inferida"],
    "momento_balanceamento": ["Antes do split", "Não reportado", "Não se aplica", "Só no treino"],
    "metricas": ["AUC", "Accuracy", "Balanced accuracy", "F1", "MCC", "Outra", "Precision", "Sensitivity",
                 "Specificity"],
    "codigo_dados": ["Ambos", "Código", "Dados", "Nenhum", "Não reportado"],
}

# campo Select -> (rótulos que exigem texto, campo de texto)
OUTRO = {
    "tipo_contribuicao": ({"Outro"}, "outra_contribuicao"),
    "datasets": ({"Outro público", "Privado-próprio"}, "outros_datasets"),
    "sensores": ({"Outro"}, "outros_sensores"),
    "cenarios_classificacao": ({"Outro"}, "outro_cenario"),
    "representacao_entrada": ({"Outro"}, "outra_representacao"),
    "familia_algoritmo": ({"Outro"}, "outra_familia"),
    "estrategia_validacao": ({"Outra"}, "outra_estrategia_validacao"),
    "metricas": ({"Outra"}, "outras_metricas"),
}


def lista(valor):
    """Normaliza o valor para lista (None vira lista vazia)."""
    if valor is None:
        return []
    return valor if isinstance(valor, list) else [valor]


def texto(valor, tipo):
    """Converte o valor YAML para a célula da planilha."""
    if valor is None:
        return None
    if tipo == "many":
        return SEP.join(map(str, lista(valor)))
    if tipo == "bool":
        return "Sim" if valor else "Não"
    return valor


def ler(pasta, alertas):
    """Lê os YAML de uma pasta; erros de sintaxe viram alertas."""
    dados = {}
    for arq in sorted(pasta.glob("*.yaml")):
        try:
            doc = yaml.safe_load(arq.read_text(encoding="utf-8"))
            dados[int(doc["meta"]["row_id"])] = doc
        except (yaml.YAMLError, KeyError, TypeError, ValueError) as erro:
            alertas.append({"row_id": arq.stem, "chave": None, "problema": f"arquivo inválido: {erro}"})
    return dados


def validar(rid, campos):
    """Confere campos ausentes, rótulos fora do Parsifal, Outro/texto e soma por classe."""
    achados = []
    por_chave = {c.get("chave"): c.get("valor") for c in campos}

    def alerta(chave, problema):
        achados.append({"row_id": rid, "chave": chave, "problema": problema})

    for _, chave, _, tipo in CAMPOS:
        if chave not in por_chave:
            alerta(chave, "campo ausente no YAML")
            continue
        valor = por_chave[chave]
        if tipo in ("one", "many") and valor is not None:
            if tipo == "one" and isinstance(valor, list):
                alerta(chave, "Select One recebeu lista")
            for item in lista(valor):
                if item not in OPCOES[chave]:
                    alerta(chave, f"rótulo fora do Parsifal: {item!r}")
        if tipo == "bool" and valor is not None and not isinstance(valor, bool):
            alerta(chave, "Boolean deve ser true/false")
    for chave, (gatilhos, campo_texto) in OUTRO.items():
        marcou = bool(set(lista(por_chave.get(chave))) & gatilhos)
        preencheu = por_chave.get(campo_texto) not in (None, "")
        if marcou and not preencheu:
            alerta(campo_texto, "opção Outro/Outra marcada sem texto")
        if preencheu and not marcou:
            alerta(campo_texto, "texto preenchido sem marcar Outro/Outra")
    if "Não reportado" in lista(por_chave.get("estrategia_validacao")) and len(lista(por_chave["estrategia_validacao"])) > 1:
        alerta("estrategia_validacao", "Não reportado é exclusivo")
    n, classes = por_chave.get("n_participantes"), re.findall(r"=\s*(\d+)", str(por_chave.get("n_por_classe") or ""))
    if n is not None and classes and sum(map(int, classes)) != n:
        alerta("n_por_classe", f"soma por classe ({sum(map(int, classes))}) difere de n_participantes ({n})")
    return achados


def resumo_qa(qa):
    """Recalcula nota, máximo, proporção e faixa (nota null = N/A, fora do cálculo)."""
    notas = {k: v.get("nota") for k, v in (qa or {}).items()}
    aplicaveis = [n for n in notas.values() if n is not None]
    soma, maximo = sum(aplicaveis), len(aplicaveis)
    pct = soma / maximo if maximo else None
    faixa = None if pct is None else "Alta" if pct >= 0.8 else "Média" if pct >= 0.5 else "Baixa"
    return notas, soma, maximo, pct, faixa


def consolidar(ia, alertas):
    linhas, evidencias, qa_linhas, revisao = [], [], [], []
    for rid, doc in sorted(ia.items()):
        campos, deriv, meta = doc.get("campos") or [], doc.get("derivados") or {}, doc.get("meta") or {}
        if str(meta.get("elegibilidade", "")).startswith("NÃO"):
            alertas.append({"row_id": rid, "chave": None, "problema": f"elegibilidade '{meta.get('elegibilidade')}': revisar o artigo no Zotero/Parsifal"})
            continue
        alertas += validar(rid, campos)
        por_chave = {c.get("chave"): c for c in campos}
        linha = {nome: texto(por_chave.get(chave, {}).get("valor"), tipo) for _, chave, nome, tipo in CAMPOS}
        notas, soma, maximo, pct, faixa = resumo_qa(deriv.get("qa"))
        aux = deriv.get("aux_preproc_apenas_treino", {})
        linha.update({
            "aux_preproc_apenas_treino": aux.get("valor"),
            "aux_observacoes_ia": " | ".join(f"{c['id']}: {c['observacao']}" for c in campos if c.get("observacao")),
            "risco_vazamento": deriv.get("risco_vazamento", {}).get("valor"),
            **{k: v for k, v in notas.items()},
            "nota_qa": soma, "nota_qa_max": maximo, "nota_qa_pct": pct, "faixa_qa": faixa,
            "aux_elegibilidade": meta.get("elegibilidade"), "aux_qualidade_texto": meta.get("qualidade_do_texto"),
            "aux_status_triagem": meta.get("status_triagem"), "aux_ressalva_triagem": meta.get("ressalva_triagem"),
            "aux_zotero_key": meta.get("zotero_key"), "aux_titulo": meta.get("titulo"),
        })
        if deriv.get("nota_qa") is not None and deriv["nota_qa"] != soma:
            alertas.append({"row_id": rid, "chave": "nota_qa", "problema": f"IA informou {deriv['nota_qa']}, soma real {soma}"})
        linhas.append(linha)
        for c in campos:
            evidencias.append({"row_id": rid, **{k: (texto(c.get(k), "many") if k == "valor" else c.get(k))
                                                for k in ("id", "chave", "valor", "status", "confianca", "evidencia", "auditoria", "observacao")}})
        for k, v in (deriv.get("qa") or {}).items():
            qa_linhas.append({"row_id": rid, "questao": k, "resposta": v.get("resposta"), "nota": v.get("nota"),
                              "campos": ", ".join(map(str, lista(v.get("campos")))), "justificativa": v.get("justificativa")})
        revisao += [{"row_id": rid, "ponto": p, "resolvido": None} for p in lista(doc.get("pontos_para_revisao_humana"))]
    return (pd.DataFrame(linhas), pd.DataFrame(evidencias), pd.DataFrame(qa_linhas), pd.DataFrame(revisao))


def divergencias(ia, auditoria):
    """Campos em que a auditoria DISCORDA ou NÃO VERIFICÁVEL, com o valor extraído e o auditado."""
    tipos = {chave: tipo for _, chave, _, tipo in CAMPOS}
    colunas = ["row_id", "id", "chave", "auditoria", "valor_extraido", "valor_auditado", "evidencia", "observacao", "resolvido"]
    linhas = []
    for rid, doc in sorted(auditoria.items()):
        extraido = {c.get("chave"): c.get("valor") for c in (ia.get(rid, {}).get("campos") or [])}
        for c in doc.get("campos") or []:
            if c.get("auditoria") in ("DISCORDA", "NÃO VERIFICÁVEL"):
                chave = c.get("chave")
                linhas.append({"row_id": rid, "id": c.get("id"), "chave": chave, "auditoria": c["auditoria"],
                               "valor_extraido": texto(extraido.get(chave), tipos.get(chave)),
                               "valor_auditado": texto(c.get("valor"), tipos.get(chave)),
                               "evidencia": c.get("evidencia"), "observacao": c.get("observacao"), "resolvido": None})
    return pd.DataFrame(linhas, columns=colunas)


def main():
    alertas = []
    ia = ler(RAW, alertas)
    extracao, evidencias, qa, revisao = consolidar(ia, alertas)
    dicionario = pd.DataFrame(CAMPOS, columns=["id", "chave", "campo_parsifal", "tipo"])
    dicionario["opcoes"] = dicionario["chave"].map(lambda k: SEP.join(OPCOES.get(k, [])))
    abas = {"extracao": extracao, "evidencias": evidencias, "qa": qa, "revisao": revisao}
    if AUDITORIA.exists():
        abas["auditoria"] = divergencias(ia, ler(AUDITORIA, alertas))
    abas.update({"alertas": pd.DataFrame(alertas, columns=["row_id", "chave", "problema"]), "dicionario": dicionario})
    with pd.ExcelWriter(SAIDA, engine="openpyxl") as xw:
        for nome, df in abas.items():
            df.to_excel(xw, sheet_name=nome, index=False)
            ws = xw.sheets[nome]
            ws.freeze_panes = "B2"
            ws.auto_filter.ref = ws.dimensions
    print(f"{len(ia)} artigos consolidados em {SAIDA}; {len(alertas)} alertas (ver aba 'alertas').")


if __name__ == "__main__":
    main()
