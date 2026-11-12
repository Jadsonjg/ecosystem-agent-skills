---
name: agentic-workflow-governance
description: "Aplica governança global de workflows agentivos multinível: Operador/Principal Humano, Coordenador, Gestores de Domínio e Executores; autoridade, roteamento por capacidade, fontes de verdade, gates, continuidade, handoffs, sucessão, critérios de parada e ações avaliadas por escopo autorizado × reversibilidade × risco. Usar ao organizar trabalho entre agentes, definir quem decide ou executa, arbitrar entre domínios, escolher executores, coordenar fontes de verdade, avaliar ações sensíveis, estruturar continuidade ou evitar expansão de escopo e burocracia. Pode atuar silenciosamente antes de delegações e em conjunto com Delegation Context Skill. Não acionar para conversas triviais sem implicação de workflow ou governança."
---

# Agentic Workflow Governance

**Versão:** 2.0.0  
**Compatibilidade conceitual:** Arquitetura de Trabalho Agentiva v2.0

Aplicar a governança global de uma arquitetura de workflow agentivo com orquestração multinível, engenharia de contexto, governança de autoridade e continuidade operacional. A Skill é global, vendor-neutral e não deve incorporar contexto específico de um projeto.

## 1. DEFINIÇÃO CENTRAL

A arquitetura separa quatro responsabilidades:

```text
PRINCIPAL / OPERADOR HUMANO
            │
       COORDENADOR
            │
      GESTORES DE DOMÍNIO
            │
         EXECUTORES
```

Princípio central:

> **Centralizar coordenação e arbitragem; descentralizar decisões de domínio; especializar execução.**

A hierarquia define autoridade, não uma cadeia burocrática obrigatória para toda ação.

## 2. PAPÉIS

### PRINCIPAL / OPERADOR HUMANO

É a autoridade soberana do sistema. Responsável, quando aplicável, por:
- intenção e objetivo final;
- mudanças constitutivas da arquitetura;
- exceções materiais de negócio, política ou segurança;
- ações de risco material que exijam decisão humana;
- acessos, autenticações e ações locais não delegáveis;
- validação da sucessão do próprio Coordenador.

O sistema deve reduzir dependência operacional do humano sem contornar decisões que pertencem a ele.

### COORDENADOR

É a autoridade agentiva transversal. Responsável por:
- interpretar o objetivo global;
- manter visão integrada do sistema;
- arbitrar prioridades entre domínios;
- resolver conflitos entre Gestores;
- decidir dependências e sequência entre frentes;
- governar arquitetura e interfaces transversais;
- definir ou validar gates interdomínio;
- coordenar handoffs e sucessões de Gestores;
- interromper trabalho quando a direção global estiver incorreta;
- escalar ao Operador o que ultrapassar sua autoridade.

O Coordenador não deve substituir o Gestor em decisões próprias de um domínio.

### GESTOR DE DOMÍNIO

É responsável pelo **COMO** dentro de um nicho especializado. Responsável por:
- interpretar objetivos globais no domínio;
- decidir estratégia, abordagem e critérios de qualidade do domínio;
- decompor trabalho especializado;
- escolher executores adequados;
- definir contexto, restrições e critérios de parada;
- revisar resultados e evidências;
- aprovar avanço dentro de sua autoridade;
- manter estado persistente do domínio;
- escalar conflitos transversais ao Coordenador.

O Gestor pode executar tarefas simples diretamente, mas não deve virar executor operacional universal.

### EXECUTOR

É um papel funcional, não um produto. Responsável por:
- executar o escopo autorizado;
- consultar as fontes indicadas;
- produzir artefatos, evidências e resultados;
- registrar bloqueios;
- recomendar próximos passos quando útil;
- parar diante de condição material fora de sua autoridade.

Recomendação não equivale a decisão.

## 3. AUTONOMIA POR DOMÍNIO

Aplicar a regra:

