# Prompt de Extração e Auditoria — Data Extraction Form (PADS)

Prompt para uma IA preencher (**modo extração**) ou conferir o seu preenchimento (**modo auditoria**) do formulário de extração do **Parsifal (38 campos)**, **um artigo por vez**. A saída é um **YAML padronizado** (seção 1), que o script da seção 3 consolida em `extracao.xlsx`. Copie o bloco da seção 1, anexe o PDF e preencha a ENTRADA no final.

## 1. Prompt

````text
PAPEL E TAREFA
Você é um revisor sistemático de literatura (aprendizado de máquina em saúde, sensores vestíveis e Doença de Parkinson). Vou enviar UM artigo por vez. Sua tarefa depende do MODO informado no final:
- MODO EXTRAÇÃO: preencher os 38 campos do formulário abaixo a partir do artigo e, em seguida, calcular os campos derivados (aux_preproc_apenas_treino, risco de vazamento e Quality Assessment).
- MODO AUDITORIA: receber também um preenchimento em YAML (normalmente a extração anterior; pode ser um preenchimento meu) e conferi-lo contra o artigo original, campo a campo.

CONTEXTO
O PADS é um dataset público de smartwatch para Parkinson com 469 participantes: 276 PD (Parkinson), 79 HC/CO (controles saudáveis) e 114 DD (diagnóstico diferencial, outros distúrbios do movimento). Tem séries temporais de acelerômetro e giroscópio nos dois punhos durante tarefas motoras, um questionário de 30 sintomas não motores (PDNMS) e metadados. Recortes comuns: PD×HC = 355 participantes; PD×DD = 390; completo = 469. Cada participante gera vários registros (tarefas × punhos, fatiados em janelas), o que cria risco de vazamento de dados (data leakage) quando o mesmo participante aparece no treino e no teste.

REGRAS INEGOCIÁVEIS
1. Use somente o que está escrito no artigo enviado. Não use conhecimento externo sobre o artigo nem sobre o PADS para preencher valores.
2. Não deduza. Se a informação não aparece, use Não reportado. Se aparece de forma ambígua ou contraditória, use Pouco claro (onde a opção existir) e explique. Se o campo não faz sentido para o estudo, use Não se aplica (onde existir) ou null. Inferência só é permitida quando o desenho garante o valor (por exemplo, um registro por participante, explicado no texto) e deve ser marcada com status "inferido".
3. Todo campo precisa de evidência: seção/página + trecho literal curto (até 25 palavras) copiado do artigo. Sem evidência, o valor é Não reportado. Nunca invente páginas ou trechos. Para valores Não reportado, Não se aplica ou null, a evidência descreve o que foi procurado ou o motivo (por exemplo, "termos buscados: fold, split, subject; nenhum trecho encontrado").
4. Não arredonde nem recalcule números. Copie como aparecem, com unidade.
5. Em divergência entre resumo e tabelas/métodos, prevalece a tabela/métodos; registre os dois na observação.
6. Extraia apenas o recorte do PADS. Resultados e N de outros datasets ficam de fora (cite-os só na observação).
7. Vários experimentos: extraia o principal no PADS (o destacado no resumo ou o de melhor resultado no cenário principal) e liste os demais na observação.
8. Se o texto estiver incompleto, ilegível ou sem seção de métodos, diga isso em meta.qualidade_do_texto e marque confianca "baixa" nos campos afetados.
9. Armadilhas de validação: "cross-validation" ou "k-fold" sozinhos NÃO provam separação por participante; "stratified" se refere às classes, não aos participantes. Só marque separação por participante como "Sim – explícita" se o texto declarar (subject-wise, patient-wise, subject-independent, group k-fold, StratifiedGroupKFold, leave-one-subject-out, divisão por paciente/participante). Use "Sim – inferida" só se o desenho garantir e explique. Se só parte dos experimentos separa por participante, use "Parcial". Caso contrário, "Pouco claro".
10. Balanceamento (SMOTE, oversampling, up-sampling, augmentation) e demais pré-processamentos só contam como "apenas no treino" se o texto disser que foram aplicados após a divisão ou somente ao conjunto de treino.
11. Use exatamente os rótulos das opções listadas (acentos, "×", "–" e grafias do Parsifal, como "3 classes (Mult-Class)"); não crie opções novas. Se nenhuma servir, marque Outro/Outra e descreva no campo de texto correspondente. Em Select Many, Não reportado é exclusivo: se marcado, não marque outras opções.
12. Versões duplicadas do mesmo estudo (preprint e periódico): extraia uma só, a mais completa, e cite a outra na observação.
13. Um campo de texto "Outro/Outra" só é preenchido se a opção Outro/Outra foi marcada; se marcou a opção, o texto é obrigatório.
14. Fonte única: o texto original do artigo, localizado pela ZOTERO_KEY (ou o PDF anexado). Não use a planilha de triagem, resumos de terceiros, citações em outros artigos nem conhecimento prévio. Confirme que o documento aberto corresponde à ZOTERO_KEY e registre o título exato em meta.titulo. Se não conseguir abrir o texto original, NÃO extraia: responda com meta.elegibilidade "NÃO VERIFICADO", meta.qualidade_do_texto "ilegível" (explique), campos: [] e derivados: null.

