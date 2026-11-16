# Guia de Preenchimento — Data Extraction Form (estudos com o PADS)

Guia para extrair dados dos **29 estudos aceitos** na triagem, no formato do **Parsifal (38 campos)**. Cada campo traz: o que significa, onde procurar no artigo, como decidir e os casos duvidosos.

**Padrão adotado:** o formulário do Parsifal manda em tudo (ordem, nomes e rótulos das opções). Os nomes são copiados **exatamente** como estão no Parsifal, inclusive as grafias dele (*Mult-Class*, *Espeçificação*, *Quais tarefas PADs*). Não corrija essas grafias na hora de preencher.

**Fonte única:** todos os valores vêm do **texto original do artigo**, localizado pela *Key in Zotero* de cada `row_id`. Não use resumos, colunas ou anotações da triagem como fonte de dados (o status de triagem serve só para análise de sensibilidade).

## 1. Princípios gerais

1. **Extraia o que está escrito, não o que você supõe.** Se o artigo não diz, não deduza.
2. **Três respostas de "sem informação" têm sentidos diferentes:**
   - **Não reportado:** o artigo deveria informar, mas não informa.
   - **Pouco claro:** o artigo informa, mas de forma ambígua ou contraditória.
   - **Não se aplica:** o campo não faz sentido para aquele estudo (por exemplo, *Punho* em estudo só com questionário).
3. **Registre a evidência.** No YAML, cada campo tem `evidencia` (seção/página + trecho literal curto) e `observacao`. No Parsifal, resuma o que for duvidoso em *Notas do revisor* (campo 38).
4. **Texto completo vence o resumo.** Se só leu o resumo, escreva "só resumo" na observação.
5. **Vários experimentos no mesmo artigo:** extraia o experimento principal com o PADS (o destacado no resumo ou o de melhor resultado no cenário principal) e cite os demais na observação. Campos Select Many aceitam mais de uma marcação.
6. **Estudos que usam o PADS só em parte:** extraia **apenas o recorte do PADS** e marque o papel dele no campo 5.
7. **Estudos sem avaliação preditiva** (análises estatísticas): preencha identificação, PADS e amostra; em *Unidade de particionamento* e *Separação por participante* use `Não se aplica`; em *Estratégia de Validação* (sem opção `Não se aplica`) use `Não reportado` e explique.
8. **Versões duplicadas** (preprint e artigo de periódico do mesmo estudo): extraia **uma** versão, a final/mais completa, e anote a outra na observação. Não conte o estudo duas vezes.
9. **Rótulos idênticos ao Parsifal.** Copie acentos, "×", "–" (de `Sim – explícita`) e grafias exatamente.
10. **Campo "Outro/Outra" marcado ⇔ campo de texto preenchido.** Só preencha o texto se marcou a opção; se marcou a opção, o texto é obrigatório.

## 2. O PADS em um minuto

- Dataset público de smartwatch para Parkinson, com **469 participantes**: **276 PD** (Parkinson), **79 HC/CO** (controles saudáveis) e **114 DD** (diagnóstico diferencial: outros distúrbios do movimento).
- Os sujeitos fazem **tarefas motoras** com sensores nos dois punhos (acelerômetro e giroscópio). Os artigos contam entre 11 e 14 tarefas; registre o número que o artigo informar.
- Há também um **questionário de 30 sintomas não motores (PDNMS)** e metadados (idade, sexo, lateralidade etc.).
- **Recortes comuns:** PD×HC = 355 sujeitos (276+79); PD×DD = 390 (276+114); série completa = 469.
- Cada sujeito gera **vários registros** (tarefas × punhos, fatiados em janelas). Isso é a raiz do risco de vazamento de dados (campos 26 a 28).

## 3. Ordem de leitura sugerida (10 a 15 min por artigo)

1. **Resumo e Introdução:** contribuição, dataset, cenários.
2. **Métodos:** participantes, pré-processamento, modelo, validação.
3. **Resultados:** tabelas (prefira a tabela ao número do resumo).
4. **Discussão e Limitações.**
5. **Disponibilidade de dados/código** (fim do artigo).

**Busca rápida (Ctrl+F):** PADS, subject, patient, fold, split, leave-one, hold-out, nested, SMOTE, oversampl, up-sampl, normaliz, leakage, GitHub.

## 4. Referência rápida dos 38 campos

