# Contribuir com o Ecosystem Agent Skills

## Estrutura

| Caminho | Função |
| --- | --- |
| `README.md` | Apresentação e catálogo para leitura humana. |
| `skills.json` | Inventário com nome, versão e caminho canônico de cada Skill. |
| `CHANGELOG.md` | Histórico das alterações por Skill e da organização do monorepo. |
| `skills/<identificador>/SKILL.md` | Instruções canônicas, com nome, descrição e critérios de ativação. |
| `skills/<identificador>/references/` | Referências consultadas quando necessárias. |
| `skills/<identificador>/scripts/` | Scripts reutilizáveis necessários ao procedimento. |
| `skills/<identificador>/assets/` | Recursos usados pela Skill. |
| `skills/<identificador>/agents/` | Metadados opcionais de integração com plataformas. |
| `tests/` | Verificações do catálogo e evidências de validação por Skill. |
| `.github/workflows/` | Automação das verificações do repositório. |

Crie as pastas opcionais conforme a necessidade. Preserve identificadores estáveis e atualize a versão de cada Skill conforme as suas próprias mudanças. Em reorganizações que só alterem caminhos ou documentação de localização, preserve as versões.

A fonte canônica da Delegation Context Skill está em `skills/delegation-context-skill/`. Mantenha os arquivos legados da raiz sincronizados quando alterar o pacote ou o prompt mestre. O catálogo deve apontar para a pasta canônica.

Este monorepo é público. Inclua somente Skills e materiais autorizados para publicação, inclusive no histórico importado.

## Criação em quatro etapas

1. **Proposta do Operador.** Registre o problema, a estrutura imaginada, quando houver, e as regras adicionais.
2. **Avaliação de viabilidade.** Explique em destaque o que é uma Skill e avalie se um procedimento reutilizável resolve o problema. Quando recomendar a criação, descreva o funcionamento, os gatilhos, os casos de uso e a viabilidade em outras plataformas.
3. **Revisão e autorização.** Incorpore as diretrizes do Operador. Comece a criar a Skill somente após autorização explícita para executar.
4. **Criação e conclusão.** Implemente e valide, salve a fonte no GitHub, atualize o catálogo, a versão e o changelog. Entregue o relatório em PDF em `Meu Drive / Skills` com o caminho para a Skill, a versão atual, o que ela faz em linguagem simples, suas aplicações e exemplos de quando evitar seu uso.

## Portabilidade obrigatória (vendor neutrality)

Descreva o procedimento principal em termos de capacidades, entradas, resultados e limites. Declare as dependências necessárias e como substituí-las quando a plataforma mudar. Exemplos, metadados e adaptadores específicos de um fornecedor são permitidos quando opcionais e separados do procedimento principal.

Antes de aprovar uma Skill nova:

- Execute ao menos um cenário representativo fora do ChatGPT, usando as instruções canônicas e as capacidades equivalentes disponíveis. Registre o ambiente, o cenário, as dependências substituídas e o resultado observado.
- Confira se a ativação, as etapas essenciais e o resultado esperado continuam viáveis sem um recurso exclusivo do ChatGPT. Valide também um cenário em que a Skill deve permanecer inativa.
- **Barre a aprovação e a publicação** se o fluxo essencial só funcionar no ChatGPT ou se a portabilidade ainda estiver sem evidência. Uma integração opcional pode ter validação própria, separada da aprovação da Skill.

A verificação automatizada abaixo cobre a estrutura. A decisão de portabilidade depende do teste funcional e da evidência registrada.

```sh
python3 tests/validate_catalog.py
```

## Guias rápidos em PDF

Use o [Padrão Visual da Biblioteca de Skills](docs/guias-visuais/README.md) para gerar, validar e publicar o relatório de uso de cada Skill. O padrão define a composição, as regras de acessibilidade, os arquivos reutilizáveis e o limite de páginas.