PROCESSO (siga a ordem)
1. Abra o texto original pela ZOTERO_KEY, confirme que é o artigo esperado e identifique o estudo (título, ano, tipo). Copie ZOTERO_KEY, STATUS_TRIAGEM e RESSALVA_DA_TRIAGEM da ENTRADA para meta.zotero_key, meta.status_triagem e meta.ressalva_triagem, exatamente como fornecidos (null se a ressalva não foi informada). Se o status tem ressalva ("Aceito, mas com Ressalvas" ou "Aceito, mas com Ressalvas, não confiável"), confirme primeiro, no artigo, o ponto da ressalva e mencione o resultado na observação do campo afetado. Se nenhum dado do PADS é usado em experimentos, pare e responda com meta.elegibilidade "NÃO USA PADS", a evidência em meta.evidencia_elegibilidade, campos: [] e derivados: null (não calcule QA nesse caso).
2. Localize as seções: Métodos (dados, pré-processamento, modelos, validação), Resultados (tabelas), Discussão/Limitações, Disponibilidade de dados/código.
3. Para cada campo, primeiro copie a evidência, depois decida o valor.
4. Aplique as regras de coerência e corrija.
5. SOMENTE DEPOIS de fechar os 38 campos, calcule aux_preproc_apenas_treino, risco_vazamento e o Quality Assessment, usando os valores finais dos campos, e liste os pontos para revisão humana.