`chave` é o nome estável usado no YAML e no script (seção 9).

| Nº | `chave` | Campo (Parsifal) | Tipo |
| --- | --- | --- | --- |
| 1 | `row_id` | ID do Registro (row_id) | Integer |
| 2 | `ano_publicacao` | Ano de Publicação | String |
| 3 | `tipo_contribuicao` | Tipo de Contribuição | Select One |
| 4 | `outra_contribuicao` | Outra Contribuição | String |
| 5 | `papel_pads` | Papel do PADS | Select One |
| 6 | `datasets` | Datasets | Select Many |
| 7 | `outros_datasets` | Outros Datasets | String |
| 8 | `modalidade_pads` | Modalidade do PADS | Select Many |
| 9 | `tarefas_pads` | Tarefas do PADS | Select One |
| 10 | `quais_tarefas_pads` | Quais tarefas PADs | String |
| 11 | `sensores` | Sensores | Select Many |
| 12 | `outros_sensores` | Outros Sensores | String |
| 13 | `punhos` | Punho(s) usado(s) | Select One |
| 14 | `n_participantes` | N° de participantes | Integer |
| 15 | `n_por_classe` | N° por classe: PD / HC / DD | String |
| 16 | `cenarios_classificacao` | Cenários de classificação | Select Many |
| 17 | `outro_cenario` | Outro Cenários de classificação | String |
| 18 | `representacao_entrada` | Representação de entrada | Select Many |
| 19 | `outra_representacao` | Outra Representação de entrada | String |
| 20 | `familia_algoritmo` | Família do Algoritmo | Select Many |
| 21 | `outra_familia` | Outra Família do Algoritmo | String |
| 22 | `especificacao_algoritmo` | Espeçificação do Algoritmo | String |
| 23 | `balanceamento_augmentation` | Balanceamento/augmentation | Select One |
| 24 | `estrategia_validacao` | Estratégia de Validação | Select Many |
| 25 | `outra_estrategia_validacao` | Outra Estratégia de Validação | String |
| 26 | `unidade_particionamento` | Unidade de particionamento (partitioning unit) | Select One |
| 27 | `separacao_participante` | Separação por participante (subject-level separation) | Select One |
| 28 | `momento_balanceamento` | Balanceamento | Select One |
| 29 | `detalhes_balanceamento` | Detalhes do balanceamento (Caso Aplicado) | String |
| 30 | `validacao_externa` | Validação externa do Modelo | Boolean |
| 31 | `metricas` | Métricas de avaliação | Select Many |
| 32 | `outras_metricas` | Outras Métricas de avaliação | String |
| 33 | `melhor_resultado` | Melhor resultado (Evaluation Values) | String |
| 34 | `demais_valores` | Demais valores | String |
| 35 | `codigo_dados` | Código/dados disponíveis | Select One |
| 36 | `limitacoes` | Limitações Reportadas | String |
| 37 | `lacuna` | Lacuna identificada pelos autores | String |
| 38 | `notas_revisor` | Notas do revisor | String |

## 5. Campos

Quando um campo tem a opção **Outro/Outra**, preencha o campo de texto seguinte somente se marcá-la.

### Bloco A — Identificação (1 a 4)

**1. ID do Registro (`row_id`)** · Integer. Copie a coluna `row_id` da planilha de triagem.

**2. Ano de Publicação** · String. Quatro dígitos, do ano da versão final. Se o metadado divergir (por exemplo, o metadado indica 2027, mas DOI e copyright indicam 2026), use o ano do DOI/copyright e anote.

**3. Tipo de Contribuição** · Select One

- **Novo modelo:** propõe arquitetura, pipeline ou técnica nova.
- **Estudo comparativo:** compara técnicas ou atributos existentes.
- **Análise estatística:** testa associações, sem foco em classificação.
- **Plataforma-sistema:** produto ou sistema completo (por exemplo, app com TinyML).
- **Outro.**

Decida pelo que o próprio artigo declara como contribuição principal (*we propose*, *we compare*, *we investigate*).

**4. Outra Contribuição** · String. Só se marcou Outro no campo 3.

### Bloco B — Uso do PADS (5 a 13)

**5. Papel do PADS** · Select One

- **Principal:** o PADS é a base de treino e avaliação.
- **Validação externa-generalização:** o modelo foi desenvolvido em outra base e testado no PADS.
- **Análise suplementar:** o PADS entra numa análise secundária.

