#!/usr/bin/env python3
"""Gera numeros.tex, tabelas/*.tex e figuras/*.pdf a partir de dados/extracao.xlsx e dados/metadados_estudos.csv."""
from collections import Counter
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
XLSX = ROOT / "dados" / "extracao.xlsx"
META_CSV = ROOT / "dados" / "metadados_estudos.csv"
TAB_DIR = ROOT / "tabelas"
FIG_DIR = ROOT / "figuras"

CITEKEY_BY_ROW = {
    2: "djemaa_quantifying_2026",
    13: "mohtavipour_deep_2026",
    21: "sridhar_early_2026",
    23: "zannat_label-efficient_2026",
    32: "huang_self-supervised_2025",
    40: "zhang_generative_2025",
    44: "gao_coverage-aware_2026",
    47: "abioye_improving_2025",
    49: "abola_differentiating_2025",
    51: "xu_adaptive_2024",
    54: "ren_baseline_2026",
    70: "varghese_machine_2024",
    76: "xing_asa-dsnet_2025",
    77: "pathirathna_neurolens_2026",
    79: "zeebaree_three-class_2027",
    80: "zhao_multi-scale_2025",
    81: "vasisht_energy_2026",
    83: "kalathoti_blockchain-enabled_2026",
    85: "suk-ieam_smartwatch-based_2025",
    87: "wang_parkinsons_2025",
    89: "ouabd_parkinsons_2026",
    90: "vu_simple_2026",
    92: "yu_improved_2024",
    99: "win_checkpd_2026",
    101: "wei_sgc-rml_2026",
    104: "haque_eco-xpd_2026",
    105: "padilha_identificacao_2025",
    108: "padilha_parkinsons_2024",
    109: "lobo_parkinsons_2025",
}


def tex_esc(text: object) -> str:
    """Escapa texto arbitrario para LaTeX seguro em modo UTF-8."""
    if text is None or (isinstance(text, float) and np.isnan(text)):
        return "--"
    s = str(text)
    repl = [
        ("\\", r"\textbackslash{}"),
        ("&", r"\&"),
        ("%", r"\%"),
        ("$", r"\$"),
        ("#", r"\#"),
        ("_", r"\_"),
        ("{", r"\{"),
        ("}", r"\}"),
        ("~", r"\textasciitilde{}"),
        ("^", r"\textasciicircum{}"),
        ("×", r"$\times$"),
        ("±", r"$\pm$"),
        ("≥", r"$\ge$"),
        ("≤", r"$\le$"),
        ("−", "-"),
        ("–", "--"),
        ("—", "---"),
        ("’", "'"),
        ("‘", "'"),
        ("“", "``"),
        ("”", "''"),
        ("²", r"$^2$"),
        ("χ", r"$\chi$"),
        ("η", r"$\eta$"),
        ("α", r"$\alpha$"),
        ("β", r"$\beta$"),
        ("θ", r"$\theta$"),
    ]
    for a, b in repl:
        s = s.replace(a, b)
    return s


def fmt_pct(num: float, den: int, decimals: int = 1) -> str:
    if den == 0:
        return "0,0\\%"
    return f"{100.0 * num / den:.{decimals}f}".replace(".", ",") + r"\%"


def fmt_num(val: float, decimals: int = 1) -> str:
    return f"{val:.{decimals}f}".replace(".", ",")


def split_many(series: pd.Series) -> Counter:
    c: Counter = Counter()
    for val in series.dropna():
        for item in str(val).split("; "):
            item = item.strip()
            if item:
                c[item] += 1
    return c


def compact_veiculo(row: pd.Series) -> str:
    tipo = row["tipo_publicacao"]
    v = str(row["veiculo"])
    r = str(row["repositorio"]) if pd.notna(row["repositorio"]) else ""
    if tipo == "preprint":
        return f"Prep. ({r})"
    mapa = {
        "2026 International Conference on Next-Gen Intelligent Computing and Applications (ICONICA)": "ICONICA (Anais)",
        "2025 IEEE 23rd International Conference on Industrial Informatics (INDIN)": "INDIN (Anais)",
        "2024 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)": "BIBM (Anais)",
        "2025 IEEE International Conference on Bioinformatics and Biomedicine (BIBM)": "BIBM (Anais)",
        "2026 IEEE International Conference on Automatic Control and Intelligent Systems (I2CACIS)": "I2CACIS (Anais)",
        "2026 11th International Conference on Machine Learning Technologies (ICMLT)": "ICMLT (Anais)",
        "2025 18th International Convention on Rehabilitation Engineering and Assistive Technology (i-CREATe)": "i-CREATe (Anais)",
        "2026 6th International Conference on Innovative Research in Applied Science, Engineering and Technology (IRASET)": "IRASET (Anais)",
        "Escola Regional de Informática de Goiás (ERI-GO)": "ERI-GO (Anais)",
        "Biomedical Signal Processing and Control": "Biomed. Signal P. C.",
        "VFAST Transactions on Software Engineering": "VFAST Trans. SE",
        "Frontiers in Artificial Intelligence": "Front. Artif. Intell.",
        "IT Journal Research and Development": "IT J. Res. Dev.",
        "IEEE Internet of Things Journal": "IEEE IoT J.",
        "Egyptian Informatics Journal": "Egypt. Inform. J.",
        "Brain Science Advances": "Brain Sci. Adv.",
        "Cognitive Computation": "Cogn. Comput.",
        "Information Fusion": "Inf. Fusion",
        "npj Parkinson's Disease": "npj Parkinsons Dis.",
    }
    return mapa.get(v, v)


def compact_cenarios(val: object) -> str:
    if pd.isna(val):
        return "--"
    parts = [p.strip() for p in str(val).split("; ")]
    rep = {
        "3 classes (Mult-Class)": "3-cl",
        "PD×HC": r"PD$\times$HC",
        "PD×DD": r"PD$\times$DD",
        "DD×HC": r"DD$\times$HC",
        "Outro": "Outro",
    }
    return ", ".join(rep.get(p, tex_esc(p)) for p in parts)


def compact_contrib(val: object) -> str:
    mapa = {
        "Novo modelo": "Novo mod.",
        "Estudo comparativo": "Comparat.",
        "Análise estatística": "Estatíst.",
        "Plataforma-sistema": "Plataf.",
        "Outro": "Base/ML",
    }
    return mapa.get(str(val), tex_esc(val))


def compact_papel(val: object) -> str:
    mapa = {
        "Principal": "Princ.",
        "Análise suplementar": "Supl.",
        "Validação externa-generalização": "Val. ext.*",
    }
    return mapa.get(str(val), tex_esc(val))


def compact_risco(val: object) -> str:
    mapa = {
        "Baixo": "Baixo",
        "Moderado": "Mod.",
        "Alto": "Alto",
        "Indeterminado": "Indet.",
        "Não se aplica": "N/A",
    }
    return mapa.get(str(val), tex_esc(val))