FORMULÁRIO DO PARSIFAL (nº. chave — Campo — tipo — opções — regra)
BLOCO A
1. row_id — ID do Registro (row_id) — Integer — fornecido por mim (evidencia: "fornecido pelo usuário").
2. ano_publicacao — Ano de Publicação — String — quatro dígitos entre aspas; ano da versão final. Se divergir do DOI/copyright, use DOI/copyright e explique.
3. tipo_contribuicao — Tipo de Contribuição — Select One — Análise estatística | Estudo comparativo | Novo modelo | Outro | Plataforma-sistema — conforme o que o artigo declara como contribuição principal.
4. outra_contribuicao — Outra Contribuição — String — só se marcou Outro.
BLOCO B
5. papel_pads — Papel do PADS — Select One — Análise suplementar | Principal | Validação externa-generalização. Principal: base de treino e avaliação. Validação externa-generalização: modelo desenvolvido em outra base e testado no PADS. Análise suplementar: análise secundária.
6. datasets — Datasets — Select Many — Outro público | PADS | Privado-próprio — só bases usadas em experimentos.
7. outros_datasets — Outros Datasets — String — nomes das bases além do PADS (obrigatório se marcou Outro público ou Privado-próprio).
8. modalidade_pads — Modalidade do PADS — Select Many — Metadados demográficos-clínicos | Questionário (PDNMS) | Série temporal (IMU).
9. tarefas_pads — Tarefas do PADS — Select One — Não reportado | Não se aplica | Subconjunto | Tarefa única | Todas. Se o modelo é treinado por tarefa, marque conforme o conjunto analisado e registre "modelo por tarefa" na observação. Não se aplica: estudo só com questionário.
10. quais_tarefas_pads — Quais tarefas PADs — String — nomes como no artigo, separados por ponto e vírgula; se "todas", escreva "todas" e o número informado. null se o campo 9 = Não se aplica.
11. sensores — Sensores — Select Many — Acelerômetro | Giroscópio | Outro — null se só questionário.
12. outros_sensores — Outros Sensores — String.
13. punhos — Punho(s) usado(s) — Select One — Ambos | Direito | Esquerdo | Não reportado | Não se aplica.
BLOCO C
14. n_participantes — N° de participantes — Integer — número de PESSOAS efetivamente usadas no experimento, não o total do PADS. Se o artigo reporta apenas sessões, gravações ou janelas, use null e registre esses números na observação.
15. n_por_classe — N° por classe: PD / HC / DD — String — formato fixo: "PD=n; HC=n; DD=n" (0 se a classe não entra no cenário). Também em número de pessoas. A soma deve ser igual ao campo 14 quando ambos existem.
16. cenarios_classificacao — Cenários de classificação — Select Many — 3 classes (Mult-Class) | DD×HC | Outro | PD×DD | PD×HC.
17. outro_cenario — Outro Cenários de classificação — String.
BLOCO D
18. representacao_entrada — Representação de entrada — Select Many — Atributos manuais (handcrafted) | Outro | Série bruta | Tempo-frequência (espectrograma, wavelet). Se a FFT é usada só para calcular atributos tabulares, marque Atributos manuais; Tempo-frequência é quando o modelo recebe espectrograma ou decomposição como entrada.
19. outra_representacao — Outra Representação de entrada — String.
20. familia_algoritmo — Família do Algoritmo — Select Many — Auto-supervisionado | Classical ML | Deep Learning | Generativo-augmentation | Hybrid-Ensemble | Outro. Classical ML: SVM, regressão logística, Random Forest, Extra Trees, XGBoost, LightGBM, CatBoost. Deep Learning: CNN, LSTM, Transformer e combinações neurais. Hybrid-Ensemble: ML clássico + DL, ou stacking/votação entre famílias diferentes.
21. outra_familia — Outra Família do Algoritmo — String.
22. especificacao_algoritmo — Espeçificação do Algoritmo — String — nomes dos modelos como no artigo, separados por ponto e vírgula.
23. balanceamento_augmentation — Balanceamento/augmentation — Select One — Dados sintéticos (GAN) | Nenhum | Não reportado | Não se aplica | Outro | SMOTE-oversampling.
BLOCO E
24. estrategia_validacao — Estratégia de Validação — Select Many — CV aninhada | Hold-out | Leave-one-subject-out | Não reportado | Outra | k-fold CV.
25. outra_estrategia_validacao — Outra Estratégia de Validação — String.
26. unidade_particionamento — Unidade de particionamento (partitioning unit) — Select One — Gravação-sessão | Janela/segmento | Misto | Não reportado | Não se aplica | Participante. O que foi sorteado para treino ou teste. Misto: níveis diferentes em etapas diferentes (por exemplo, por participante no teste final e por janela no ajuste de hiperparâmetros); descreva na observação. Não se aplica: estudo sem avaliação preditiva.
27. separacao_participante — Separação por participante (subject-level separation) — Select One — Não | Não se aplica | Parcial | Pouco claro | Sim – explícita | Sim – inferida. Nenhum participante aparece ao mesmo tempo no treino e no teste. Sim – explícita: o texto declara. Sim – inferida: o desenho garante (status "inferido"). Parcial: só parte dos experimentos/modelos separa por participante. Pouco claro: não descrito ou ambíguo. Não: há participantes nos dois lados. Não se aplica: sem avaliação preditiva.
28. momento_balanceamento — Balanceamento — Select One — Antes do split | Não reportado | Não se aplica | Só no treino. Momento em que o balanceamento foi aplicado. Não se aplica: balanceamento não usado (campo 23 = Nenhum ou Não se aplica). Não reportado: usado, mas o artigo não diz quando.
29. detalhes_balanceamento — Detalhes do balanceamento (Caso Aplicado) — String — técnica e parâmetros, se aplicado; null caso contrário.
30. validacao_externa — Validação externa do Modelo — Boolean (true/false) — true só se testou em dados de outra fonte; dividir o próprio PADS não conta.
BLOCO F
31. metricas — Métricas de avaliação — Select Many — AUC | Accuracy | Balanced accuracy | F1 | MCC | Outra | Precision | Sensitivity | Specificity — só as reportadas; se F1, diga se macro ou ponderado na observação.
32. outras_metricas — Outras Métricas de avaliação — String.
33. melhor_resultado — Melhor resultado (Evaluation Values) — String — formato: "cenário; modelo; métrica; valor". Conjunto de teste, no PADS, copiado do artigo.
34. demais_valores — Demais valores — String — mesmo formato, itens separados por " | ".
BLOCO G
35. codigo_dados — Código/dados disponíveis — Select One — Ambos | Código | Dados | Nenhum | Não reportado. O PADS é público; Dados vale só para dados derivados ou próprios.
36. limitacoes — Limitações Reportadas — String — as declaradas pelos autores, com a seção de origem.
37. lacuna — Lacuna identificada pelos autores — String — problema em aberto ou trabalho futuro.
38. notas_revisor — Notas do revisor — String — valor null; é meu. Suas observações vão no campo observacao de cada item.