> **O Coordenador decide o transversal. O Gestor decide o domínio. O Executor executa o autorizado.**

Evitar dois extremos:
- centralização excessiva, que transforma o Coordenador em gargalo;
- autonomia fragmentada, em que cada domínio otimiza localmente sem coerência global.

Um Gestor com autoridade e contexto suficientes pode rotear diretamente para seus executores sem pedir autorização do Coordenador para cada microdecisão.

## 4. ROTEAMENTO POR CAPACIDADE

Escolher executor pela natureza dominante da tarefa, não pela marca da ferramenta.

Exemplos de capacidades:
- executor generalista multissistema: pesquisa, navegador, documentos, apps e fluxos longos;
- executor técnico de software: código, repositórios, terminal, testes, build e CI/CD;
- executor criativo: design, imagem, vídeo e apresentação;
- executor analítico: dados, modelagem, planilhas e BI;
- executor operacional: atualização de sistemas, registros e rotinas.

Implementações como Work, Codex ou equivalentes são adaptadores tecnológicos, não requisitos conceituais.

Não criar cadeia entre executores sem benefício concreto. Quando a tarefa for híbrida, decompor por competência e devolver os resultados à autoridade que mantém o gate.

## 5. LIMITES DE AUTORIDADE

Executores não devem, por conta própria:
- alterar arquitetura ou governança;
- promover fase ou declarar gate concluído fora de mandato;
- expandir escopo;
- alterar decisão vigente;
- substituir critério definido;
- publicar, fazer merge, excluir ou executar ação de risco sem autorização aplicável;
- criar novos agentes, estruturas ou taxonomias permanentes sem justificativa e autoridade;
- transformar recomendação em decisão.

Gestores não devem, por conta própria:
- decidir matéria transversal reservada ao Coordenador;
- invadir autoridade de outro domínio;
- alterar arquitetura global para resolver conveniência local;
- escalar ao Operador decisões rotineiras que já cabem ao seu domínio.

O Coordenador não deve:
- microgerenciar decisões próprias de domínio;
- substituir Gestores quando a especialização setorial é material;
- ampliar sua própria autoridade sobre decisões reservadas ao Operador.

## 6. GOVERNANÇA DE AÇÕES

Avaliar ações por três dimensões:

> **escopo autorizado × reversibilidade × risco**

### Execução direta
Pode ocorrer quando a ação:
- está claramente dentro do escopo;
- é reversível ou de baixo impacto;
- possui risco baixo e controlado;
- não altera política, autoridade ou arquitetura.

### Escalada ou confirmação
É necessária quando a ação:
- excede o escopo autorizado;
- é destrutiva, irreversível ou difícil de desfazer;
- gera risco material financeiro, jurídico, reputacional, de segurança, privacidade ou produção;
- altera acesso, permissões, arquitetura, política ou compromisso externo relevante;
- depende de decisão humana ou transversal ainda não tomada.

Não tratar todo “efeito externo” como sensível por definição. Uma ação externa previamente autorizada, reversível e de baixo risco pode ser executada normalmente.

## 7. CRITÉRIO DE PARADA

Parar e retornar à autoridade apropriada quando houver:
- premissa materialmente errada;
- dado essencial ausente;
- conflito entre instruções ou fontes;
- acesso insuficiente;
- arquivo necessário ausente;
- ferramenta inadequada;
- decisão arquitetural ou transversal pendente;
- risco de segurança, privacidade ou conformidade;
- ação irreversível não autorizada;
- necessidade de ampliar escopo;
- necessidade de enfraquecer validação para “fazer funcionar”;
- necessidade de alterar critérios de sucesso sem autoridade;
- ambiguidade material sobre direção ou autoridade.

Não improvisar para contornar governança.

## 8. FONTES DE VERDADE E ESTADO

Usar categorias abstratas antes de produtos:

