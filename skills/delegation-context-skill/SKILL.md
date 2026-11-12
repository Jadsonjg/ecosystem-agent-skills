---
name: delegation-context-skill
description: "Padroniza delegações entre coordenadores e executores, separando contexto operacional do briefing executável, calibrando o nível de raciocínio necessário e interrompendo delegações prematuras ou inseguras. Usar ao preparar delegação formal, comando, briefing ou handoff para Work, outro agente, outro chat executor, executor técnico ou humano, ferramenta, automação ou sistema multiagente; exemplos: “me dê o prompt para o Work”, “mande isso para o executor”, “crie o briefing”, “prepare o comando para outro chat”, “delegue essa tarefa”, “faça o handoff”, “me dê a instrução para o agente” ou equivalentes. Não acionar apenas por existir uma tarefa normal no chat, quando o próprio chat executar diretamente ou quando o usuário pedir somente resposta, opinião ou explicação."
---

# Delegation Context Skill

Aplicar a **Delegation Context Skill** às delegações formais, preservando as regras abaixo.

Esta skill se aplica sempre que você estiver atuando como coordenador, gestor, planejador, supervisor ou responsável por preparar uma tarefa que será executada por outro chat, agente, Work, ferramenta, automação, sistema multiagente ou executor humano.

Seu objetivo é melhorar a qualidade da delegação sem transformar o operador em transportador manual de contexto.

---

## 1. REGRA CENTRAL

Antes de fornecer qualquer prompt, comando ou briefing destinado a outro executor, apresente primeiro uma seção chamada:

### Informações adicionais

Depois apresente:

### Comando / Briefing

A distinção é obrigatória:

**INFORMAÇÕES ADICIONAIS = o operador entende a delegação.**

**COMANDO / BRIEFING = o executor entende como executar.**

Não misture essas duas funções.

---

## 2. INFORMAÇÕES ADICIONAIS

Começar SEMPRE pelos três campos obrigatórios, nesta ordem:

- **Ação:** descrição curta, executiva e objetiva do que será feito.
- **Resultado esperado:** descrição clara do que deve existir, estar concluído, configurado, analisado ou devolvido ao final.
- **Raciocínio recomendado:** um dos cinco níveis definidos na seção 4, acompanhado de justificativa curta e prática.

Manter os três campos mesmo em delegações simples. Não substituir a seção por “Informações adicionais: nenhuma”.

Incluir os campos abaixo SOMENTE quando forem realmente necessários:

- **Modelo recomendado**
- **Ferramentas / conectores**
- **Arquivos / documentos / pastas**
- **Dependências / pré-requisitos**
- **Permissões / acessos / ação humana**
- **Limitações conhecidas**
- **Cuidados para evitar execução incorreta**

Não tornar campos opcionais obrigatórios. Não preenchê-los apenas para completar uma estrutura.

Não repetir no bloco de Informações adicionais detalhes operacionais que estarão no briefing.

---

## 3. PRINCÍPIO DE NÃO DUPLICAÇÃO

A seção Informações adicionais NÃO é um segundo briefing.

Ela existe para responder rapidamente ao operador:

- O que será feito?
- O que devo esperar como resultado?
- Há algum recurso especial necessário?
- Preciso fornecer acesso, arquivo, autorização ou ação humana?
- Existe alguma limitação ou cuidado importante antes da execução?
- A tarefa exige um modelo ou esforço de raciocínio específico?

Tudo que pertence a passos de execução, critérios detalhados, contexto extenso, regras técnicas, formato de saída ou validações do trabalho deve ficar no **Comando / Briefing**.

---

## 4. MODELO E NÍVEL DE RACIOCÍNIO

Preencher SEMPRE **Raciocínio recomendado**. Usar somente estes cinco níveis, com esta grafia:

| Nível | Calibração |
| --- | --- |
| Low | Tarefas simples, determinísticas, leitura objetiva e pequenas alterações sem ambiguidade. |
| Medium | Execução técnica normal, dependências claras, comparações simples e critérios de revisão definidos. |
| High | Decisões técnicas com múltiplas evidências, debugging, trade-offs e gates de projeto. |
| Extra High | Problemas complexos, alto custo de erro, arquitetura delicada, investigação inconclusiva ou integração difícil de múltiplas fontes. |
| Maximum | Somente complexidade, ambiguidade ou risco realmente excepcionais. |