**6. Datasets** · Select Many. **PADS**, **Outro público**, **Privado-próprio**. Marque **todas as bases usadas em experimentos**, e não as apenas citadas. Sem PADS marcado, o estudo não deveria estar entre os aceitos: sinalize.

**7. Outros Datasets** · String. Nome das bases além do PADS (obrigatório se marcou *Outro público* ou *Privado-próprio*).

**8. Modalidade do PADS** · Select Many

- **Série temporal (IMU):** sinais dos sensores.
- **Questionário (PDNMS):** os 30 itens não motores.
- **Metadados demográficos-clínicos:** idade, sexo, lateralidade etc.

Em estudo só com questionário, marque apenas *Questionário (PDNMS)* (e *Metadados*, se usados).

**9. Tarefas do PADS** · Select One

- **Todas:** o estudo usa o conjunto completo de tarefas.
- **Subconjunto:** algumas tarefas.
- **Tarefa única:** apenas uma.
- **Não reportado.**
- **Não se aplica:** estudo só com questionário.

Se o modelo é treinado **separadamente por tarefa**, marque conforme o conjunto analisado e anote "modelo por tarefa".

**10. Quais tarefas PADs** · String. Nomes como no artigo, separados por ponto e vírgula (por exemplo, *Finger-to-Finger; Finger-to-Nose*). Se for "todas", escreva "todas" e o número que o artigo informar. Vazio se o campo 9 = Não se aplica.

**11. Sensores** · Select Many. **Acelerômetro**, **Giroscópio**, **Outro**. Preencha só se usar série temporal; em estudos só de questionário, deixe vazio.

**12. Outros Sensores** · String. Só se marcou Outro no campo 11.

**13. Punho(s) usado(s)** · Select One. **Esquerdo**, **Direito**, **Ambos**, **Não reportado**, **Não se aplica**. "Ambos" inclui sinais concatenados e modelos por punho comparados; descreva na observação.

### Bloco C — Amostra e cenários (14 a 17)

**14. N° de participantes** · Integer. Número de **pessoas** efetivamente usadas no experimento, e não o total do PADS. Ex.: 355 (PD×HC), 390 (PD×DD), 469 (completo) ou outro N descrito no artigo. Se o artigo reporta só sessões, gravações ou janelas, deixe vazio e registre esses números na observação.

**15. N° por classe: PD / HC / DD** · String. Formato fixo, em número de pessoas: `PD=276; HC=79; DD=114`. Use 0 para a classe que não entra no cenário (por exemplo, `DD=0` em PD×HC). Quando 14 e 15 estão preenchidos, a **soma por classe deve ser igual ao campo 14**.

**16. Cenários de classificação** · Select Many

- **PD×HC:** Parkinson vs. saudáveis (binário).
- **PD×DD:** Parkinson vs. outros distúrbios do movimento (binário, clinicamente o mais difícil).
- **DD×HC:** outros distúrbios vs. saudáveis (binário).
- **3 classes (Mult-Class):** PD, DD e HC ao mesmo tempo. *(Grafia do Parsifal: sem o "i".)*
- **Outro.**

**Atenção:** cenários diferentes não são comparáveis diretamente. O acaso é 50% no binário e ~33% em 3 classes, e as classes são desbalanceadas (276/79/114).

**17. Outro Cenários de classificação** · String. Só se marcou Outro no campo 16.

### Bloco D — Método (18 a 23)

**18. Representação de entrada** · Select Many

- **Série bruta:** o modelo recebe amostras do sinal (típico de deep learning).
- **Atributos manuais (handcrafted):** estatísticas, energia, atributos derivados de FFT (tabela de atributos por participante).
- **Tempo-frequência (espectrograma, wavelet):** o modelo recebe espectrograma, wavelet ou decomposição por bandas como entrada.
- **Outro.**

Se a FFT é usada só para **calcular atributos tabulares**, marque **Atributos manuais**.

**19. Outra Representação de entrada** · String. Só se marcou Outro no campo 18.

**20. Família do Algoritmo** · Select Many

- **Classical ML:** SVM, regressão logística, Random Forest, Extra Trees, XGBoost, LightGBM, CatBoost.
- **Deep Learning:** CNN, LSTM, Transformer, CNN-LSTM e outras arquiteturas neurais, inclusive combinadas.
- **Hybrid-Ensemble:** combina ML clássico com DL, ou faz *stacking*/votação entre modelos de famílias diferentes.
- **Generativo-augmentation:** GAN e afins, para sintetizar dados.
- **Auto-supervisionado.**
- **Outro.**