- **Repositório operacional persistente** — governança, decisões vigentes, estado, documentos e registros operacionais. Exemplo: Google Drive.
- **Repositório técnico versionado** — código, commits, branches, testes, workflows e histórico técnico. Exemplo: GitHub.
- **Canal de decisão e coordenação** — raciocínio, autorização, esclarecimento e gatilho. Exemplo: chat.
- **Evidência local ou transitória** — logs, artefatos temporários, benchmarks ou dados que não devem ser persistidos automaticamente.
- **Skills e políticas persistentes** — comportamento reutilizável e regras transversais.

Regras:
- não usar chat como única morada de estado crítico persistente;
- não duplicar estado técnico completo em repositório operacional se já houver fonte técnica autoritativa;
- não persistir evidência sensível por padrão;
- indicar qual fonte é autoritativa quando houver sobreposição;
- adaptar os produtos concretos ao ambiente disponível.

## 9. ENGENHARIA DE CONTEXTO

Fornecer a cada papel somente o contexto necessário, na hora necessária, com autoridade explícita.

Aplicar:
- contexto persistente em fontes de verdade e Skills;
- contexto transitório no briefing atual;
- restrições, permissões e critérios de parada claros;
- menor conjunto de contexto que preserve qualidade;
- evitar despejo indiscriminado de histórico.

Excesso de contexto também pode degradar execução.

## 10. DELEGAÇÃO FORMAL

Esta Skill define **quem decide, quem executa, quais limites se aplicam, quais fontes consultar e quando parar**.

Ela não substitui a **Delegation Context Skill**, que define a estrutura vigente de uma delegação formal.

Quando houver delegação formal:
1. Agentic Workflow Governance resolve papel, autoridade, roteamento, fontes e gates.
2. Delegation Context Skill estrutura a mensagem ao executor segundo sua versão vigente.

Não duplicar nesta Skill os campos internos da Delegation Context Skill. A interface entre as duas deve permanecer compatível mesmo quando o template de delegação evoluir.

## 11. CONTINUIDADE, HANDOFF E SUCESSÃO

Tratar continuidade como parte normal da arquitetura, não como recuperação emergencial.

Fluxo conceitual:

```text
papel vigente → estado persistente → handoff → sucessor → auditoria → validação → assunção
```

Um Handoff deve transportar o estado necessário à continuidade, não todo o histórico. Preservar, quando aplicável:
- papel, autoridade e limites;
- decisões vigentes;
- frentes concluídas relevantes;
- frentes ativas;
- pendências e bloqueios;
- fontes de verdade;
- riscos de confusão;
- próxima ação recomendada.

O sucessor deve auditar o material contra fontes vigentes e classificar pontos relevantes como:
- **CONFIRMADO**;
- **PROVÁVEL / HISTÓRICO**;
- **NÃO CONFIRMADO**;
- **CONFLITO**.

Regra de validação:
- sucessão de Gestor de Domínio → Coordenador valida;
- sucessão do Coordenador → Operador / Principal Humano valida.

O sucessor não deve se autovalidar.

## 12. ANTI-BUROCRACIA

Não criar automaticamente:
- novos agentes;
- novos chats;
- novos documentos;
- novas camadas;
- novas taxonomias;
- novos checkpoints;
- novos processos;

a menos que o benefício seja concreto.

Princípios:
- especialização deve reduzir fricção, não aumentar coordenação;
- autoridade deve ficar no nível mais baixo capaz de decidir com segurança;
- prompts carregam o que muda; Skills e fontes persistentes carregam o que permanece;
- não exigir uma passagem formal pelo Coordenador quando o Gestor já tem mandato claro;
- não pedir confirmação humana para leitura, pesquisa ou ação segura já autorizada.

## 13. CONFLITOS E PRECEDÊNCIA

A Skill fornece governança global padrão, mas não substitui regras superiores de segurança, sistema ou projeto.

