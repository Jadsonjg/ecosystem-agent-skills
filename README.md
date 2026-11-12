# Ecosystem Agent Skills

Fonte oficial das Skills **Delegation Context Skill**, **Agentic Workflow Governance** e **Nível de Criticidade**.
Monorepo público de Skills do ecossistema. Consulte o [guia de contribuição](CONTRIBUTING.md) para conhecer a estrutura e o critério obrigatório de portabilidade.

## Inventário

| Skill | Versão | Fonte oficial | Compatibilidade | Instalação nativa |
| --- | --- | --- | --- | --- |
| <picture><source media="(prefers-color-scheme: dark)" srcset="skills/delegation-context-skill/assets/identity/icone-negativo.svg"><img src="skills/delegation-context-skill/assets/identity/icone.svg" alt="" width="20" height="20"></picture> Delegation Context Skill <sup>(ícone piloto)</sup> | 1.1.0 | [SKILL.md](skills/delegation-context-skill/SKILL.md) | Interface de delegação vigente | [ChatGPT](https://chatgpt.com/skills?skill_id=6acbd243c8088191b2e61b170ec6779c) |
| Agentic Workflow Governance | 2.0.0 | [Especificação canônica](skills/agentic-workflow-governance/references/especificacao-canonica.md) e [SKILL.md](skills/agentic-workflow-governance/SKILL.md) | Arquitetura de Trabalho Agentiva v2.0 | [ChatGPT](https://chatgpt.com/skills?skill_id=6acbe3f484b48191a13bc6797c8b6bf1) |
| Nível de Criticidade | 1.1.0 | [Especificação canônica](skills/nivel-de-criticidade/references/especificacao-canonica.md) e [SKILL.md](skills/nivel-de-criticidade/SKILL.md) | Arquitetura de Trabalho Agentiva v2.0; governança 2.0.0 e delegação 1.1.0 | [ChatGPT](https://chatgpt.com/skills?skill_id=6ad15379a0888191a8ff569f84eed566) |

[skills.json](skills.json) registra caminhos, versões e compatibilidade para conferência.

[Demonstração do ícone e referência compacta](skills/delegation-context-skill/README.md)

## Autoridade e gestão

Em 11/10/2026, o usuário atribuiu a este chat a função de **Gestor de Skills**, responsável por criar, manter e gerir alterações destas habilidades.

- GitHub é a fonte oficial versionada das especificações, pacotes nativos e histórico de alterações.
- ChatGPT mantém as instalações nativas utilizadas nas conversas.
- O relatório de conclusão de cada Skill nova é salvo em PDF em `Meu Drive / Skills`. A fonte técnica e as versões ficam neste repositório.
- O usuário mantém a autoridade sobre decisões sensíveis e mudanças de intenção. A função de Gestor de Skills não concede autoridade sobre outros projetos.
- As alterações de Skills são executadas dentro das instruções e autorizações vigentes do usuário; conflitos materiais são apresentados antes de mudar a lógica.
- O salvamento no GitHub não atualiza automaticamente a instalação no ChatGPT. Fonte versionada e instalação nativa devem ser verificadas separadamente.

## Como as Skills se complementam

### Agentic Workflow Governance

Define a governança multinível do sistema:

**Operador / Principal Humano → Coordenador → Gestor de Domínio → Executor**.

Seu papel é resolver:
- quem possui autoridade para decidir;
- o que é transversal e o que pertence a um domínio;
- qual capacidade executora é adequada;
- limites de autoridade e critérios de parada;
- fontes de verdade e engenharia de contexto;
- gates, ações sensíveis e escaladas;
- continuidade, Handoff e sucessão.

A versão 2.0.0 é vendor-neutral: Work, Codex, Drive e GitHub são implementações possíveis de papéis ou fontes abstratas, não requisitos da arquitetura.

Ações são avaliadas por **escopo autorizado × reversibilidade × risco**, em vez de exigir confirmação apenas porque produzem efeito externo.

### Delegation Context Skill

Estrutura a delegação formal, nesta ordem:

### Informações adicionais

**Ação:** descrição executiva.

**Resultado esperado:** resultado final esperado.

**Raciocínio recomendado:** Low, Medium, High, Extra High ou Maximum — justificativa curta e prática.

### Comando / Briefing

Instruções completas necessárias ao executor.

Os três campos são sempre obrigatórios na versão 1.1.0, inclusive em tarefas simples. Modelo, ferramentas, arquivos, dependências, permissões, limitações e cuidados continuam opcionais. Usar o menor nível suficiente; não duplicar passos e validações nas Informações adicionais; não gerar briefing final enquanto existir bloqueio relevante.

A Agentic Workflow Governance não congela nem duplica internamente esse template: ela define autoridade, roteamento, fontes e gates; a Delegation Context Skill define a forma vigente da delegação.

As Skills não substituem uma à outra e não precisam transformar conversas triviais em workflow formal.

### Nível de Criticidade

Regula de 1 a 10 o rigor adversarial aplicado a premissas, propostas, decisões, planos, execuções e resultados. Os dez níveis continuam calibrados individualmente; criticidade não equivale a discordância, autoridade, raciocínio, confiança, tom ou extensão da resposta.

Na versão **1.1.0**, pedidos cotidianos de revisão, análise, opinião, validação ou decisão ativam criticidade sem exigir expressão técnica. Gatilhos médios (“procure falhas”, “analise os riscos”) e fracos (“revise isso”, “o que você acha?”) estabelecem automaticamente **6/10 — análise crítica ativa**, se não houver nível vigente com precedência. Não se pergunta qual nível usar.

O 6/10 torna-se baseline do escopo, continua nas análises seguintes sem novo gatilho e não expira após a primeira resposta. Um baseline de 8/10, 4/10 ou outro nível já legitimamente vigente não é substituído pelo padrão de entrada 6/10.

Precedência: nível explícito da tarefa → override temporário vigente → nível persistente explícito do usuário → baseline vigente → gatilho forte de intensidade implícita → gatilho médio 6/10 → gatilho fraco 6/10. Comandos explícitos de mudança atualizam o estado correspondente: “só nesta decisão” cria override; “daqui para frente” redefine baseline.

Sinalizar a primeira ativação, a mudança de nível, o override temporário e o retorno ao baseline, informando nível, significado, como alterar e resumo da escala. Depois, aplicar silenciosamente até a próxima transição ou necessidade real de esclarecimento.

Exemplo: baseline 6/10 → “só nesta decisão use criticidade máxima” → 10/10 temporário → tarefa seguinte retorna a 6/10, com sinalização. Não alegar persistência entre contextos se a fonte de estado não estiver realmente disponível. Não gravar uma preferência local na Skill global.

A Skill respeita Agentic Workflow Governance e mantém criticidade separada do raciocínio recomendado da Delegation Context Skill. **25 testes obrigatórios aprovados**: os 17 originais foram preservados e reexecutados, com oito testes novos A–H. [Relatório da revisão](tests/nivel-de-criticidade/v1.1.0.md); [validação histórica 1.0.0](tests/nivel-de-criticidade/v1.0.0.md).

## Compatibilidade com a Arquitetura de Trabalho Agentiva

A **Agentic Workflow Governance v2.0.0** corresponde conceitualmente à **Arquitetura de Trabalho Agentiva v2.0**.

Mudanças estruturais em papéis, autoridade, gates, handoffs, fontes de verdade ou critérios de parada exigem revisão conjunta da arquitetura e da Skill. Mudanças internas do template de delegação permanecem sob a Delegation Context Skill, desde que a interface entre as duas continue compatível.

## Fluxo de manutenção

1. Ler a fonte canônica, a arquitetura compatível e a decisão vigente do usuário.
2. Preparar a alteração mínima, preservando regras obrigatórias, autoridade e critérios de parada.
3. Validar estrutura, coerência das referências, exemplos e eventuais mudanças de comportamento.
4. Salvar a fonte no GitHub, atualizar versão quando necessário e registrar a alteração no [CHANGELOG.md](CHANGELOG.md).
5. Atualizar a Skill nativa existente quando a plataforma disponibilizar uma ação de edição, sem criar instalação duplicada.
6. Conferir os arquivos salvos e informar com precisão o que foi atualizado e o que permaneceu pendente.

Não prometer acompanhamento automático de mudanças externas sem uma automação configurada.

## Estrutura e compatibilidade

Cada Skill tem uma pasta própria em `skills/`. A fonte canônica da Delegation Context Skill fica em [skills/delegation-context-skill/](skills/delegation-context-skill/). Os arquivos legados na raiz preservam os caminhos usados por integrações existentes.

A Agentic Workflow Governance fica em `skills/agentic-workflow-governance/`, com:
- `SKILL.md` — comportamento executável;
- `references/especificacao-canonica.md` — fonte conceitual canônica;
- `agents/openai.yaml` — metadados de interface;
- `assets/` — ativos da Skill.

`prompt-mestre.md` é uma exportação do corpo do `SKILL.md` da Delegation Context Skill para uso em outros chats. Deve ser regenerado junto com a fonte, sem manter lógica divergente. O [instalador-curto.md](skills/delegation-context-skill/instalador-curto.md) aponta para a fonte vigente; [exemplos.md](skills/delegation-context-skill/exemplos.md) demonstra o comportamento.

A especificação canônica da Agentic Workflow Governance é versionada e deve permanecer alinhada à versão compatível da Arquitetura de Trabalho Agentiva. Ela não é um arquivo histórico imutável: mudanças estruturais aprovadas devem produzir nova versão e registro no changelog.