**21. Outra Família do Algoritmo** · String. Só se marcou Outro no campo 20.

**22. Espeçificação do Algoritmo** · String. Nomes dos modelos como no artigo, separados por ponto e vírgula (por exemplo, *SVM; Random Forest; XGBoost*). *(Grafia do Parsifal.)*

**23. Balanceamento/augmentation** · Select One. **Nenhum**, **SMOTE-oversampling**, **Dados sintéticos (GAN)**, **Outro**, **Não reportado**, **Não se aplica**. Se houver mais de um, marque o principal e anote o resto.

### Bloco E — Validação (24 a 30) — o mais importante para a sua tese

Este bloco mede o **risco de vazamento de dados (*data leakage*)**: informação do teste "escapando" para o treino, o que infla os resultados. No PADS o risco principal é o **mesmo participante aparecer no treino e no teste**, porque cada pessoa gera muitos registros.

**24. Estratégia de Validação** · Select Many

- **Hold-out:** divisão única (por exemplo, 80/20 ou 70/30).
- **k-fold CV:** validação cruzada em k partes.
- **CV aninhada:** laço interno para hiperparâmetros e externo para avaliar.
- **Leave-one-subject-out:** cada participante é o teste uma vez.
- **Outra** e **Não reportado** (esta é exclusiva: se marcada, não marque as demais).

**25. Outra Estratégia de Validação** · String. Só se marcou Outra no campo 24.

**26. Unidade de particionamento (partitioning unit)** · Select One. O que foi **sorteado** para ir ao treino ou ao teste:

- **Participante:** todos os dados de uma pessoa ficam do mesmo lado.
- **Gravação-sessão:** cada gravação (tarefa, sessão ou punho) é sorteada isoladamente.
- **Janela/segmento:** o sinal é fatiado e cada janela é sorteada.
- **Misto:** níveis diferentes em etapas diferentes (por exemplo, por participante no teste final e por janela no ajuste de hiperparâmetros); descreva na observação.
- **Não reportado:** o artigo deveria informar, mas não informa.
- **Não se aplica:** estudo sem avaliação preditiva (análise estatística).

**Como decidir:** procure *subject-wise*, *patient-wise*, *group k-fold*, *StratifiedGroupKFold*, *leave-one-subject-out* (→ Participante). Procure *random split*, *shuffle*, janelas sorteadas (→ Gravação-sessão ou Janela/segmento). "Stratified" e "k-fold" sozinhos **não** provam separação por participante.

**27. Separação por participante (subject-level separation)** · Select One. Existe garantia de que **nenhum participante aparece ao mesmo tempo no treino e no teste?**

- **Sim – explícita:** o texto declara (*subject-wise*, *patient-wise*, *subject-independent*, *group k-fold*, *leave-one-subject-out*, divisão por paciente).
- **Sim – inferida:** o texto não declara, mas o **desenho garante** (por exemplo, um único registro por participante, explicado no texto). Exige `status: "inferido"` no YAML e entra nos pontos de revisão humana.
- **Parcial:** só parte dos experimentos/modelos/dobras separa por participante (descreva qual na observação).
- **Pouco claro:** divisão não descrita ou ambígua.
- **Não:** há participantes nos dois lados.
- **Não se aplica:** estudo sem avaliação preditiva.

Relação com o campo 26: Participante → `Sim – explícita` ou `Sim – inferida`; Gravação-sessão ou Janela/segmento → `Não`; Misto → normalmente `Parcial`.

**28. Balanceamento** · Select One. É o **momento** em que o balanceamento foi aplicado:

- **Só no treino:** aplicado depois da divisão, apenas ao conjunto de treino.
- **Antes do split:** aplicado a todos os dados antes de dividir (gera vazamento).
- **Não reportado:** foi usado, mas o artigo não diz quando.
- **Não se aplica:** balanceamento não usado (campo 23 = Nenhum ou Não se aplica).

**29. Detalhes do balanceamento (Caso Aplicado)** · String. Técnica e parâmetros, se aplicado (por exemplo, "SMOTE, k=5, só classe HC"). Vazio se o campo 23 = Nenhum ou Não se aplica.