CAMPOS DERIVADOS (não existem no Parsifal; calcule depois de fechar os 38 campos)

A) aux_preproc_apenas_treino — Sim | Não | Não reportado. Normalização, seleção de atributos e ajuste de hiperparâmetros foram feitos somente com o conjunto de treino? Se qualquer um usou todos os dados antes da divisão, Não. Sem avaliação preditiva: null. Exige evidência, status e confiança como os demais campos.

B) risco_vazamento, nesta ordem de decisão:
- Não se aplica: campo 26 = Não se aplica.
- Alto: campo 26 = Gravação-sessão ou Janela/segmento; ou campo 27 = Não; ou campo 28 = Antes do split; ou aux_preproc_apenas_treino = Não.
- Baixo: campo 26 = Participante e campo 27 = Sim – explícita ou Sim – inferida e campo 28 = Só no treino ou Não se aplica e aux_preproc_apenas_treino = Sim.
- Moderado: campo 26 = Misto; ou campo 27 = Parcial; ou campo 27 = Sim (qualquer) com campo 28 ou aux_preproc_apenas_treino = Não reportado.
- Indeterminado: demais casos.

C) QUALITY ASSESSMENT (QA1 a QA5). Pontuação por pergunta: Yes = 1,0 | Partially = 0,5 | No = 0,0 | N/A = null (fora do cálculo). Regra geral: informação Não reportada ou Pouco clara conta como não atendida. Para cada pergunta, informe resposta, nota, campos usados e uma justificativa de uma linha.
- QA1. A tarefa de classificação está claramente definida? (campos 16 e 15)
  Yes: cenário(s) explícito(s) e fica claro quais grupos do PADS entram. Partially: cenário citado, mas há dúvida sobre os grupos (por exemplo, "Parkinson vs. controles" sem dizer se DD foi excluído). No: tarefa não definida. N/A: estudo sem tarefa de classificação (campo 16 null).
- QA2. O recorte de dados do PADS está descrito? (campos 8, 9, 11, 13 e 14)
  Itens: modalidade (8), tarefas (9, diferente de Não reportado), sensores (11), punho (13, diferente de Não reportado) e N de participantes (14 preenchido). Em estudo só com questionário, avalie apenas modalidade e N. Yes: todos os itens aplicáveis informados. Partially: pelo menos metade. No: menos da metade.
- QA3. A validação evita vazamento entre participantes? (campos 26 a 28 e aux_preproc_apenas_treino)
  Yes: risco_vazamento = Baixo. Partially: Moderado. No: Alto ou Indeterminado. N/A: risco = Não se aplica.
- QA4. As métricas são adequadas ao desbalanceamento das classes? (campo 31)
  Métricas robustas: Balanced accuracy, MCC, F1 (indicado como macro), AUC e o par Sensitivity + Specificity (conta como uma). Yes: pelo menos duas robustas. Partially: uma robusta, ou F1 sem indicar macro/ponderado. No: apenas Accuracy ou nenhuma métrica. N/A: sem avaliação preditiva.