def parse_best_result(row: pd.Series) -> tuple[str, str, str, str]:
    s = str(row["Melhor resultado (Evaluation Values)"])
    parts = [p.strip() for p in s.split("; ")]
    if len(parts) >= 4:
        cen, mod, met, val = parts[0], parts[1], parts[2], "; ".join(parts[3:])
    else:
        cen, mod, met, val = "--", s, "--", "--"
    cen = (cen.replace("3 classes (Mult-Class)", "3 classes")
              .replace("PD×HC (tarefa Relaxed / Rest Tremor)", "PD×HC (Relaxed/Rest)")
              .replace("PD×DD (tarefa StretchHold)", "PD×DD (StretchHold)")
              .replace("PD vs. non-PD (binário)", "PD vs. non-PD")
              .replace("PD×HC", r"PD$\times$HC")
              .replace("PD×DD", r"PD$\times$DD")
              .replace("DD×HC", r"DD$\times$HC")
              .replace("Associação sintomas não motores vs. amplitude de movimento (PADS)", "Correl. NMS-IMU")
              .replace("Diferenciação diagnóstica (6 grupos)", "6 grupos"))
    # Abreviar nomes longos de modelo mantendo fidelidade ao artigo
    mod_map = {
        "Multi-stream deep representation learning network": "Multi-stream CNN-Transf.",
        "Proposed CNN–BiLSTM + Attention": "CNN-BiLSTM + Attention",
        "BOSS + SVM (Hybrid Data com Conditional TremorGANs)": "BOSS+SVM (TremorGANs)",
        "Calibrated Stacking Ensemble (CatBoostClassifier + RandomForestClassifier + LogisticRegression)": "Stacking (CatBoost+RF+LR)",
        "Multinomial Logistic Regression": "Reg. Logística Multinom.",
        "Correlação de Spearman": "Correl. de Spearman",
        "Classifier Stacking (Smartwatch + Questionnaire, complete)": "Stacking (IMU+PDNMS)",
        "1D CNN (8-bit, session-level)": "1D CNN (8-bit)",
        "Soft-voting XGBoost–LightGBM ensemble (150 handcrafted features, patient-level 5-fold CV)": "Soft-voting XGB-LGBM",
        "Blockchain-Integrated CNN–Transformer": "CNN-Transformer",
        "V7 Ensemble (PatchTST + Quality)": "PatchTST + Quality",
        "Proposed (With xReDA)": "Eco-xPD (c/ xReDA)",
        "BTE + SMOTE + Random Forest": "BTE+SMOTE+RF",
    }
    mod = mod_map.get(mod, mod)
    met = (met.replace("Balanced accuracy", "Bal. Acc.")
              .replace("Accuracy / F1-score / AUC", "Acc/F1/AUC")
              .replace("Spearman r (FDR-adjusted p)", "Spearman r")
              .replace("Acurácia", "Accuracy"))
    val = re.sub(r"\s*\([^)]{20,}\)", "", val).strip()
    if " / " in val and len(val) > 22:
        val = val.split(" / ")[0].strip()
    if "para carga de sintomas" in val:
        val = "r = -0.171 (p=0.0071)"
    val = val.replace("0.972868 (97.29%, 95% CI ± 0.00701)", "97.29%").replace(" [.708,.942]", "")
    val = val.replace("0.068 (LR χ²(75) = 1740.33, p < 0.001)", "0.068 (LR χ²=1740, p<0.001)")
    return (cen if "$" in cen else tex_esc(cen)), tex_esc(mod), tex_esc(met), tex_esc(val)


def compact_val_label(val: object) -> str:
    if pd.isna(val):
        return "--"
    parts = [p.strip() for p in str(val).split("; ")]
    mapa = {
        "k-fold CV": "k-fold",
        "Hold-out": "HO",
        "CV aninhada": "Anin.",
        "Leave-one-subject-out": "LOSO",
        "Não reportado": "Não rep.",
        "Outra": "LOTO",
    }
    return "+".join(mapa.get(p, tex_esc(p)) for p in parts)


def compute_gap_themes(df: pd.DataFrame) -> list[tuple[str, list[int]]]:
    themes = [
        ("Ausência de validação externa / coortes multicêntricas", []),
        ("Dificuldade no diagnóstico diferencial (PD$\\times$DD)", []),
        ("Falta de severidade (UPDRS/H\\&Y) e vida livre", []),
        ("Falta de multimodalidade, XAI, calibração e justiça", []),
        ("Indisponibilidade de código/dados (reprodutibilidade)", []),
    ]
    p_ext = re.compile(r"valida[çc][ãa]o\s+(cl[íi]nica\s+)?externa|multic[êe]ntric|[úu]nico dataset|unico dataset|coortes? independentes?|datasets? independentes?|segundo dataset|centro [úu]nico|single site|entre( diferentes)? datasets|entre centros|domain shift|datasets maiores")
    p_dd = re.compile(r"diagn[óo]stico diferencial|\bpd\s+vs\.?\s*dd\b|\bdp\s+vs\.?\s*dd\b|\(dd\)|\bdd\b|tremor essencial|outros dist[úu]rbios")
    p_long = re.compile(r"updrs|hoehn|severidade|estadiamento|est[áa]gio|vida livre|free-living|longitudinal|prodr[ôo]m|medicament|on/off|transversal|monitoramento cont[íi]nuo")
    p_mult = re.compile(r"multimodal|outras modalidades|novas modalidades|\bxai\b|interpretabil|explicabil|\bshap\b|grad-cam|integrated gradients|calibra|fairness|justi[çc]a|confund|confus[ãa]o|demogr[áa]fic|leakage|vazamento|federado|on-device")
    for _, r in df.sort_values("ID do Registro (row_id)").iterrows():
        rid = int(r["ID do Registro (row_id)"])
        txt = f"{r['Limitações Reportadas'] or ''} {r['Lacuna identificada pelos autores'] or ''}".lower()
        if p_ext.search(txt):
            themes[0][1].append(rid)
        if p_dd.search(txt):
            themes[1][1].append(rid)
        if p_long.search(txt):
            themes[2][1].append(rid)
        if p_mult.search(txt):
            themes[3][1].append(rid)
        if str(r["Código/dados disponíveis"]) in ("Nenhum", "Não reportado"):
            themes[4][1].append(rid)
    return themes