**30. Validação externa do Modelo** · Boolean. **Sim** quando o modelo foi testado em **dados de outra fonte** (outro dataset, outro grupo de participantes ou outro dispositivo). Dividir o próprio PADS em treino e teste, mesmo por participante, **não** conta.

### Bloco F — Resultados (31 a 34)

**31. Métricas de avaliação** · Select Many. AUC, Accuracy, **Balanced accuracy**, F1, MCC, Precision, Sensitivity, Specificity, Outra. Marque só o que o artigo reporta. A *balanced accuracy* é central aqui, porque as classes do PADS são desbalanceadas; anote na observação se o F1 é macro ou ponderado.

**32. Outras Métricas de avaliação** · String. Só se marcou Outra no campo 31.

**33. Melhor resultado (Evaluation Values)** · String. Formato fixo: **cenário; modelo; métrica; valor**. Exemplo: *DD×HC; Extra Trees; Balanced accuracy; 82,48%*.

- Use o valor do **conjunto de teste**, não de treino ou validação.
- Em caso de divergência entre resumo e tabela, use a tabela e anote.
- Em estudos com outras bases, extraia só o resultado no PADS.
- Se houver média ± desvio, inclua.
- Não arredonde nem recalcule.

**34. Demais valores** · String. Outros resultados relevantes no mesmo formato, separados por ` | ` (barra vertical com espaços) no YAML; ao digitar no Parsifal, troque por quebra de linha.

### Bloco G — Síntese (35 a 38)

**35. Código/dados disponíveis** · Select One. **Código**, **Dados**, **Ambos**, **Nenhum**, **Não reportado**. Como o PADS é público, "Dados" vale só para dados derivados ou próprios (por exemplo, atributos extraídos). Procure *Data/Code availability* e links de repositório.

**36. Limitações Reportadas** · String. Resuma as limitações **declaradas pelos autores** (amostra, generalização, falta de validação externa etc.), com a seção de origem.

**37. Lacuna identificada pelos autores** · String. O que os autores indicam como problema em aberto ou trabalho futuro. Alimenta a síntese de lacunas.

**38. Notas do revisor** · String. **Campo do revisor (você).** A IA deixa `null` e registra suas observações no campo `observacao` de cada item do YAML (a planilha as reúne em `aux_observacoes_ia`). Use as Notas para: dúvidas, exceções, evidência (seção/página), "só resumo", modelo por tarefa, número de sessões ou janelas, divergências entre resumo e tabela e o valor de `aux_preproc_apenas_treino`.

## 6. Campos auxiliares e derivados (fora do Parsifal)

Não há campo no Parsifal para estes itens; ficam no YAML (`derivados`) e na planilha.

**`aux_preproc_apenas_treino`** · Sim | Não | Não reportado. Normalização, seleção de atributos (ANOVA, LASSO) e ajuste de hiperparâmetros foram feitos **somente com o conjunto de treino**? Se qualquer um deles usou todos os dados antes da divisão, marque Não. Em estudo sem avaliação preditiva, use `null`.

**`risco_vazamento`** · calcule, nesta ordem de decisão:

- **Não se aplica:** campo 26 = Não se aplica (sem avaliação preditiva).
- **Alto:** campo 26 = Gravação-sessão ou Janela/segmento; ou campo 27 = Não; ou campo 28 = Antes do split; ou `aux_preproc_apenas_treino` = Não.
- **Baixo:** campo 26 = Participante **e** campo 27 = Sim – explícita ou Sim – inferida **e** campo 28 = Só no treino ou Não se aplica **e** `aux_preproc_apenas_treino` = Sim.
- **Moderado:** campo 26 = Misto; ou campo 27 = Parcial; ou campo 27 = Sim (qualquer) com campo 28 ou `aux_preproc_apenas_treino` = Não reportado.
- **Indeterminado:** demais casos (por exemplo, campo 26 ou 27 = Pouco claro/Não reportado).

Sinais de alerta: desempenho muito alto (por exemplo, acurácia de 100%) e artigos que não descrevem a divisão.

## 7. Regras de coerência (confira ao terminar cada artigo)