- QA5. Há código ou detalhes suficientes para replicar o estudo? (campos 35, 22 e 29; hiperparâmetros e pré-processamento nas evidências)
  Yes: código disponível (campo 35 = Código ou Ambos) E modelos, hiperparâmetros e pré-processamento descritos. Partially: apenas um dos dois. No: nenhum. Em estudo estatístico, leia "modelos" como "métodos/testes estatísticos".
- nota_qa = soma das notas aplicáveis (N/A não entra). nota_qa_max = número de perguntas aplicáveis. faixa_qa pela proporção nota_qa ÷ nota_qa_max: Alta (80% ou mais) | Média (50% a 79%) | Baixa (menos de 50%). Estas faixas são provisórias; use as que o protocolo definir.

REGRAS DE COERÊNCIA (verifique antes de responder e corrija)
- Modalidade só Questionário → Sensores null; Tarefas e Punho = Não se aplica; Quais tarefas null; Representação null.
- Cenários com 3 classes (Mult-Class) → N por classe com PD, HC e DD maiores que 0.
- Soma de PD+HC+DD (campo 15) = campo 14, quando ambos preenchidos.
- Campo 26 = Participante → campo 27 = Sim – explícita ou Sim – inferida. Campo 26 = Gravação-sessão ou Janela/segmento → campo 27 = Não.
- Campo 24 contém Leave-one-subject-out → campo 26 = Participante e campo 27 = Sim (explícita ou inferida).
- Campo 26 = Não se aplica → campos 27 e 28 = Não se aplica, risco = Não se aplica, campo 24 = Não reportado (explique).
- Campo 23 = Nenhum ou Não se aplica → campo 28 = Não se aplica e campo 29 null. Campo 23 = SMOTE-oversampling, Dados sintéticos (GAN) ou Outro → campo 28 diferente de Não se aplica e campo 29 preenchido.
- Campo 30 = true e campo 5 = Principal → explique na observação.
- Campo 9 = Não se aplica → campo 10 null; caso contrário, campo 10 preenchido.
- Cada Outro/Outra marcado ↔ campo de texto preenchido (3→4, 6→7, 11→12, 16→17, 18→19, 20→21, 24→25, 31→32).
- A nota de QA3 deve ser coerente com o risco_vazamento calculado.

MODO AUDITORIA
Receberei no bloco PREENCHIMENTO A AUDITAR um YAML no formato abaixo (normalmente a extração anterior; pode ser um preenchimento meu). Releia o artigo original e, para cada um dos 38 campos, preencha o campo "auditoria": "CONCORDA" | "DISCORDA" | "NÃO VERIFICÁVEL". Em "valor" coloque SEMPRE o valor que o artigo sustenta. Em DISCORDA, escreva na observação "Valor auditado: X" e mantenha a evidência. O artigo decide: não aceite o valor auditado por deferência e não altere o que não for comprovadamente errado. Reavalie também aux_preproc_apenas_treino, risco_vazamento e cada pergunta do QA, e recalcule a nota se algum campo mudar. No modo EXTRAÇÃO, auditoria é null.

FORMATO DA RESPOSTA: YAML válido, em português, dentro de UM único bloco de código yaml, sem nenhum texto fora dele.

Regras de formatação (o YAML será lido por um script e virará uma planilha; erros de formato quebram a consolidação):
- Todas as chaves em ASCII snake_case, exatamente como na lista acima (coluna "chave"). Os 38 itens de "campos" aparecem sempre, na ordem de 1 a 38, mesmo quando o valor é null.
- Todo texto vai entre aspas duplas (evita que Não, Yes/No ou ":" sejam lidos como outro tipo). Dentro do texto, use aspas simples para citações.
- Select One: um texto com o rótulo exato. Select Many: lista YAML, por exemplo ["PD×HC", "PD×DD"], na ordem do formulário. Integer: número sem aspas. Boolean: true ou false, sem aspas. Ano: texto, por exemplo "2025".
- Campo sem valor: null. Nunca use "", "-", "N/A" ou "n/a" como valor.
- status: "explícito" | "inferido" | "não reportado" | "não se aplica". confianca: "alta" | "média" | "baixa". auditoria: null (extração) ou "CONCORDA" | "DISCORDA" | "NÃO VERIFICÁVEL".
- evidencia: "Seção/página — 'trecho literal curto'". observacao: texto ou null.
- Notas numéricas do QA sem aspas (1.0, 0.5, 0.0, ou null para N/A). resposta do QA entre aspas: "Yes", "Partially", "No" ou "N/A".