def write_macros(df: pd.DataFrame, df_ev: pd.DataFrame, df_rev_pts: pd.DataFrame, themes: list[tuple[str, list[int]]]) -> None:
    n_tot = len(df)
    n_pre = int(df["is_preprint"].sum())
    n_rev = n_tot - n_pre
    n_vaz_app = int((df["risco_vazamento"] != "Não se aplica").sum())
    n_rev_vaz_app = int(((~df["is_preprint"]) & (df["risco_vazamento"] != "Não se aplica")).sum())

    ano_c = df["Ano de Publicação"].astype(str).value_counts().to_dict()
    contrib_c = df["Tipo de Contribuição"].value_counts().to_dict()
    papel_c = df["Papel do PADS"].value_counts().to_dict()
    tipo_pub_c = df["tipo_publicacao"].value_counts().to_dict()
    repo_c = df["repositorio"].fillna("").value_counts().to_dict()

    ds_c = split_many(df["Datasets"])
    mod_c = split_many(df["Modalidade do PADS"])
    tar_c = df["Tarefas do PADS"].value_counts().to_dict()
    sens_c = split_many(df["Sensores"])
    punho_c = df["Punho(s) usado(s)"].value_counts().to_dict()
    cen_c = split_many(df["Cenários de classificação"])
    rep_c = split_many(df["Representação de entrada"])
    fam_c = split_many(df["Família do Algoritmo"])
    bal_c = df["Balanceamento/augmentation"].value_counts().to_dict()
    val_c = split_many(df["Estratégia de Validação"])
    unid_c = df["Unidade de particionamento (partitioning unit)"].value_counts().to_dict()
    sep_c = df["Separação por participante (subject-level separation)"].value_counts().to_dict()
    mom_c = df["Balanceamento"].value_counts().to_dict()
    pre_c = df["aux_preproc_apenas_treino"].fillna("NA").value_counts().to_dict()
    vext_c = df["Validação externa do Modelo"].value_counts().to_dict()
    met_c = split_many(df["Métricas de avaliação"])
    risco_c = df["risco_vazamento"].value_counts().to_dict()
    faixa_c = df["faixa_qa"].value_counts().to_dict()
    cod_c = df["Código/dados disponíveis"].value_counts().to_dict()
    tri_c = df["aux_status_triagem"].value_counts().to_dict()

    rev_df = df[~df["is_preprint"]]
    pre_df = df[df["is_preprint"]]
    rev_ano = rev_df["Ano de Publicação"].astype(str).value_counts().to_dict()
    rev_risco = rev_df["risco_vazamento"].value_counts().to_dict()
    pre_risco = pre_df["risco_vazamento"].value_counts().to_dict()
    rev_faixa = rev_df["faixa_qa"].value_counts().to_dict()
    pre_faixa = pre_df["faixa_qa"].value_counts().to_dict()
    rev_cen = split_many(rev_df["Cenários de classificação"])
    pre_cen = split_many(pre_df["Cenários de classificação"])
    rev_fam = split_many(rev_df["Família do Algoritmo"])
    pre_fam = split_many(pre_df["Família do Algoritmo"])

    n_multi_ds = int(df["Datasets"].astype(str).str.contains(";").sum())
    n_multi_sobrep = int((df["Datasets"].astype(str).str.contains("Outro público") & df["Datasets"].astype(str).str.contains("Privado-próprio")).sum())
    n_only_pdnms = int((df["Modalidade do PADS"] == "Questionário (PDNMS)").sum())
    n_part_rep = int(df["N° de participantes"].notna().sum())
    n_part_min = int(df["N° de participantes"].min())
    n_part_max = int(df["N° de participantes"].max())
    n_part_med = int(df["N° de participantes"].median())
    n_classe_rep = int(df["N° por classe: PD / HC / DD"].notna().sum())
    n_sep_sim = sep_c.get("Sim – explícita", 0) + sep_c.get("Sim – inferida", 0)
    n_cod_disp = cod_c.get("Código", 0) + cod_c.get("Ambos", 0) + cod_c.get("Dados", 0)
    n_rev_cod_disp = int(rev_df["Código/dados disponíveis"].isin(["Código", "Ambos", "Dados"]).sum())
    n_pre_cod_disp = int(pre_df["Código/dados disponíveis"].isin(["Código", "Ambos", "Dados"]).sum())
    n_sem_lim = int((df["Limitações Reportadas"].fillna("Não reportado") == "Não reportado").sum())
    n_sem_lac = int((df["Lacuna identificada pelos autores"].fillna("Não reportado") == "Não reportado").sum())

    macros = {
        "nTotal": n_tot,
        "nRevisadosPares": n_rev,
        "pctRevisadosPares": fmt_pct(n_rev, n_tot),
        "nPreprints": n_pre,
        "pctPreprints": fmt_pct(n_pre, n_tot),
        "nAplicaveisVaz": n_vaz_app,
        "nNaoAplicaveisVaz": n_tot - n_vaz_app,
        "nImportados": 115,
        "nDuplicados": 24,
        "nTriados": 91,
        "nRejeitados": 62,
        "nRejCEUm": 31,
        "nRejCEDois": 10,
        "nRejCETres": 21,
        "nRejMetadados": 4,
        "nRejTexto": 58,
        "nAceitos": 29,
        "nScholarDireto": 69,
        "nScholarBalde": 84,
        "nNatureExcl": 14,
        "nNatureTotal": 77,
        "nSnowballing": 15,
        "nSementesSnowballing": 11,
        "nStringsTotal": 17,
        "nStringsIEEE": 7,
        "nStringsPMC": 1,
        "nStringsSD": 3,
        "nStringsScopus": 6,
        "nComumScholarNature": 63,
        "nSoScholar": 6,
        "nUniaoScholarNature": 83,
        "nCamposTotalAud": len(df_ev),
        "nPontosRevisao": len(df_rev_pts),
        "nTriagemAceito": tri_c.get("Aceito", 0),
        "nTriagemRessalvas": tri_c.get("Aceito, mas com Ressalvas", 0),
        "nTriagemNaoConfiavel": tri_c.get("Aceito, mas com Ressalvas, não confiável", 0),
        "nTriagemIncerto": tri_c.get("Incerto - texto completo", 0),
        "nAnoDoisQuatro": ano_c.get("2024", 0),
        "nAnoDoisCinco": ano_c.get("2025", 0),
        "nAnoDoisSeis": ano_c.get("2026", 0),
        "pctAnoDoisQuatro": fmt_pct(ano_c.get("2024", 0), n_tot),
        "pctAnoDoisCinco": fmt_pct(ano_c.get("2025", 0), n_tot),
        "pctAnoDoisSeis": fmt_pct(ano_c.get("2026", 0), n_tot),
        "nPeriodicos": tipo_pub_c.get("periódico", 0),
        "pctPeriodicos": fmt_pct(tipo_pub_c.get("periódico", 0), n_tot),
        "nAnais": tipo_pub_c.get("anais de conferência", 0),
        "pctAnais": fmt_pct(tipo_pub_c.get("anais de conferência", 0), n_tot),
        "nPreArxiv": repo_c.get("arXiv", 0),
        "nPreMedrxiv": repo_c.get("medRxiv", 0),
        "nPreRS": repo_c.get("Research Square", 0),
        "nPreJMIR": repo_c.get("JMIR Preprints", 0),
        "nContribNovoModelo": contrib_c.get("Novo modelo", 0),
        "pctContribNovoModelo": fmt_pct(contrib_c.get("Novo modelo", 0), n_tot),
        "nContribComparativo": contrib_c.get("Estudo comparativo", 0),
        "pctContribComparativo": fmt_pct(contrib_c.get("Estudo comparativo", 0), n_tot),
        "nContribEstatistica": contrib_c.get("Análise estatística", 0),
        "nContribPlataforma": contrib_c.get("Plataforma-sistema", 0),
        "nContribOutro": contrib_c.get("Outro", 0),
        "nPapelPrincipal": papel_c.get("Principal", 0),
        "pctPapelPrincipal": fmt_pct(papel_c.get("Principal", 0), n_tot),
        "nPapelSuplementar": papel_c.get("Análise suplementar", 0),
        "nPapelExtGen": papel_c.get("Validação externa-generalização", 0),
        "nMultiBase": n_multi_ds,
        "pctMultiBase": fmt_pct(n_multi_ds, n_tot),
        "nOutroPublico": ds_c.get("Outro público", 0),
        "nPrivadoProprio": ds_c.get("Privado-próprio", 0),
        "nMultiBaseSobrep": n_multi_sobrep,
        "nModIMU": mod_c.get("Série temporal (IMU)", 0),
        "pctModIMU": fmt_pct(mod_c.get("Série temporal (IMU)", 0), n_tot),
        "nModPDNMS": mod_c.get("Questionário (PDNMS)", 0),
        "pctModPDNMS": fmt_pct(mod_c.get("Questionário (PDNMS)", 0), n_tot),
        "nModMetadados": mod_c.get("Metadados demográficos-clínicos", 0),
        "pctModMetadados": fmt_pct(mod_c.get("Metadados demográficos-clínicos", 0), n_tot),
        "nModSoPDNMS": n_only_pdnms,
        "nTarTodas": tar_c.get("Todas", 0),
        "pctTarTodas": fmt_pct(tar_c.get("Todas", 0), n_tot),
        "nTarSubconj": tar_c.get("Subconjunto", 0),
        "nTarNaoRep": tar_c.get("Não reportado", 0),
        "nTarNA": tar_c.get("Não se aplica", 0),
        "nSensGiro": sens_c.get("Giroscópio", 0),
        "nSensAcel": sens_c.get("Acelerômetro", 0),
        "nSensOutro": sens_c.get("Outro", 0),
        "nSensVazio": int(df["Sensores"].isna().sum()),
        "nPunhoAmbos": punho_c.get("Ambos", 0),
        "pctPunhoAmbos": fmt_pct(punho_c.get("Ambos", 0), n_tot),
        "nPunhoNaoRep": punho_c.get("Não reportado", 0),
        "nPunhoDir": punho_c.get("Direito", 0),
        "nPunhoEsq": punho_c.get("Esquerdo", 0),
        "nPunhoNA": punho_c.get("Não se aplica", 0),
        "nPartRep": n_part_rep,
        "pctPartRep": fmt_pct(n_part_rep, n_tot),
        "nPartMin": n_part_min,
        "nPartMax": n_part_max,
        "nPartMediana": n_part_med,
        "nClasseRep": n_classe_rep,
        "nCenPDHC": cen_c.get("PD×HC", 0),
        "pctCenPDHC": fmt_pct(cen_c.get("PD×HC", 0), n_tot),
        "nCenPDDD": cen_c.get("PD×DD", 0),
        "pctCenPDDD": fmt_pct(cen_c.get("PD×DD", 0), n_tot),
        "nCenTresClasses": cen_c.get("3 classes (Mult-Class)", 0),
        "pctCenTresClasses": fmt_pct(cen_c.get("3 classes (Mult-Class)", 0), n_tot),
        "nCenDDHC": cen_c.get("DD×HC", 0),
        "nCenOutro": cen_c.get("Outro", 0),
        "nCenNA": int(df["Cenários de classificação"].isna().sum()),
        "nRepBruta": rep_c.get("Série bruta", 0),
        "pctRepBruta": fmt_pct(rep_c.get("Série bruta", 0), n_tot),
        "nRepHandcrafted": rep_c.get("Atributos manuais (handcrafted)", 0),
        "pctRepHandcrafted": fmt_pct(rep_c.get("Atributos manuais (handcrafted)", 0), n_tot),
        "nRepTF": rep_c.get("Tempo-frequência (espectrograma, wavelet)", 0),
        "nRepOutro": rep_c.get("Outro", 0),
        "nRepNA": int(df["Representação de entrada"].isna().sum()),
        "nFamDL": fam_c.get("Deep Learning", 0),
        "pctFamDL": fmt_pct(fam_c.get("Deep Learning", 0), n_tot),
        "nFamML": fam_c.get("Classical ML", 0),
        "pctFamML": fmt_pct(fam_c.get("Classical ML", 0), n_tot),
        "nFamHybrid": fam_c.get("Hybrid-Ensemble", 0),
        "nFamGen": fam_c.get("Generativo-augmentation", 0),
        "nFamSSL": fam_c.get("Auto-supervisionado", 0),
        "nFamOutro": fam_c.get("Outro", 0),
        "nBalNenhum": bal_c.get("Nenhum", 0),
        "nBalOutro": bal_c.get("Outro", 0),
        "nBalSMOTE": bal_c.get("SMOTE-oversampling", 0),
        "nBalGAN": bal_c.get("Dados sintéticos (GAN)", 0),
        "nBalNA": bal_c.get("Não se aplica", 0),
        "nBalNaoRep": bal_c.get("Não reportado", 0),
        "nValKfold": val_c.get("k-fold CV", 0),
        "pctValKfold": fmt_pct(val_c.get("k-fold CV", 0), n_tot),
        "nValHoldout": val_c.get("Hold-out", 0),
        "nValAninhada": val_c.get("CV aninhada", 0),
        "nValLOSO": val_c.get("Leave-one-subject-out", 0),
        "nValNaoRep": val_c.get("Não reportado", 0),
        "nValOutra": val_c.get("Outra", 0),
        "nUnidPart": unid_c.get("Participante", 0),
        "pctUnidPart": fmt_pct(unid_c.get("Participante", 0), n_vaz_app),
        "nUnidNaoRep": unid_c.get("Não reportado", 0),
        "nUnidNA": unid_c.get("Não se aplica", 0),
        "nSepExpl": sep_c.get("Sim – explícita", 0),
        "nSepInf": sep_c.get("Sim – inferida", 0),
        "nSepTotalSim": n_sep_sim,
        "pctSepTotalSim": fmt_pct(n_sep_sim, n_vaz_app),
        "nSepPoucoClaro": sep_c.get("Pouco claro", 0),
        "nSepNA": sep_c.get("Não se aplica", 0),
        "nMomTreino": mom_c.get("Só no treino", 0),
        "nMomAntes": mom_c.get("Antes do split", 0),
        "nMomNaoRep": mom_c.get("Não reportado", 0),
        "nMomNA": mom_c.get("Não se aplica", 0),
        "nPreprocSim": pre_c.get("Sim", 0),
        "nPreprocNao": pre_c.get("Não", 0),
        "nPreprocNaoRep": pre_c.get("Não reportado", 0),
        "nPreprocNA": pre_c.get("NA", 0),
        "nValExtNao": vext_c.get("Não", 0),
        "nValExtSim": vext_c.get("Sim", 0),
        "nMetFOne": met_c.get("F1", 0),
        "pctMetFOne": fmt_pct(met_c.get("F1", 0), n_tot),
        "nMetAcc": met_c.get("Accuracy", 0),
        "pctMetAcc": fmt_pct(met_c.get("Accuracy", 0), n_tot),
        "nMetSens": met_c.get("Sensitivity", 0),
        "nMetPrec": met_c.get("Precision", 0),
        "nMetAUC": met_c.get("AUC", 0),
        "nMetBalAcc": met_c.get("Balanced accuracy", 0),
        "nMetSpec": met_c.get("Specificity", 0),
        "nMetMCC": met_c.get("MCC", 0),
        "nMetOutra": met_c.get("Outra", 0),
        "nRiscoBaixo": risco_c.get("Baixo", 0),
        "pctRiscoBaixoAplic": fmt_pct(risco_c.get("Baixo", 0), n_vaz_app),
        "nRiscoModerado": risco_c.get("Moderado", 0),
        "pctRiscoModeradoAplic": fmt_pct(risco_c.get("Moderado", 0), n_vaz_app),
        "nRiscoAlto": risco_c.get("Alto", 0),
        "pctRiscoAltoAplic": fmt_pct(risco_c.get("Alto", 0), n_vaz_app),
        "nRiscoIndet": risco_c.get("Indeterminado", 0),
        "pctRiscoIndetAplic": fmt_pct(risco_c.get("Indeterminado", 0), n_vaz_app),
        "nRiscoNA": risco_c.get("Não se aplica", 0),
        "qaMediaPct": fmt_num(df["nota_qa_pct"].mean() * 100, 1) + r"\%",
        "qaMedianaPct": fmt_num(df["nota_qa_pct"].median() * 100, 1) + r"\%",
        "qaMinPct": fmt_num(df["nota_qa_pct"].min() * 100, 1) + r"\%",
        "qaMaxPct": fmt_num(df["nota_qa_pct"].max() * 100, 1) + r"\%",
        "nQAAlta": faixa_c.get("Alta", 0),
        "pctQAAlta": fmt_pct(faixa_c.get("Alta", 0), n_tot),
        "nQAMedia": faixa_c.get("Média", 0),
        "pctQAMedia": fmt_pct(faixa_c.get("Média", 0), n_tot),
        "nQABaixa": faixa_c.get("Baixa", 0),
        "pctQABaixa": fmt_pct(faixa_c.get("Baixa", 0), n_tot),
        "nCodNenhum": cod_c.get("Nenhum", 0),
        "pctCodNenhum": fmt_pct(cod_c.get("Nenhum", 0), n_tot),
        "nCodNaoRep": cod_c.get("Não reportado", 0),
        "pctCodNaoRep": fmt_pct(cod_c.get("Não reportado", 0), n_tot),
        "nCodCodigo": cod_c.get("Código", 0),
        "nCodAmbos": cod_c.get("Ambos", 0),
        "nCodDisponivel": n_cod_disp,
        "pctCodDisponivel": fmt_pct(n_cod_disp, n_tot),
        "nQAUmYes": int((df["QA1"] == 1.0).sum()),
        "nQAUmPart": int((df["QA1"] == 0.5).sum()),
        "nQAUmNo": int((df["QA1"] == 0.0).sum()),
        "nQAUmNA": int(df["QA1"].isna().sum()),
        "nQADoisYes": int((df["QA2"] == 1.0).sum()),
        "nQADoisPart": int((df["QA2"] == 0.5).sum()),
        "nQADoisNo": int((df["QA2"] == 0.0).sum()),
        "nQATresYes": int((df["QA3"] == 1.0).sum()),
        "nQATresPart": int((df["QA3"] == 0.5).sum()),
        "nQATresNo": int((df["QA3"] == 0.0).sum()),
        "nQATresNA": int(df["QA3"].isna().sum()),
        "nQAQuatroYes": int((df["QA4"] == 1.0).sum()),
        "nQAQuatroPart": int((df["QA4"] == 0.5).sum()),
        "nQAQuatroNo": int((df["QA4"] == 0.0).sum()),
        "nQAQuatroNA": int(df["QA4"].isna().sum()),
        "nQACincoYes": int((df["QA5"] == 1.0).sum()),
        "nQACincoPart": int((df["QA5"] == 0.5).sum()),
        "nQACincoNo": int((df["QA5"] == 0.0).sum()),
        "nLacunaValExt": len(themes[0][1]),
        "nLacunaPDDD": len(themes[1][1]),
        "nLacunaLongitSev": len(themes[2][1]),
        "nLacunaMultimodalXAI": len(themes[3][1]),
        "nSemLimitacao": n_sem_lim,
        "nSemLacuna": n_sem_lac,
        "nRevAplicaveisVaz": n_rev_vaz_app,
        "nRevAnoDoisQuatro": rev_ano.get("2024", 0),
        "nRevAnoDoisCinco": rev_ano.get("2025", 0),
        "nRevAnoDoisSeis": rev_ano.get("2026", 0),
        "nRevRiscoBaixo": rev_risco.get("Baixo", 0),
        "pctRevRiscoBaixoAplic": fmt_pct(rev_risco.get("Baixo", 0), n_rev_vaz_app),
        "nRevRiscoMod": rev_risco.get("Moderado", 0),
        "nRevRiscoAlto": rev_risco.get("Alto", 0),
        "nRevRiscoIndet": rev_risco.get("Indeterminado", 0),
        "nPreRiscoBaixo": pre_risco.get("Baixo", 0),
        "pctPreRiscoBaixo": fmt_pct(pre_risco.get("Baixo", 0), n_pre),
        "nPreRiscoMod": pre_risco.get("Moderado", 0),
        "nPreRiscoAlto": pre_risco.get("Alto", 0),
        "nRevQAAlta": rev_faixa.get("Alta", 0),
        "pctRevQAAlta": fmt_pct(rev_faixa.get("Alta", 0), n_rev),
        "nRevQAMedia": rev_faixa.get("Média", 0),
        "nRevQABaixa": rev_faixa.get("Baixa", 0),
        "nPreQAAlta": pre_faixa.get("Alta", 0),
        "nPreQAMedia": pre_faixa.get("Média", 0),
        "qaMediaRevPct": fmt_num(rev_df["nota_qa_pct"].mean() * 100, 1) + r"\%",
        "qaMediaPrePct": fmt_num(pre_df["nota_qa_pct"].mean() * 100, 1) + r"\%",
        "nRevPDDD": rev_cen.get("PD×DD", 0),
        "pctRevPDDD": fmt_pct(rev_cen.get("PD×DD", 0), n_rev),
        "nPrePDDD": pre_cen.get("PD×DD", 0),
        "pctPrePDDD": fmt_pct(pre_cen.get("PD×DD", 0), n_pre),
        "nRevDL": rev_fam.get("Deep Learning", 0),
        "pctRevDL": fmt_pct(rev_fam.get("Deep Learning", 0), n_rev),
        "nPreDL": pre_fam.get("Deep Learning", 0),
        "nRevCodDisp": n_rev_cod_disp,
        "pctRevCodDisp": fmt_pct(n_rev_cod_disp, n_rev),
        "nPreCodDisp": n_pre_cod_disp,
        "pctPreCodDisp": fmt_pct(n_pre_cod_disp, n_pre),
    }

    lines = ["% Arquivo gerado automaticamente por scripts/gerar_artefatos.py — NAO EDITAR A MAO"]
    for k, v in macros.items():
        lines.append(f"\\newcommand{{\\{k}}}{{{v}}}")
    (ROOT / "numeros.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_tables(df: pd.DataFrame, themes: list[tuple[str, list[int]]]) -> None:
    TAB_DIR.mkdir(parents=True, exist_ok=True)
    n_tot = len(df)
    n_vaz_app = int((df["risco_vazamento"] != "Não se aplica").sum())

    # Tabela 1: 29 estudos condensada (largura ~0.98\textwidth, quase alinhada ao texto)
    t1_rows = []
    for _, r in df.sort_values("ID do Registro (row_id)").iterrows():
        rid = int(r["ID do Registro (row_id)"])
        ck = CITEKEY_BY_ROW[rid]
        ano = str(r["Ano de Publicação"])
        veic = tex_esc(compact_veiculo(r))
        contrib = compact_contrib(r["Tipo de Contribuição"])
        papel = compact_papel(r["Papel do PADS"])
        cen = compact_cenarios(r["Cenários de classificação"])
        risco = compact_risco(r["risco_vazamento"])
        qa = f"{int(round(r['nota_qa_pct']*100))}\\%({r['faixa_qa'][0]})"
        t1_rows.append(f"{rid} & \\cite{{{ck}}} & {ano} & {veic} & {contrib} & {papel} & {cen} & {risco} & {qa} \\\\")

    tab1 = f"""\\begin{{table}}[tbp]
\\centering
\\caption{{Síntese dos \\nTotal\\ estudos incluídos (ordem de \\texttt{{row\\_id}}). QA: A=Alta, M=Média, B=Baixa; *Val. ext. declarada sem teste externo independente.}}
\\label{{tab:estudos}}
{{\\tiny
\\setlength{{\\tabcolsep}}{{2.0pt}}
\\renewcommand{{\\arraystretch}}{{0.84}}
\\begin{{tabular*}}{{0.98\\textwidth}}{{@{{}}r@{{\\extracolsep{{\\fill}}}} >{{\\raggedright\\arraybackslash}}p{{3.45cm}} c >{{\\raggedright\\arraybackslash}}p{{2.35cm}} l l >{{\\raggedright\\arraybackslash}}p{{2.95cm}} l r@{{}}}}
\\toprule
\\textbf{{ID}} & \\textbf{{Estudo}} & \\textbf{{Ano}} & \\textbf{{Veículo/Tipo}} & \\textbf{{Contrib.}} & \\textbf{{Papel}} & \\textbf{{Cenários}} & \\textbf{{Vaz.}} & \\textbf{{QA}} \\\\
\\midrule
{chr(10).join(t1_rows)}
\\bottomrule
\\end{{tabular*}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab1_estudos.tex").write_text(tab1, encoding="utf-8")

    # Tabela 2: Recorte do PADS (QP2) compacta
    mod_c = split_many(df["Modalidade do PADS"])
    tar_c = df["Tarefas do PADS"].value_counts().to_dict()
    sens_c = split_many(df["Sensores"])
    punho_c = df["Punho(s) usado(s)"].value_counts().to_dict()
    cen_c = split_many(df["Cenários de classificação"])
    cen_na = int(df["Cenários de classificação"].isna().sum())
    sens_na = int(df["Sensores"].isna().sum())

    t2_lines = [
        ("Modalidade*", "Série temporal (IMU) / Questionário (PDNMS) / Metadados", f"{mod_c.get('Série temporal (IMU)',0)}; {mod_c.get('Questionário (PDNMS)',0)}; {mod_c.get('Metadados demográficos-clínicos',0)}", n_tot),
        ("Tarefas motoras", "Todas / Subconjunto / Não rep. / N/A", f"{tar_c.get('Todas',0)}; {tar_c.get('Subconjunto',0)}; {tar_c.get('Não reportado',0)}; {tar_c.get('Não se aplica',0)}", n_tot),
        ("Sensores*", "Giroscópio / Acelerômetro / Outro / Não rep. ou N/A", f"{sens_c.get('Giroscópio',0)}; {sens_c.get('Acelerômetro',0)}; {sens_c.get('Outro',0)}; {sens_na}", n_tot),
        ("Punho(s)", "Ambos / Não rep. / Esq. ou Dir. (1 cada) / N/A", f"{punho_c.get('Ambos',0)}; {punho_c.get('Não reportado',0)}; {punho_c.get('Esquerdo',0)+punho_c.get('Direito',0)}; {punho_c.get('Não se aplica',0)}", n_tot),
        ("Cenários*", r"PD$\times$HC / PD$\times$DD / 3 classes / Outro / DD$\times$HC / N/A", f"{cen_c.get('PD×HC',0)}; {cen_c.get('PD×DD',0)}; {cen_c.get('3 classes (Mult-Class)',0)}; {cen_c.get('Outro',0)}; {cen_c.get('DD×HC',0)}; {cen_na}", n_tot),
    ]
    t2_body = "\n".join(f"{dim} & {cat} & {cnt} & $N={den}$ \\\\" for dim, cat, cnt, den in t2_lines)
    tab2 = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Recorte do dataset PADS nos \\nTotal\\ estudos (QP2). *Campos multirrótulo (somas acima de 100\\%); contagens na ordem das categorias.}}
\\label{{tab:recorte}}
{{\\scriptsize
\\setlength{{\\tabcolsep}}{{3.5pt}}
\\begin{{tabular}}{{@{{}}l l l r@{{}}}}
\\toprule
\\textbf{{Dimensão}} & \\textbf{{Categorias (na ordem das contagens)}} & \\textbf{{Contagens ($n$)}} & \\textbf{{Base}} \\\\
\\midrule
{t2_body}
\\bottomrule
\\end{{tabular}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab2_recorte.tex").write_text(tab2, encoding="utf-8")

    # Tabela 3: Validacao e vazamento (QP4) compacta
    val_c = split_many(df["Estratégia de Validação"])
    unid_c = df["Unidade de particionamento (partitioning unit)"].value_counts().to_dict()
    sep_c = df["Separação por participante (subject-level separation)"].value_counts().to_dict()
    mom_c = df["Balanceamento"].value_counts().to_dict()
    pre_c = df["aux_preproc_apenas_treino"].fillna("Não se aplica").value_counts().to_dict()
    risco_c = df["risco_vazamento"].value_counts().to_dict()

    t3_lines = [
        ("Estratégia*", "k-fold CV / Hold-out / CV aninhada / Não rep. / LOSO / Outra", f"{val_c.get('k-fold CV',0)}; {val_c.get('Hold-out',0)}; {val_c.get('CV aninhada',0)}; {val_c.get('Não reportado',0)}; {val_c.get('Leave-one-subject-out',0)}; {val_c.get('Outra',0)}", "$N=29$"),
        ("Unid. particionamento", "Participante / Não reportado / Não se aplica", f"{unid_c.get('Participante',0)} (81,5\\%); {unid_c.get('Não reportado',0)}; {unid_c.get('Não se aplica',0)}", "$N=27$ (+2 N/A)"),
        ("Separação participante", "Sim explícita / Sim inferida / Pouco claro / N/A", f"{sep_c.get('Sim – explícita',0)}; {sep_c.get('Sim – inferida',0)}; {sep_c.get('Pouco claro',0)}; {sep_c.get('Não se aplica',0)}", "$N=27$ (+2 N/A)"),
        ("Momento balanceam.", "Só no treino / Antes do split / Não rep. / N/A", f"{mom_c.get('Só no treino',0)}; {mom_c.get('Antes do split',0)}; {mom_c.get('Não reportado',0)}; {mom_c.get('Não se aplica',0)}", "$N=29$"),
        ("Pré-proc. só no treino", "Sim / Não / Não reportado / Não se aplica", f"{pre_c.get('Sim',0)}; {pre_c.get('Não',0)}; {pre_c.get('Não reportado',0)}; {pre_c.get('Não se aplica',0)}", "$N=27$ (+2 N/A)"),
        ("Risco de vazamento", "Baixo / Moderado / Alto / Indeterminado / N/A", f"{risco_c.get('Baixo',0)}; {risco_c.get('Moderado',0)}; {risco_c.get('Alto',0)}; {risco_c.get('Indeterminado',0)}; {risco_c.get('Não se aplica',0)}", "$N=27$ (+2 N/A)"),
    ]
    t3_body = "\n".join(f"{dim} & {cat} & {cnt} & {den} \\\\" for dim, cat, cnt, den in t3_lines)
    tab3 = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Protocolos de validação e risco de vazamento reportado (QP4). *Multirrótulo; $N=27$ exclui \\nNaoAplicaveisVaz\\ análises estatísticas (N/A).}}
\\label{{tab:validacao}}
{{\\scriptsize
\\setlength{{\\tabcolsep}}{{3.2pt}}
\\begin{{tabular}}{{@{{}}l l l r@{{}}}}
\\toprule
\\textbf{{Aspecto}} & \\textbf{{Categorias (na ordem das contagens)}} & \\textbf{{Contagens ($n$)}} & \\textbf{{Denominador}} \\\\
\\midrule
{t3_body}
\\bottomrule
\\end{{tabular}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab3_validacao.tex").write_text(tab3, encoding="utf-8")

    # Tabela 4: Desempenho reportado em ordem de row_id (sem ranqueamento, compacta)
    t4_rows = []
    for _, r in df.sort_values("ID do Registro (row_id)").iterrows():
        rid = int(r["ID do Registro (row_id)"])
        ck = CITEKEY_BY_ROW[rid]
        cen, mod, met, val = parse_best_result(r)
        v_strat = compact_val_label(r["Estratégia de Validação"])
        risco = compact_risco(r["risco_vazamento"])
        t4_rows.append(f"{rid} & \\cite{{{ck}}} & {cen} & {mod} & {met} & {val} & {v_strat} ({risco}) \\\\")

    tab4 = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Melhor resultado reportado por estudo (ordem de \\texttt{{row\\_id}}; sem ranqueamento --- protocolos não são comparáveis).}}
\\label{{tab:desempenho}}
{{\\tiny
\\setlength{{\\tabcolsep}}{{1.3pt}}
\\renewcommand{{\\arraystretch}}{{0.80}}
\\begin{{tabular*}}{{0.98\\textwidth}}{{@{{}}r@{{\\extracolsep{{\\fill}}}} >{{\\raggedright\\arraybackslash}}p{{3.08cm}} >{{\\raggedright\\arraybackslash}}p{{2.05cm}} >{{\\raggedright\\arraybackslash}}p{{2.45cm}} >{{\\raggedright\\arraybackslash}}p{{1.15cm}} >{{\\raggedright\\arraybackslash}}p{{2.05cm}} l@{{}}}}
\\toprule
\\textbf{{ID}} & \\textbf{{Estudo}} & \\textbf{{Cenário}} & \\textbf{{Modelo/Método}} & \\textbf{{Métrica}} & \\textbf{{Valor}} & \\textbf{{Validação (Vaz.)}} \\\\
\\midrule
{chr(10).join(t4_rows)}
\\bottomrule
\\end{{tabular*}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab4_desempenho.tex").write_text(tab4, encoding="utf-8")

    # Tabela 5: Lacunas tematicas (QP5) - sem sobreposicao de colunas
    t5_rows = []
    notes_by_theme = [
        "Treino/teste restrito ao PADS; validação externa = 0/29.",
        "Menor acurácia em PD vs.\\ DD.",
        "Falta MDS-UPDRS/H\\&Y e coleta em vida livre.",
        "Fusão, XAI, calibração e controle de vazamento.",
        "Só \\nCodDisponivel/\\nTotal\\ com código ou dados.",
    ]
    # Escolher citacoes representativas curtas para caber na largura
    short_order = [2, 23, 32, 40, 47, 49, 70, 76, 77, 80, 81, 83, 85, 87, 89, 90, 99, 101, 104, 105]
    for (tema, rids), nota in zip(themes, notes_by_theme):
        picks = [i for i in short_order if i in rids][:2]
        if len(picks) < 2:
            picks = rids[:2]
        cites = ", ".join(f"\\cite{{{CITEKEY_BY_ROW[i]}}}" for i in picks)
        t5_rows.append(f"{tema} & {len(rids)}/{n_tot} ({fmt_pct(len(rids), n_tot)}) & {cites} (e +{max(0, len(rids)-len(picks))}) & {nota} \\\\")

    tab5 = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Síntese temática das limitações reportadas, lacunas e reprodutibilidade nos \\nTotal\\ estudos (QP5).}}
\\label{{tab:lacunas}}
{{\\scriptsize
\\setlength{{\\tabcolsep}}{{2.6pt}}
\\renewcommand{{\\arraystretch}}{{0.84}}
\\begin{{tabular}}{{@{{}}>{{\\raggedright\\arraybackslash}}p{{4.40cm}} r >{{\\raggedright\\arraybackslash}}p{{3.55cm}} >{{\\raggedright\\arraybackslash}}p{{4.00cm}}@{{}}}}
\\toprule
\\textbf{{Tema / Lacuna}} & \\textbf{{$n/N$ (\\%)}} & \\textbf{{Exemplos no corpus}} & \\textbf{{Implicação para o PADS}} \\\\
\\midrule
{chr(10).join(t5_rows)}
\\bottomrule
\\end{{tabular}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab5_lacunas.tex").write_text(tab5, encoding="utf-8")

    # Tabela 6: Preprints x Revisados por pares (4.7)
    rev = df[~df["is_preprint"]]
    pre = df[df["is_preprint"]]
    rev_app = int((rev["risco_vazamento"] != "Não se aplica").sum())
    t6_lines = [
        ("Publicação em 2026", f"{int((rev['Ano de Publicação'].astype(str)=='2026').sum())}/23 ({fmt_pct(int((rev['Ano de Publicação'].astype(str)=='2026').sum()), 23)})", "6/6 (100,0\\%)", "15/29 (51,7\\%)"),
        ("Contribuição: Novo modelo", f"{int((rev['Tipo de Contribuição']=='Novo modelo').sum())}/23", "4/6", "17/29"),
        (r"Cenário PD$\times$DD", f"{split_many(rev['Cenários de classificação']).get('PD×DD',0)}/23 ({fmt_pct(split_many(rev['Cenários de classificação']).get('PD×DD',0), 23)})", f"{split_many(pre['Cenários de classificação']).get('PD×DD',0)}/6 ({fmt_pct(split_many(pre['Cenários de classificação']).get('PD×DD',0), 6)})", "15/29 (51,7\\%)"),
        ("Família: Deep Learning", f"{split_many(rev['Família do Algoritmo']).get('Deep Learning',0)}/23 ({fmt_pct(split_many(rev['Família do Algoritmo']).get('Deep Learning',0), 23)})", "6/6 (100,0\\%)", "22/29 (75,9\\%)"),
        ("Separação por participante (Sim)", f"{int(rev['Separação por participante (subject-level separation)'].isin(['Sim – explícita','Sim – inferida']).sum())}/{rev_app}", "6/6", f"{int(df['Separação por participante (subject-level separation)'].isin(['Sim – explícita','Sim – inferida']).sum())}/27"),
        ("Risco de vazamento Baixo", f"{int((rev['risco_vazamento']=='Baixo').sum())}/{rev_app} ({fmt_pct(int((rev['risco_vazamento']=='Baixo').sum()), rev_app)})", f"{int((pre['risco_vazamento']=='Baixo').sum())}/6 ({fmt_pct(int((pre['risco_vazamento']=='Baixo').sum()), 6)})", f"{int((df['risco_vazamento']=='Baixo').sum())}/27 ({fmt_pct(int((df['risco_vazamento']=='Baixo').sum()), 27)})"),
        ("QA faixa Alta (Média QA)", f"{int((rev['faixa_qa']=='Alta').sum())}/23 ({fmt_num(rev['nota_qa_pct'].mean()*100, 1)}\\%)", f"{int((pre['faixa_qa']=='Alta').sum())}/6 ({fmt_num(pre['nota_qa_pct'].mean()*100, 1)}\\%)", f"{int((df['faixa_qa']=='Alta').sum())}/29 ({fmt_num(df['nota_qa_pct'].mean()*100, 1)}\\%)"),
        ("Código/dados disponíveis", f"{int(rev['Código/dados disponíveis'].isin(['Código','Ambos']).sum())}/23", f"{int(pre['Código/dados disponíveis'].isin(['Código','Ambos']).sum())}/6", f"{int(df['Código/dados disponíveis'].isin(['Código','Ambos']).sum())}/29"),
    ]
    t6_body = "\n".join(f"{a} & {b} & {c} & {d} \\\\" for a, b, c, d in t6_lines)
    tab6 = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{Comparação descritiva entre revisados por pares ($n=23$) e \\textit{{preprints}} ($n=6$), e sensibilidade no total ($n=29$).}}
\\label{{tab:preprints}}
{{\\scriptsize
\\setlength{{\\tabcolsep}}{{3.5pt}}
\\renewcommand{{\\arraystretch}}{{0.82}}
\\begin{{tabular*}}{{0.78\\textwidth}}{{@{{}}l@{{\\extracolsep{{\\fill}}}} r r r@{{}}}}
\\toprule
\\textbf{{Indicador}} & \\textbf{{Revisados ($n=23$)}} & \\textbf{{Preprints ($n=6$)}} & \\textbf{{Total ($n=29$)}} \\\\
\\midrule
{t6_body}
\\bottomrule
\\end{{tabular*}}
}}
\\end{{table}}
"""
    (TAB_DIR / "tab6_preprints.tex").write_text(tab6, encoding="utf-8")


def setup_mpl():
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["DejaVu Sans", "Arial", "Helvetica"],
        "font.size": 8.5,
        "axes.edgecolor": "black",
        "axes.linewidth": 0.8,
        "savefig.dpi": 300,
    })