- Modalidade só Questionário (8) → Sensores (11) vazio; Tarefas (9) e Punho (13) = Não se aplica; Quais tarefas (10) vazio; Representação (18) vazia.
- Cenários (16) com `3 classes (Mult-Class)` → Nº por classe (15) com PD, HC e DD maiores que 0.
- Soma de PD+HC+DD (15) = N° de participantes (14), quando ambos estão preenchidos.
- Campo 26 = Participante → campo 27 = Sim – explícita ou Sim – inferida.
- Campo 26 = Gravação-sessão ou Janela/segmento → campo 27 = Não e risco = Alto.
- Campo 24 contém Leave-one-subject-out → campo 26 = Participante e campo 27 = Sim.
- Campo 26 = Não se aplica → campo 27 = Não se aplica, campo 28 = Não se aplica, risco = Não se aplica e campo 24 = Não reportado (explique na observação).
- Campo 23 = Nenhum ou Não se aplica → campo 28 = Não se aplica e campo 29 vazio.
- Campo 23 = SMOTE-oversampling, Dados sintéticos (GAN) ou Outro → campo 28 ≠ Não se aplica e campo 29 preenchido.
- Campo 30 = Sim e campo 5 = Principal → explique na observação. Campo 5 = Validação externa-generalização → campo 30 normalmente = Sim.
- Campo 6 sem PADS → o estudo não deveria estar entre os aceitos; sinalize.
- Cada Outro/Outra marcado ↔ campo de texto correspondente preenchido (3→4, 6→7, 11→12, 16→17, 18→19, 20→21, 24→25, 31→32).
- Campo 24 com **Não reportado**: não marque outras opções.
- Campo 9 ≠ Não se aplica → campo 10 preenchido; campo 9 = Não se aplica → campo 10 vazio.

## 8. Quality Assessment (QA1 a QA5)

O QA mede a **qualidade metodológica e de relato** de cada estudo. Ele é calculado **depois** do preenchimento do formulário, a partir dos campos finais, sem reler o artigo. Pontuação por pergunta: **Yes = 1,0 · Partially = 0,5 · No = 0,0 · N/A = fora do cálculo**. Regra geral: informação **Não reportada** ou **Pouco clara** conta como não atendida.

| Pergunta | Campos | Yes (1,0) | Partially (0,5) | No (0,0) |
| --- | --- | --- | --- | --- |
| **QA1.** A tarefa de classificação está claramente definida? | 16, 15 | Cenário explícito e grupos do PADS claros | Cenário citado, com dúvida sobre os grupos (por exemplo, DD excluído ou não) | Tarefa não definida |
| **QA2.** O recorte de dados do PADS está descrito? | 8, 9, 11, 13, 14 | Todos os itens aplicáveis informados | Pelo menos metade dos itens | Menos da metade |
| **QA3.** A validação evita vazamento entre participantes? | 26 a 28 e `aux_preproc_apenas_treino` | Risco de vazamento Baixo | Risco Moderado | Risco Alto ou Indeterminado |
| **QA4.** As métricas são adequadas ao desbalanceamento das classes? | 31 | Pelo menos duas métricas robustas | Uma métrica robusta, ou F1 sem indicar macro/ponderado | Apenas Accuracy ou nenhuma |
| **QA5.** Há código ou detalhes suficientes para replicar o estudo? | 35, 22, 29 | Código disponível e modelos, hiperparâmetros e pré-processamento descritos | Apenas um dos dois | Nenhum |

### Como decidir cada pergunta

- **QA1:** `N/A` se o estudo não tem tarefa de classificação (campo 16 vazio).
- **QA2:** os itens são modalidade (8), tarefas (9), sensores (11), punho (13) e N de participantes (14). Conte como informado o item que não está em "Não reportado" e, no caso do N, que está preenchido. Em estudo só com questionário, avalie apenas modalidade e N.
- **QA3:** use o `risco_vazamento` calculado na seção 6. Se o risco é **Não se aplica**, QA3 = `N/A`. Exemplo: campo 26 = Participante, 27 = Sim – explícita, 28 = Só no treino e `aux_preproc_apenas_treino` = Sim → risco Baixo → **Yes**. Se `aux_preproc_apenas_treino` for Não reportado → risco Moderado → **Partially**.
- **QA4:** métricas robustas são *Balanced accuracy*, MCC, F1 (indicado como macro), AUC e o par *Sensitivity* + *Specificity* (conta como uma). Isso importa porque as classes do PADS são desbalanceadas (276/79/114). `N/A` se não há avaliação preditiva.
- **QA5:** o formulário não tem campo para hiperparâmetros; confira-os no texto e registre na observação. Em estudo estatístico, leia "modelos" como "métodos/testes estatísticos".
- **QA3 e QA5** dependem do texto completo e são os que mais merecem revisão humana.