Usar o menor nível de raciocínio que preserve a qualidade necessária. Não selecionar um nível alto apenas porque o campo é obrigatório. Não criar, renomear ou substituir os cinco níveis. Dar justificativa curta e prática.

Exemplo: **Raciocínio recomendado:** Medium — a execução é técnica, mas o escopo e os critérios estão bem definidos.

Manter **Modelo recomendado** opcional. Incluí-lo somente quando a escolha afetar materialmente qualidade, confiabilidade, custo, tempo ou risco da execução, como em estratégia, auditorias, arquitetura de informação, planejamento técnico, análises financeiras complexas, comunicação com muitas restrições ou alto custo de retrabalho.

### Portabilidade entre plataformas

Diferenciar sempre entre:

**Recomendação semântica**

Exemplo: `Raciocínio recomendado: High — exige síntese de múltiplas evidências.`

Usar quando só for possível recomendar a configuração ao operador.

**Configuração acionável**

Usar somente se a plataforma, API ou ferramenta realmente oferecer um mecanismo para alterar a configuração. Quando disponível, utilizar o mecanismo nativo correspondente, sem inventar parâmetros ou equivalências entre plataformas.

Nunca afirmar que alterou modelo, modo ou nível de raciocínio sem controle real e sem efetivamente realizar essa alteração.

Não tratar atalhos de interface, comandos iniciados por `/`, nomes de modos ou seletores específicos de uma plataforma como universais.

Se não houver controle técnico disponível, apenas recomendar. Não transformar a recomendação de raciocínio ou modelo em permissão para executar uma ação.

---

## 5. AUTONOMIA PARA INTERROMPER ANTES DA DELEGAÇÃO

Antes de produzir a delegação final, avalie se prosseguir pode gerar erro, retrabalho, risco ou resultado inferior.

Interrompa antes da delegação quando identificar, por exemplo:

- premissa incorreta;
- dados insuficientes;
- conflito entre instruções ou fontes;
- ferramenta inadequada;
- ausência de arquivo essencial;
- dependência não resolvida;
- permissão necessária ainda não concedida;
- risco relevante, inclusive risco de segurança;
- escolha prematura de arquitetura;
- acesso necessário ainda ausente;
- alta probabilidade de retrabalho;
- briefing prematuro;
- executor inadequado para a tarefa;
- nível de raciocínio claramente insuficiente;
- decisão humana necessária antes da execução.

Tratar os itens acima como bloqueios quando forem relevantes para a execução; não criar impedimentos hipotéticos nem pedir novamente permissões já concedidas. Não produzir um briefing final como se estivesse tudo resolvido.

Nesses casos:

1. explique objetivamente o problema;
2. diga por que prosseguir naquele estado é inadequado;
3. proponha correção ou alternativa;
4. solicite decisão ou ação do operador quando necessário;
5. somente depois de resolver o bloqueio produza o briefing final.

Resolver correções dentro da autoridade e dos recursos disponíveis. Solicitar decisão humana apenas quando realmente necessária. Não tratar silêncio como decisão ou permissão.

Não transforme uma direção ruim em um prompt bem escrito.

---

## 6. ESCOLHA DO EXECUTOR

Não criar agentes adicionais, Works, novos chats, novas camadas, documentos intermediários ou processos extras sem justificativa concreta. Não fragmentar trabalho apenas para criar uma estrutura.

Um executor separado só deve ser recomendado quando houver justificativa real, como:

- especialização;
- recorrência;
- volume;
- complexidade;
- necessidade de continuidade;
- necessidade de ferramentas ou permissões específicas;
- benefício claro de separar planejamento de execução.

Quando um chat comum for suficiente, não recomende uma estrutura mais complexa sem necessidade.

---

## 7. COMANDO / BRIEFING

Depois das Informações adicionais, escreva o briefing completo e pronto para execução.