def write_figures(df: pd.DataFrame) -> None:
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    setup_mpl()
    halo = dict(facecolor="white", edgecolor="none", pad=0.8, alpha=0.92)

    # Fig 2: Estudos por ano e tipo de contribuicao
    years = ["2024", "2025", "2026"]
    contribs = ["Novo modelo", "Estudo comparativo", "Análise estatística", "Plataforma-sistema", "Outro"]
    colors = ["#222222", "#666666", "#aaaaaa", "#dddddd", "#ffffff"]
    hatches = ["", "///", "...", "xxx", "\\\\\\"]
    ct = pd.crosstab(df["Ano de Publicação"].astype(str), df["Tipo de Contribuição"]).reindex(index=years, columns=contribs, fill_value=0)

    fig, ax = plt.subplots(figsize=(6.3, 1.82))
    bottom = np.zeros(len(years))
    x = np.arange(len(years))
    for col, col_c, hat in zip(contribs, colors, hatches):
        vals = ct[col].values
        ax.bar(x, vals, width=0.46, bottom=bottom, label=col, color=col_c, edgecolor="black", hatch=hat, linewidth=0.8)
        for xi, v, b in zip(x, vals, bottom):
            if v >= 1:
                if col_c == "#222222":
                    ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="white", fontsize=8.5, fontweight="bold")
                elif col_c == "#666666":
                    ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="white", fontsize=8.5, fontweight="bold",
                            bbox=dict(facecolor="#666666", edgecolor="none", pad=0.8, alpha=0.85))
                else:
                    ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="black", fontsize=8.2, fontweight="bold", bbox=halo)
        bottom += vals
    for xi, tot in zip(x, bottom):
        ax.text(xi, tot + 0.30, f"n={int(tot)}", ha="center", va="bottom", fontsize=9.0, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=9.0)
    ax.set_ylabel("Estudos", fontsize=9.0)
    ax.tick_params(axis="y", labelsize=8.8)
    ax.set_ylim(0, max(bottom) + 2.2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=True, edgecolor="black", fontsize=7.8, loc="upper left")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_ano_contribuicao.pdf", bbox_inches="tight")
    plt.close(fig)

    # Fig 3: Matriz Cenario x Familia de Algoritmo
    cen_order = ["PD×HC", "PD×DD", "3 classes (Mult-Class)", "Outro", "DD×HC"]
    cen_labels = ["PD × HC", "PD × DD", "3 classes", "Outro", "DD × HC"]
    fam_order = ["Deep Learning", "Classical ML", "Hybrid-Ensemble", "Generativo-augmentation", "Auto-supervisionado", "Outro"]
    fam_labels = ["Deep\nLearning", "ML\nClássico", "Híbrido/\nEnsemble", "Generativo/\nAugment.", "Auto-sup.\n(SSL)", "Outro"]

    mat = np.zeros((len(cen_order), len(fam_order)), dtype=int)
    for _, r in df.iterrows():
        if pd.isna(r["Cenários de classificação"]) or pd.isna(r["Família do Algoritmo"]):
            continue
        cs = [x.strip() for x in str(r["Cenários de classificação"]).split("; ")]
        fs = [x.strip() for x in str(r["Família do Algoritmo"]).split("; ")]
        for c_val in cs:
            if c_val in cen_order:
                for f_val in fs:
                    if f_val in fam_order:
                        mat[cen_order.index(c_val), fam_order.index(f_val)] += 1

    fig, ax = plt.subplots(figsize=(6.4, 1.88))
    im = ax.imshow(mat, cmap="Greys", aspect="auto", vmin=0, vmax=max(mat.max(), 1) * 1.15)
    ax.set_xticks(np.arange(len(fam_labels)))
    ax.set_xticklabels(fam_labels, fontsize=8.5)
    ax.set_yticks(np.arange(len(cen_labels)))
    ax.set_yticklabels(cen_labels, fontsize=8.6)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            v = mat[i, j]
            txt_c = "white" if v >= mat.max() * 0.55 else "black"
            ax.text(j, i, str(v), ha="center", va="center", color=txt_c, fontsize=9.2, fontweight="bold" if v > 0 else "normal")
    ax.set_xticks(np.arange(-0.5, len(fam_labels), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(cen_labels), 1), minor=True)
    ax.grid(which="minor", color="black", linestyle="-", linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    cbar = fig.colorbar(im, ax=ax, fraction=0.022, pad=0.02)
    cbar.ax.tick_params(labelsize=8.2)
    cbar.set_label("Ocorrências", fontsize=8.5)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_cenario_familia.pdf", bbox_inches="tight")
    plt.close(fig)

    # Fig 4: Risco de vazamento por unidade e separacao (com halo branco sobre hachuras)
    risk_order = ["Baixo", "Moderado", "Alto", "Indeterminado", "Não se aplica"]
    r_colors = ["#eeeeee", "#aaaaaa", "#444444", "#ffffff", "#dddddd"]
    r_hatches = ["", "///", "", "xxx", "..."]

    fig, axes = plt.subplots(1, 2, figsize=(6.8, 1.82), sharey=True)
    panels = [
        (axes[0], "Unidade de particionamento (partitioning unit)", ["Participante", "Não reportado", "Não se aplica"], ["Participante", "Não reportado", "Não se aplica"], "(a) Unidade de particionamento"),
        (axes[1], "Separação por participante (subject-level separation)", ["Sim – explícita", "Sim – inferida", "Pouco claro", "Não se aplica"], ["Sim expl.", "Sim inf.", "Pouco claro", "N/A"], "(b) Separação por participante"),
    ]
    for ax, col, cats, clabels, title in panels:
        ct_p = pd.crosstab(df[col], df["risco_vazamento"]).reindex(index=cats, columns=risk_order, fill_value=0)
        x = np.arange(len(cats))
        bottom = np.zeros(len(cats))
        for rk, rc, rh in zip(risk_order, r_colors, r_hatches):
            vals = ct_p[rk].values
            ax.bar(x, vals, width=0.52, bottom=bottom, label=rk, color=rc, edgecolor="black", hatch=rh, linewidth=0.8)
            for xi, v, b in zip(x, vals, bottom):
                if v > 0:
                    if rc == "#444444":
                        ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="white", fontsize=8.0, fontweight="bold")
                    elif rh:
                        ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="black", fontsize=8.0, fontweight="bold", bbox=halo)
                    else:
                        ax.text(xi, b + v / 2, str(int(v)), ha="center", va="center", color="black", fontsize=8.0, fontweight="bold")
            bottom += vals
        ax.set_xticks(x)
        ax.set_xticklabels(clabels, fontsize=8.2)
        ax.set_title(title, fontsize=8.8, fontweight="bold")
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
    axes[0].set_ylabel("Estudos", fontsize=8.6)
    axes[0].tick_params(axis="y", labelsize=8.2)
    axes[0].set_ylim(0, 24.5)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 1.07), ncol=5, frameon=True, edgecolor="black", fontsize=7.6)
    fig.tight_layout(rect=[0, 0, 1, 0.92])
    fig.savefig(FIG_DIR / "fig4_risco_vazamento.pdf", bbox_inches="tight")
    plt.close(fig)

    # Fig 5: QA1 a QA5 (com halo branco sobre hachuras)
    qa_cols = ["QA1", "QA2", "QA3", "QA4", "QA5"]
    qa_labels = [
        "QA1: Tarefa definida",
        "QA2: Recorte descrito",
        "QA3: Evita vazamento",
        "QA4: Métricas adequadas",
        "QA5: Replicabilidade",
    ]
    cats = ["Sim (1,0)", "Parcial (0,5)", "Não (0,0)", "N/A"]
    q_colors = ["#333333", "#999999", "#eeeeee", "#ffffff"]
    q_hatches = ["", "///", "", "..."]
    mat_qa = np.zeros((5, 4), dtype=int)
    for i, qc in enumerate(qa_cols):
        s = df[qc]
        mat_qa[i, 0] = int((s == 1.0).sum())
        mat_qa[i, 1] = int((s == 0.5).sum())
        mat_qa[i, 2] = int((s == 0.0).sum())
        mat_qa[i, 3] = int(s.isna().sum())

    fig, ax = plt.subplots(figsize=(6.4, 1.78))
    y = np.arange(len(qa_cols))[::-1]
    left = np.zeros(len(qa_cols))
    for j, (clab, col_c, hat) in enumerate(zip(cats, q_colors, q_hatches)):
        vals = mat_qa[:, j]
        ax.barh(y, vals, height=0.56, left=left, label=clab, color=col_c, edgecolor="black", hatch=hat, linewidth=0.8)
        for yi, v, lft in zip(y, vals, left):
            if v >= 2:
                if col_c == "#333333":
                    ax.text(lft + v / 2, yi, str(int(v)), ha="center", va="center", color="white", fontsize=8.0, fontweight="bold")
                elif hat:
                    ax.text(lft + v / 2, yi, str(int(v)), ha="center", va="center", color="black", fontsize=8.0, fontweight="bold", bbox=halo)
                else:
                    ax.text(lft + v / 2, yi, str(int(v)), ha="center", va="center", color="black", fontsize=8.0, fontweight="bold")
        left += vals
    ax.set_yticks(y)
    ax.set_yticklabels(qa_labels, fontsize=8.4)
    ax.set_xlabel("Estudos (total = 29)", fontsize=8.4)
    ax.tick_params(axis="x", labelsize=8.2)
    ax.set_xlim(0, 29.5)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, 1.22), ncol=4, frameon=True, edgecolor="black", fontsize=7.6)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig5_qa.pdf", bbox_inches="tight")
    plt.close(fig)


def main():
    df_ext = pd.read_excel(XLSX, sheet_name="extracao")
    df_ev = pd.read_excel(XLSX, sheet_name="evidencias")
    df_rev_pts = pd.read_excel(XLSX, sheet_name="revisao")
    df_meta = pd.read_csv(META_CSV)
    df = df_ext.merge(df_meta[["row_id", "tipo_publicacao", "veiculo", "repositorio", "doi"]], left_on="ID do Registro (row_id)", right_on="row_id", how="left")
    df["is_preprint"] = df["tipo_publicacao"] == "preprint"

    themes = compute_gap_themes(df)
    write_macros(df, df_ev, df_rev_pts, themes)
    write_tables(df, themes)
    write_figures(df)
    print("Artefatos regenerados com sucesso!")


if __name__ == "__main__":
    main()