### Nota total e uso

- **nota_qa** = soma das perguntas aplicáveis; **nota_qa_max** = número de perguntas aplicáveis (5 quando não há N/A); **nota_qa_pct** = nota_qa ÷ nota_qa_max.
- **Faixas provisórias** (defina no protocolo antes de aplicar): **Alta** ≥ 80% (4,0 a 5,0 de 5); **Média** de 50% a 79% (2,5 a 3,5 de 5); **Baixa** < 50% (0 a 2,0 de 5).
- **Uso sugerido:** não excluir estudos (o corpus tem poucos artigos); usar a nota para caracterizar a qualidade e fazer uma análise de sensibilidade (todos vs. só os de faixa Alta).
- **No Parsifal:** registre a resposta de cada pergunta na etapa 4 (Quality Assessment). Se o Parsifal do seu projeto não permitir a resposta N/A com peso 0 (confira em Planning → Quality Assessment), a nota oficial é a da planilha (`nota_qa_pct`).
- **Na planilha (Excel em português), se quiser recalcular à mão:** `=SE(AW2>=0,8;"Alta";SE(AW2>=0,5;"Média";"Baixa"))`, com AW2 = `nota_qa_pct` (coluna 49 da aba `extracao`). O script da seção 9 já calcula essa faixa.

## 9. Organização dos dados (pastas, YAML e planilha)

**Princípio:** o **YAML por artigo é a fonte da verdade**; a planilha é **derivada** (gerada pelo script, nunca editada à mão); o **Parsifal** é o destino final (digitação a partir da aba `extracao`).

```text
extracao_pads/
├── pdfs/              # opcional: cópia local do PDF, nomeada {row_id}.pdf (a IA localiza o texto pela Key in Zotero)
├── raw/               # saída da IA (modo EXTRAÇÃO): {row_id}.yaml
├── auditoria/         # saída da IA (modo AUDITORIA): {row_id}.yaml
├── consolidar.py      # script da seção 3 do arquivo de prompt
└── extracao.xlsx      # gerado pelo script
```

**Fluxo por artigo:**

1. Uma conversa por artigo; informe `row_id`, *Key in Zotero* e status de triagem (ou anexe o PDF) e rode o prompt em modo EXTRAÇÃO. **Confira `meta.titulo`:** o título extraído deve ser o do artigo esperado; se não for, a IA abriu o documento errado e o YAML deve ser descartado.
2. Salve o bloco YAML em `raw/{row_id}.yaml` (UTF-8).
3. Rode `python consolidar.py` e leia a aba `alertas` (rótulo fora do Parsifal, campo ausente, Outro sem texto, soma por classe, nota QA divergente, elegibilidade diferente de `USA PADS`).
4. **Auditoria:** em outra conversa, rode o prompt em modo AUDITORIA, colando o YAML de `raw/`, e salve a saída em `auditoria/{row_id}.yaml`. Rode o script de novo: a aba `auditoria` lista os campos em que a IA discorda ou não consegue verificar.
5. Revise, no mínimo, as divergências da aba `auditoria`, os campos 24 a 30 e 33, todo `confianca: "baixa"` e todo `status: "inferido"` (aba `revisao`), sempre no artigo original.
6. **Para corrigir um valor, edite o YAML de `raw/`** (campo `valor`) e escreva em `auditoria` algo como `"CORRIGIDO pelo revisor (valor da IA: X)"`. Rode o script de novo.
7. Digite no Parsifal a partir da aba `extracao` (colunas 1 a 38, com os nomes do Parsifal). Select Many aparece como `A; B`; Boolean como `Sim`/`Não`.

### Escopo, fonte e rastreabilidade

- **Escopo e fonte:** a IA recebe a *Key in Zotero* de cada artigo e extrai direto do texto original. Extrair os artigos com status de triagem **Aceito**, **Aceito, mas com Ressalvas** e **Aceito, mas com Ressalvas, não confiável**. Informe o status (e a ressalva, se houver) na ENTRADA do prompt; ele vai para `meta.status_triagem` e para a coluna `aux_status_triagem`, e permite comparar os resultados por status (análise de sensibilidade). Nos dois status com ressalva, a IA confirma primeiro o ponto da ressalva.
- **Rastreabilidade:** a IA registra em `meta` o modelo usado (`ia_modelo`) e a versão do prompt (`prompt_versao`); mantenha esses campos preenchidos em todos os YAML.
- **Mesmo prompt para todos:** use a mesma `prompt_versao` nos 29 artigos; se ajustar o prompt no meio do processo, atualize `prompt_versao` e reexecute apenas os artigos afetados.