O briefing deve conter apenas o necessário para que o executor trabalhe corretamente, podendo incluir:

- objetivo;
- contexto;
- escopo;
- dados de entrada;
- passos de execução;
- critérios de qualidade;
- restrições;
- regras de decisão;
- pontos de parada;
- validações;
- entregáveis;
- formato de saída;
- tratamento de erros;
- comportamento em caso de dúvida.

O executor não deve precisar reconstruir informações essenciais a partir de mensagens dispersas.

Ao mesmo tempo, não infle o briefing com contexto irrelevante.

---

## 8. RELAÇÃO ENTRE OPERADOR, COORDENADOR E EXECUTOR

Considere três papéis distintos:

**Coordenador**
- pensa;
- decide direção;
- organiza;
- prioriza;
- escolhe executor;
- prepara a delegação;
- define gates;
- interrompe quando a direção estiver inadequada.

**Operador**
- autoriza decisões sensíveis;
- fornece acessos, arquivos ou permissões quando necessário;
- entende o que está sendo delegado;
- aprova quando houver decisão humana necessária.

**Executor**
- executa a tarefa dentro do briefing;
- não amplia autonomamente sua autoridade;
- não transforma exceções em regras;
- retorna resultado, bloqueio ou necessidade de decisão.

A skill deve reduzir a necessidade de o operador transportar manualmente contexto entre esses papéis.

---

## 9. FORMATO PADRÃO DE SAÍDA

Quando houver uma delegação válida, usar exatamente estes dois blocos principais, nesta ordem e sem renomeá-los:

### Informações adicionais

**Ação:** [descrição executiva]

**Resultado esperado:** [resultado final esperado]

**Raciocínio recomendado:** [Low, Medium, High, Extra High ou Maximum] — [justificativa curta e prática]

[Acrescentar campos opcionais somente quando necessários, conforme a seção 2.]

### Comando / Briefing

[Prompt completo pronto para o executor.]

Não deixar marcadores ou campos vazios na resposta final. Omitir campos opcionais sem utilidade.

Se houver um bloqueio relevante, aplicar primeiro a seção 5; não emitir esta estrutura como briefing final enquanto o bloqueio estiver sem resolução.

---

## 10. REGRA FINAL

A qualidade da delegação é mais importante do que preencher um template.

Use a estrutura para reduzir ambiguidade e retrabalho, não para criar burocracia.

Se uma informação não ajuda o operador a entender a delegação ou o executor a executar melhor, não a inclua.

Se houver um problema de direção, pare antes de delegar.

Se a delegação estiver correta, entregue o briefing pronto para uso.

---

## 11. FONTE E ADAPTAÇÃO NATIVA

Manter como fonte oficial o repositório https://github.com/Jadsonjg/ecosystem-agent-skills. Usar `skills/delegation-context-skill/SKILL.md` como especificação nativa canônica; `prompt-mestre.md` é sua exportação em Markdown para uso em outros chats e deve permanecer equivalente. Consolidar alterações primeiro nessa fonte e registrá-las no histórico de versões antes de atualizar a instalação nativa.

Esta versão 1.1.0 incorpora as determinações explícitas do usuário em 11/10/2026: três campos sempre obrigatórios; raciocínio separado do modelo opcional; cinco níveis e sua calibração; retirada da alternativa “Informações adicionais: nenhuma”; critérios de parada e anti-burocracia ampliados conforme esta especificação. A versão inicial 1.0.0 está preservada no histórico do repositório. Não reintroduzir regras antigas conflitantes ao consultar a fonte.

Não simplificar regras obrigatórias, remover critérios de parada, transformar recomendações em permissões, tornar campos opcionais obrigatórios, alterar os cinco níveis ou renomear os dois blocos principais.

Respeitar a autoridade e as instruções explícitas do usuário em futuras alterações. Não afirmar que a fonte oficial ou a instalação foi atualizada sem efetivamente salvar e verificar a respectiva alteração.

Se uma tarefa exigir consultar a fonte oficial e não for possível acessá-la, informar o impedimento e solicitar seu conteúdo; não reconstruir regras ausentes por suposição.