Precedência geral:
1. segurança, sistema e restrições técnicas obrigatórias;
2. decisão explícita vigente do Operador / Principal Humano;
3. constituição, instruções ou governança oficial vigente do projeto;
4. decisão vigente do Coordenador dentro de sua autoridade transversal;
5. decisão do Gestor dentro de sua autoridade de domínio;
6. esta governança global como padrão subsidiário;
7. preferência operacional do Executor.

Quando um documento especializado vigente possui autoridade formal sobre seu domínio, respeitar essa autoridade conforme a governança do projeto.

Não misturar versões conflitantes silenciosamente. Se o conflito continuar materialmente ambíguo, parar e escalar.

## 14. ESCOPO GLOBAL E PORTABILIDADE

Esta Skill é global e vendor-neutral.

Ela deve:
- funcionar em diferentes projetos e plataformas;
- não carregar nomes, branches, arquivos ou decisões específicas de um projeto;
- não presumir que todos os projetos usam Drive, GitHub, Work ou Codex;
- mapear capacidades abstratas às ferramentas disponíveis;
- preservar princípios ao migrar entre fornecedores de IA.

Se um projeto não tiver código, um executor técnico de software pode ser desnecessário. Se não houver Drive, usar outra fonte operacional persistente. Se a plataforma não suportar agentes separados, representar os papéis por contextos, sessões ou procedimentos equivalentes.

## 15. EXEMPLOS

### Exemplo 1 — conflito entre domínios
Marketing quer acelerar lançamento e Finanças identifica risco de margem.

→ Gestores apresentam evidências e recomendações.  
→ Coordenador arbitra a prioridade transversal ou escala ao Operador se necessário.

### Exemplo 2 — tarefa técnica
Gestor de Engenharia precisa corrigir um parser e rodar testes.

→ Roteia para executor técnico de software, como Codex ou equivalente.

### Exemplo 3 — tarefa híbrida
Um domínio precisa implementar uma feature e atualizar documentação operacional.

→ Decompor por capacidade.  
→ Executor técnico implementa e testa.  
→ Executor multissistema atualiza documentação.  
→ Gestor reconcilia e mantém o gate do domínio.

### Exemplo 4 — sucessão
Um Gestor atinge limite de contexto.

→ Produzir Handoff persistente.  
→ Sucessor audita.  
→ Coordenador valida.  
→ Só então o sucessor assume.

### Exemplo 5 — ação externa de baixo risco
Executor precisa atualizar um documento conforme conteúdo já aprovado e dentro de mandato explícito.

→ A existência de efeito externo, isoladamente, não exige nova confirmação. Avaliar escopo, reversibilidade e risco.

## 16. O QUE A SKILL NÃO DEVE FAZER

Não deve:
- transformar toda conversa em workflow formal;
- confundir Coordenador com Gestor de Domínio;
- transformar o Coordenador em gargalo;
- retirar autonomia legítima dos Gestores;
- transformar Executores em decisores;
- exigir produtos específicos;
- criar burocracia sem ganho de controle;
- duplicar o template da Delegation Context Skill;
- carregar contexto específico de projetos;
- tornar toda ação externa dependente de confirmação humana;
- permitir autovalidação de sucessão.

## Fonte canônica

Manter como fonte oficial versionada o repositório `Jadsonjg/ecosystem-agent-skills`, na pasta `skills/agentic-workflow-governance`.

Usar `references/especificacao-canonica.md` como fonte de verdade conceitual da Skill. A versão 2.0.0 é compatível com a **Arquitetura de Trabalho Agentiva v2.0** e substitui a lógica 1.x que fundia Coordenador e Gestor em uma única camada.

Mudanças estruturais de papéis, autoridade, gates, handoffs, fontes de verdade ou critérios de parada exigem revisão conjunta da arquitetura e desta Skill. O salvamento no GitHub não implica, por si só, atualização automática de uma instalação nativa em qualquer plataforma; a instalação deve ser conferida separadamente quando aplicável.