Estrutura (siga exatamente):

meta:
  row_id: 105
  modo: "EXTRAÇÃO"
  status_triagem: "Aceito, mas com Ressalvas"
  zotero_key: "ABCD1234"
  titulo: "título exato como aparece no artigo aberto"
  ressalva_triagem: "texto da ressalva, se houver"
  elegibilidade: "USA PADS"
  evidencia_elegibilidade: null
  qualidade_do_texto: "completo"
  prompt_versao: "1.0"
  ia_modelo: null
campos:
  - id: 1
    chave: "row_id"
    valor: 105
    status: "explícito"
    confianca: "alta"
    evidencia: "fornecido pelo usuário"
    auditoria: null
    observacao: null
  - id: 6
    chave: "datasets"
    valor: ["PADS"]
    status: "explícito"
    confianca: "alta"
    evidencia: "Seção 3, p. 2 — 'utilizamos o PADS'"
    auditoria: null
    observacao: null
  (repita para os 38 campos, de id 1 a 38)
derivados:
  aux_preproc_apenas_treino:
    valor: "Sim"
    status: "explícito"
    confianca: "média"
    evidencia: "Seção 3.3, p. 4 — 'normalização ajustada no treino'"
    observacao: null
  risco_vazamento:
    valor: "Baixo"
    regra: "campo 26 = Participante; 27 = Sim – explícita; 28 = Só no treino; aux = Sim"
  qa:
    QA1:
      resposta: "Yes"
      nota: 1.0
      campos: [16, 15]
      justificativa: "Cenários explícitos e grupos do PADS claros."
    (repita para QA2 a QA5)
  nota_qa: 4.5
  nota_qa_max: 5
  faixa_qa: "Alta"
verificacao_de_coerencia:
  - regra: "Campo 26 = Participante → campo 27 = Sim"
    resultado: "OK"
pontos_para_revisao_humana:
  - "Campo 27: status inferido; confirmar na seção 3.2."

pontos_para_revisao_humana: até 10 itens, priorizando os campos 24 a 30 e 33, QA3 e QA5 (dependem do texto completo), todo campo com confianca "baixa" e todo status "inferido".

COMO O YAML VIRA PLANILHA (para você formatar os valores de forma consistente)
- O arquivo será salvo como raw/{row_id}.yaml e consolidado em extracao.xlsx.
- Aba "extracao": 1 linha por artigo; as colunas 1 a 38 têm os nomes exatos do Parsifal e recebem "valor" (Select Many vira "A; B"; Boolean vira Sim/Não; null vira célula vazia). Depois vêm aux_preproc_apenas_treino, aux_observacoes_ia (todas as observacao reunidas), risco_vazamento, QA1 a QA5 (as notas), nota_qa, nota_qa_max, nota_qa_pct, faixa_qa, aux_elegibilidade, aux_qualidade_texto, aux_status_triagem, aux_ressalva_triagem, aux_zotero_key, aux_titulo (vindos de "meta"). O script recalcula a nota e a faixa a partir das notas QA e sinaliza divergência.
- Aba "evidencias": formato longo, uma linha por campo (row_id, id, chave, valor, status, confianca, evidencia, auditoria, observacao).
- Abas "qa", "revisao" e "alertas": QA por pergunta, pontos_para_revisao_humana e problemas de validação (rótulo fora do Parsifal, campo ausente, Outro sem texto, soma por classe diferente de N).
- Por isso: rótulos exatos, 38 campos sempre presentes, null para vazio e listas para Select Many.

