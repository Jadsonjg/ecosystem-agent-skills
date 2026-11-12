# Changelog

## 2026-11-12 — Oficialização da identidade iconográfica

- Aprovação do Operador para as três identidades e para o pipeline do piloto `3636f0fb3428ddfa744b2d656116a8b44d2587b8`.
- Catálogo, variantes SVG e PNG, documentação, inventário, gerador de guias e regressões integrados à `main`. Identidades em estado `approved`, com assets legados e versões funcionais preservados.
- Guias oficiais v1.2.0 regenerados com a identidade aprovada. Validador interno, regressões e veraPDF 1.30.4 com perfil `ua1` aprovados para os três guias, com 106 regras e zero falhas em cada um. Comparação a 144 dpi limitada à região do ícone.
- As edições com identidade ficam em [Meu Drive / Skills](https://drive.google.com/drive/folders/1rRFedy2sxODJTqnh9Q2xGBaySnxjOGuF), com sufixo `-v1.2.0-identidade.pdf`. As edições anteriores foram preservadas para recuperação.
- A leitura com tecnologia assistiva e a propagação entre conversas são verificações distintas. A primeira criação real de ponta a ponta aguarda futura demanda do Operador.


Registrar todas as mudanças relevantes das Skills geridas neste repositório.

## Organização do monorepo — 2026-11-12

- Repositório reorganizado como `ecosystem-agent-skills`. As três Skills têm diretórios próprios e mantêm as versões existentes.
- Catálogo atualizado e caminhos legados da Delegation Context Skill preservados.
- Fluxo de criação e validação obrigatória de portabilidade documentados em [CONTRIBUTING.md](CONTRIBUTING.md).

## Nível de Criticidade [1.1.0] — 2026-10-15

### Alterado
- Gatilhos médios e fracos de revisão, análise, opinião, validação e decisão passam a ativar automaticamente 6/10 quando não houver nível vigente com precedência.
- O 6/10 de entrada estabelece baseline do escopo e continua nas interações relevantes seguintes, sem exigir reativação.
- Precedência atualizada para preservar padrões explícitos e baselines vigentes; um “revise isso” não reduz 8/10 nem substitui 4/10 explicitamente escolhido.
- Preservados overrides temporários com retorno ao baseline; “daqui para frente” redefine o baseline.
- Sinalização obrigatória da primeira ativação, mudança, override e retorno, incluindo nível, significado, como alterar e resumo da escala; sem repetir banner continuamente.
- O fluxo inicial verifica sinalização inclusive em configuração de estado e uso conjunto com outras Skills.
- Atualizados metadados, fonte canônica e inventário, preservando a instalação nativa existente.
- Instalação nativa 1.1.0 conferida: mesma identidade, sem duplicata; ícone regenerado pela plataforma e pacote final alinhados à fonte.
- Mantidas as regras de dez níveis, veracidade, evidência/status, autoridade, proporcionalidade, eficiência e compatibilidade. As outras duas Skills não foram alteradas.

### Validação
- 17 testes anteriores preservados e reexecutados; oito novos A–H adicionados: **25 aprovados**.
- Verificadas também entrada por gatilho médio, sinalização em configuração de projeto, consulta em contexto novo e compatibilidade com delegação.
- Corrigidas omissões de sinalização observadas na primeira rodada, com rechecagem em contextos novos.
- Persistência entre sessões continua condicionada à fonte de estado realmente disponível.
- [Relatório 1.1.0](tests/nivel-de-criticidade/v1.1.0.md).

## Nível de Criticidade [1.0.0] — 2026-10-15

### Adicionado
- Skill global e vendor-neutral, derivada da especificação integral fornecida pelo usuário em `Texto colado(1).txt`.
- Dez níveis individuais de rigor adversarial, agrupados em cinco faixas sem reduzir a escala a cinco modos.
- Separação entre criticidade, discordância, raciocínio, confiança, tom, extensão, detalhamento, pessimismo e autoridade.
- Tentativa de falsificação proporcional ao impacto, reversibilidade, incerteza, alcance e custo de correção.
- Disciplina de evidência/status, efeitos de segunda ordem, proteção de decisões aprovadas e parada/escalada por problema material.
- Resolução do nível por tarefa, temporário, domínio/projeto e padrão geral; expiração explícita e ausência de número inventado.
- Persistência apenas em fonte apropriada autorizada quando houver suporte; sem promessa de memória não registrada.
- Piso de segurança, veracidade e governança em todos os níveis, inclusive 1/10; aprovação integral de boa solução permitida em 10/10.
- Compatibilidade com Arquitetura de Trabalho Agentiva v2.0, Agentic Workflow Governance 2.0.0 e Delegation Context Skill 1.1.0, sem alterar essas Skills.

### Validação
- Executados os 17 cenários obrigatórios, com respostas observadas em contextos isolados e sequências de tarefas.
- Incluídas consulta efetiva de fonte sintética, expiração em duas sequências e recuperação de padrão de projeto em contexto novo.
- Resultado: 17 aprovados. Calibração dos dez níveis, preservação da fonte e integridade das Skills existentes também conferidas.
- Instalação nativa 1.0.0 concluída e verificada, com uma única Skill; textos e valores de interface preservados. Ícone e metadados de interface gerados pela plataforma incluídos no pacote versionado.
- [Evidências e limites da validação](tests/nivel-de-criticidade/v1.0.0.md).

## Agentic Workflow Governance [2.0.0] — 2026-10-11

### Alterado
- Separada a antiga camada única `Cérebro/Gestor` em uma hierarquia multinível: `Operador / Principal Humano → Coordenador → Gestor de Domínio → Executor`.
- Coordenador passou a responder por arbitragem transversal, prioridades entre domínios, arquitetura, dependências e gates interdomínio; Gestores preservam autonomia para decidir o COMO dentro do próprio nicho.
- Executores passaram a ser definidos por capacidade abstrata, com Work, Codex e equivalentes tratados como implementações possíveis, não requisitos conceituais.
- Fontes de verdade passaram a ser descritas por categorias portáveis, mantendo Drive e GitHub apenas como exemplos de implementação.
- Governança de ações deixou de usar “efeito externo” como critério automático de confirmação e passou a avaliar `escopo autorizado × reversibilidade × risco`.
- Formalizados Handoff, auditoria de sucessor e sucessão como mecanismos normais de continuidade operacional.
- Definido que sucessão de Gestor é validada pelo Coordenador e sucessão do próprio Coordenador é validada pelo Operador/Principal Humano.
- Removida a duplicação do template interno da Delegation Context Skill; Agentic Workflow Governance mantém a interface de autoridade/roteamento/gates e a Delegation Context Skill mantém o formato vigente de delegação.
- Revisada a precedência de autoridade para respeitar segurança/sistema, Operador, governança oficial do projeto, Coordenador e Gestor de Domínio.
- A especificação canônica deixou de ser o anexo histórico imutável e passou a ser uma especificação versionada alinhada à Arquitetura de Trabalho Agentiva v2.0.
- Atualizados metadados de interface, inventário `skills.json` e README.

### Compatibilidade
- Compatível com **Arquitetura de Trabalho Agentiva v2.0**.
- Delegation Context Skill permanece em **1.1.0**; sua lógica interna não foi alterada nesta revisão.

## Delegation Context Skill [1.1.0] — 2026-10-11

### Alterado
- Raciocínio recomendado passou a ser obrigatório, ao lado de Ação e Resultado esperado, inclusive em tarefas simples.
- Definidos exatamente cinco níveis: Low, Medium, High, Extra High e Maximum; usar o menor nível suficiente, com justificativa curta.
- Modelo recomendado permanece opcional e separado de raciocínio.
- Retirada a alternativa “Informações adicionais: nenhuma”.
- Preservados os dois blocos, não duplicação, portabilidade, papéis, limites de autoridade e critérios de parada; incluídas as determinações explícitas do usuário sobre segurança, arquitetura prematura e anti-burocracia.
- Atualizados prompt mestre, instalador e exemplos para eliminar divergências com a instalação nativa.
- Incluídos SKILL.md, metadados de interface e ícone da Skill instalada.

## Agentic Workflow Governance [1.0.0] — 2026-10-11

### Adicionado
- Skill nativa e especificação canônica integral na pasta `skills/agentic-workflow-governance/`.
- Gestor como autoridade central; Work e Codex como braços paralelos, com roteamento direto.
- Limites de autoridade, critérios de parada, fontes da verdade, ações reversíveis/sensíveis, contexto e anti-burocracia.
- Complementaridade com Delegation Context Skill, preservando a precedência e os critérios de acionamento da fonte.
- Registro da proveniência do conteúdo recebido em `Texto colado.txt`, convertido em Markdown sem alteração de conteúdo.

## Gestão das Skills — 2026-10-11

### Decisão do usuário
- Atribuída a este chat a função de Gestor de Skills para criação e gestão das alterações.
- GitHub adotado como fonte oficial; não criar documento de gestão no Drive.
- Mantido o endereço do repositório existente; as duas Skills são geridas aqui.
- Atualizadas as referências de fonte nas instalações nativas; regras operacionais preservadas.

### Validação
- Estrutura nativa das duas Skills validada.
- Comportamentos já conferidos: delegação simples com Low, parada por arquivo essencial ausente, roteamento híbrido e interrupção de experimento sem autorização.
- Nesta atualização, apenas as referências de fonte das instalações foram alteradas; a lógica operacional permaneceu igual.

## [1.0.0] — 2026-10-09

### Adicionado
- Estrutura `Informações adicionais` → `Comando / Briefing`.
- Campos centrais `Ação` e `Resultado esperado`.
- Campos opcionais para modelo/raciocínio, ferramentas, arquivos, dependências, permissões, limitações e cuidados.
- Princípio de não duplicação entre contexto executivo e briefing operacional.
- Regra de interrupção antes da delegação quando houver premissa, ferramenta, dado ou direção inadequada.
- Critério para recomendar executor separado apenas quando houver especialização, recorrência, volume, complexidade ou continuidade.
- Distinção entre recomendação semântica de raciocínio e configuração técnica acionável.
- Regra de portabilidade entre plataformas.
- Prompt Mestre reutilizável.
- Instalador curto para ambientes com acesso ao repositório.
- Exemplos de aplicação.