**Abas de `extracao.xlsx` (todas geradas pelo script):**

| Aba | Conteúdo |
| --- | --- |
| `extracao` | 1 linha por artigo; colunas 1 a 38 com os nomes exatos do Parsifal, depois `aux_preproc_apenas_treino`, `aux_observacoes_ia`, `risco_vazamento`, `QA1` a `QA5`, `nota_qa`, `nota_qa_max`, `nota_qa_pct`, `faixa_qa`, `aux_elegibilidade`, `aux_qualidade_texto`, `aux_status_triagem`, `aux_ressalva_triagem`, `aux_zotero_key`, `aux_titulo`. |
| `evidencias` | Formato longo: `row_id`, `id`, `chave`, `valor`, `status`, `confianca`, `evidencia`, `auditoria`, `observacao`. |
| `qa` | Uma linha por artigo × pergunta: `resposta`, `nota`, `campos`, `justificativa`. |
| `revisao` | Pontos para revisão humana por artigo (coluna `resolvido` para você marcar). |
| `auditoria` | Só existe se houver arquivos em `auditoria/`: campos em que a auditoria da IA discorda ou não consegue verificar, com `valor_extraido`, `valor_auditado`, `evidencia`, `observacao` e coluna `resolvido` para você marcar. |
| `alertas` | Problemas de validação do YAML. |
| `dicionario` | Campos, chaves, tipos e opções válidas. |

**Convenções de valor** (obrigatórias no YAML; detalhes no arquivo de prompt): Select One = texto; Select Many = lista; Integer = número; Boolean = `true`/`false`; vazio = `null` (nunca `""`, `-` ou `N/A`); todo texto entre aspas duplas (evita que `Não`, `Yes`/`No` e `:` quebrem o YAML).

## 10. Glossário

- **PD:** doença de Parkinson. **HC/CO:** controle saudável. **DD:** diagnóstico diferencial (outros distúrbios do movimento).
- **IMU:** unidade de medida inercial (acelerômetro + giroscópio).
- **PDNMS:** questionário de 30 sintomas não motores do PADS.
- **Vazamento de dados (*data leakage*):** informação do teste que "escapa" para o treino e infla o desempenho.
- **k-fold:** validação cruzada em k partes. **Hold-out:** divisão única treino/teste.
- **CV aninhada:** validação com laço interno (hiperparâmetros) e externo (avaliação).
- **LOSO:** *leave-one-subject-out*, um participante por vez como teste.
- **SMOTE / up-sampling:** técnicas para balancear classes criando ou repetindo amostras da classe menor.
- **Acurácia balanceada:** média da sensibilidade de cada classe; robusta a desbalanceamento.
- **F1 macro:** média do F1 de cada classe, sem ponderar pelo tamanho.
- **MCC:** coeficiente de correlação de Matthews, métrica única para classes desbalanceadas.
- **XAI:** inteligência artificial explicável. **SSL:** aprendizado auto-supervisionado. **GAN:** rede generativa adversarial.

## 11. Checklist final por artigo

- [ ] Li Métodos e a tabela de Resultados (não só o resumo).
- [ ] Extraí apenas o recorte do PADS (e uma única versão do estudo).
- [ ] Preenchi N° de participantes e N° por classe em **pessoas** (sessões e janelas nas observações) e a soma confere.
- [ ] Identifiquei a unidade de particionamento (26), a separação por participante (27) e o momento do balanceamento (28).
- [ ] Verifiquei se normalização, seleção de atributos e hiperparâmetros ficaram só no treino (`aux_preproc_apenas_treino`).
- [ ] Calculei o risco de vazamento.
- [ ] Pontuei QA1 a QA5 a partir dos campos finais (com N/A quando couber) e conferi a nota.
- [ ] Registrei seção/página das dúvidas.
- [ ] Conferi as regras de coerência da seção 7 e a aba `alertas`.
- [ ] Salvei o YAML em `raw/{row_id}.yaml` e rodei o script.