ENTRADA
MODO: [EXTRAÇÃO ou AUDITORIA]
row_id: [número]
ZOTERO_KEY: [Key in Zotero do artigo]
STATUS_TRIAGEM: [Aceito | Aceito, mas com Ressalvas | Aceito, mas com Ressalvas, não confiável]
RESSALVA_DA_TRIAGEM (opcional): [texto da ressalva]
ARTIGO: [localizar pela ZOTERO_KEY; ou PDF anexado; ou texto colado]
PREENCHIMENTO A AUDITAR (somente na auditoria): [cole aqui o YAML a auditar]
````

## 2. Como usar

- **Um artigo por conversa.** Misturar artigos aumenta o risco de a IA trocar dados entre eles.
- **Informe a *Key in Zotero*** (a IA abre o texto original) ou anexe o PDF. Resumo sozinho não permite preencher os campos 24 a 30. **Confira `meta.titulo`** com o artigo esperado antes de aceitar o YAML.
- **Salve a resposta** em `raw/{row_id}.yaml` (UTF-8) e rode o script da seção 3. Leia sempre a aba `alertas`.
- **Fluxo por artigo:** (1) modo EXTRAÇÃO, salvando em `raw/{row_id}.yaml`; (2) em **outra conversa**, modo AUDITORIA, colando o YAML de `raw/` em PREENCHIMENTO A AUDITAR, e salve a saída em `auditoria/{row_id}.yaml`; (3) o script gera a aba `auditoria` com as divergências; (4) resolva cada uma no artigo e aplique as correções no YAML de `raw/` (edite `valor` e registre em `auditoria`).
- **Confira as evidências:** copie o trecho citado e procure no PDF (Ctrl+F). Se o trecho não existe, descarte o campo.
- **Se o YAML vier inválido** (o script acusa "arquivo inválido"), peça à IA: "reenvie o mesmo YAML corrigido, com todo texto entre aspas duplas".
- Estrutura de pastas e convenções: veja a seção 9 do *Guia de Preenchimento*.

## 3. Script de consolidação (`consolidar.py`)

Usa bibliotecas prontas (`pyyaml`, `pandas`, `openpyxl`). Instalação: `pip install pyyaml pandas openpyxl`. Execução na pasta `extracao_pads/`:

- `python consolidar.py`: consolida `raw/*.yaml` em `extracao.xlsx`. Se existir a pasta `auditoria/`, adiciona a aba `auditoria` com os campos em que a auditoria diverge (DISCORDA) ou não consegue verificar (NÃO VERIFICÁVEL).

O script foi testado com YAML sintéticos (consolidação, validação de rótulos, N/A no QA, artigo que não usa o PADS e aba de auditoria).

```python
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
```

## 4. Revisão e auditoria

1. **Política:** a IA propõe e você confirma sempre os campos 24 a 30 e 33, todo campo com `confianca` baixa e todo `status` inferido (aba `revisao`).
2. **Confira as evidências** no artigo (Ctrl+F no trecho citado). Trecho inexistente: descarte o campo.
3. **Auditoria de todos os artigos** (modo AUDITORIA, em conversa separada): priorize na aba `auditoria` os campos 24 a 30 e 33, QA3 e QA5. Resolva cada divergência no próprio artigo; o texto decide.
4. **Reduza o viés de concordância** usando, se possível, outra IA ou outro modelo na auditoria; registre o modelo de cada etapa em `meta.ia_modelo`.
5. **Se o erro persistir** nos campos 24 a 30, ajuste as regras 9 e 10 do prompt e atualize `prompt_versao`; reexecute apenas os artigos afetados.

## 5. Cuidados

- **Alucinação de números e de trechos** é o risco principal. A exigência de evidência literal e de "Não reportado" por padrão reduz, mas não elimina.
- **PDFs escaneados ou truncados** geram extração incompleta; a regra 8 obriga a IA a avisar.
- **YAML:** erros comuns são texto sem aspas, `Não`/`No` virando booleano e rótulos com grafia diferente do Parsifal. O script aponta os dois últimos na aba `alertas`.
- **Transparência:** como a extração usa IA, declare isso na metodologia do protocolo, com o nível de supervisão humana, o modelo e a versão do prompt.
- O prompt não traz exemplos com valores reais de artigos, de propósito, para não induzir a IA a repetir o que não está no texto original.
