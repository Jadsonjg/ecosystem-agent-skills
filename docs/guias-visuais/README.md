# Padrão Visual da Biblioteca de Skills

**Versão vigente: 1.2.0 · 12/11/2026**
**Escopo:** Guias Rápidos da Biblioteca de Skills do Ecossistema IA & Operações.

Este diretório é a referência oficial para escrever, gerar e conferir novos guias. A especificação da Skill correspondente em `skills/<identificador>/SKILL.md` define seu funcionamento. Este padrão define como apresentá-lo.

## Composição fixa

1. Cabeçalho na cor institucional registrada para a Skill, com texto branco, nome e versão da Skill, título didático e uma frase introdutória. A edição oficial usa “BIBLIOTECA DE SKILLS”. Em propostas, indique “PROPOSTA VISUAL — NÃO OFICIAL”.
2. Três cards, nesta ordem: **Para que serve?**, **O que resolve?**, **Como se aplica?**. Use linguagem para leigos, com uma ideia por card. No A4, os três ficam lado a lado. Sintetize o texto antes de alterar o tamanho da fonte.
3. Demonstração prática. Identifique o cenário e apresente uma situação concreta e fiel à Skill.
4. **Quando não usar?** Mostre de um a três exemplos breves. Indique em que situações a Skill é dispensável.
5. Referência ao fim da última página. “Para mais informações sobre a Skill:” e, na linha seguinte, o link “Consultar a pasta oficial no GitHub.”. Confira o destino no catálogo e no repositório.

O template implementa margens de 42 pt, vão de 12 pt entre cards, cabeçalho de 154 pt e corpo dos cards de 10,5 pt com entrelinha de 15 pt. Título principal em DejaVu Serif 29 pt, seções em DejaVu Serif 15,5–19 pt ou DejaVu Sans Bold conforme o componente, corpo e rótulos em DejaVu Sans. O espaço dos componentes intermediários segue o conteúdo. As medidas do gerador são a implementação de referência.

| Cor | Uso |
| --- | --- |
| `cor_institucional` | Fundo dos cabeçalhos, títulos dos cards, destaques do bloco adicional, título de “Quando não usar?” e link final |
| `#F7F7F2` / `#FFFFFF` | Papel, cards e texto branco nos cabeçalhos |
| `#202A26` / `#4B5A53` | Texto e informação secundária |
| `#E8F1E9` / `#CFDAD2` | Realces e divisórias |
| `#212121` / `#1E5AAD` | Fundo da conversa e balão do usuário |
| `#ECECEC` / `#B4B4B4` | Texto e rótulos da conversa |

## Cor institucional por Skill

| Skill | Cor registrada | Branco no cabeçalho |
| --- | --- | ---: |
| [Delegation Context Skill](conteudo/delegation-context-skill.json) | Verde profundo · `#143B36` | 12,29:1 |
| [Agentic Workflow Governance](conteudo/agentic-workflow-governance.json) | Azul profundo · `#233D63` | 10,94:1 |
| [Nível de Criticidade](conteudo/nivel-de-criticidade.json) | Vinho profundo · `#59273F` | 11,75:1 |

O registro está na chave `cor_institucional` do JSON de cada Skill. Ao adicionar uma Skill, compare as cores já registradas, escolha um tom profundo e distinguível e registre o código `#RRGGBB`. Use a cor solicitada pelo Operador quando houver. Se o tom não passar no contraste, ajuste-o para uma variante mais escura antes de registrar. Confirme o resultado nos guias renderizados. A geração sempre reutiliza o código registrado. Reavalie uma cor existente somente quando o Operador solicitar sua substituição.

O gerador e o validador aplicam a luminância relativa sRGB da [WCAG 2.2](https://www.w3.org/TR/WCAG22/#dfn-relative-luminance). O mínimo é 7:1 para branco sobre a cor institucional, inclusive no cabeçalho compacto e na numeração. Os textos coloridos exigem no mínimo 4,5:1 sobre papel e realce claro. A tipografia, os fundos das áreas de leitura, as divisórias e a conversa mantêm os tons fixos da tabela. Os balões do usuário mantêm `#1E5AAD`. Nome, versão e rótulos identificam o conteúdo em texto.

Todo JSON novo deve registrar uma cor. Para reproduzir arquivos de entrada históricos da v1.0.0 sem essa chave, o gerador usa o verde histórico `#143B36`.

## Densidade e revisão editorial

1. Leia o `SKILL.md` e identifique o **essencial**: finalidade, ocasião de uso, como solicitar, resultado esperado e limites que mudam a conduta do leitor.
2. Selecione o **complementar de alto valor**: exemplos, distinções ou decisões que tornem o uso mais claro. Deixe detalhes **técnicos ou especializados** na documentação oficial, salvo quando forem indispensáveis à compreensão.
3. Confira se um leitor leigo consegue interpretar a demonstração e decidir quando a Skill é dispensável. Faça essa revisão mesmo quando a página já parecer bem composta.
4. Se sobrar muito espaço, revise, nesta ordem: lacunas essenciais, complementos de alto valor, suficiência do exemplo, utilidade de um recurso visual e distribuição dos componentes. Preserve o respiro quando o conteúdo já for suficiente. Não use meta de ocupação, texto repetido ou ampliação artificial de fontes e caixas.

## Escolha dos componentes

- **Conteúdo adicional:** use o bloco de dois a quatro itens quando o leitor precisar entender uma sequência, escala, regra ou estrutura antes da demonstração. Use itens numerados somente quando a ordem fizer parte do conceito.
- **Conversa:** prefira quando a interação mostrar como ativar uma Skill, mudar um parâmetro ou obter uma resposta estruturada. Use mensagens curtas, contexto fictício, balão azul à direita e resposta aberta sobre o fundo escuro. Identifique sempre “Você” e “Assistente” em texto. Na configuração de rigor, demonstre os avisos de mudança pertinentes.
- **Demonstração sem conversa:** para Skills centradas em um processo ou resultado, use um caso comentado no bloco textual `paragrafos`. A combinação desse bloco com a sequência em `adicional` cobre um processo linear. Para uma decisão ramificada, descreva as opções e seus critérios em ordem lógica. Adote um diagrama somente se ele comunicar relações que o texto não deixa claras. Use rótulos textuais e registre uma descrição equivalente.
- **Economia visual:** mantenha apenas recursos que cumprem uma função diferente. Uma escala pode explicar os níveis, e a conversa pode mostrar como mudar de nível. Dispense ambos quando um caso curto já demonstrar a aplicação.
- **Paginação:** tente uma página A4. Use duas se a continuação trouxer ganho didático e a síntese tornar o exemplo incompleto. Com `duas_paginas: true`, inclua `demonstracao_inicial` para a primeira parte do caso e `demonstracao` para a continuação. Os cards aparecem apenas na primeira página. A segunda usa cabeçalho compacto, e o encerramento fica no fim. O gerador recusa conteúdo que extrapole a área útil. Mais de duas páginas exige autorização expressa do Operador.

## Recursos visuais

Distinga um gráfico dispensável de um gráfico útil ainda sem suporte. No segundo caso, verifique se um componente simples pode explicar a relação. Reuse o gerador ou consulte os assets do projeto antes de desenhar. Prefira vetores reutilizáveis para relações, sequências e comparações. Para recurso externo, confirme origem, licença, ganho didático e descrição acessível antes da adoção. Os ícones existentes são opcionais e não são necessários à geração.

| Necessidade | Suporte atual |
| --- | --- |
| Escala ou comparação simples | `adicional.itens` com títulos e textos curtos |
| Sequência linear | `adicional.sequencial: true` para numerar |
| Hierarquia ou relação linear | `adicional.relacao` com legenda obrigatória, de dois a quatro itens e setas vetoriais entre eles |
| Caso comentado ou conversa | `demonstracao.paragrafos` ou `demonstracao.turnos` |
| Regra prática após a demonstração | `orientacao` com `titulo` e `paragrafos`, antes de “Quando não usar?” |

O diagrama linear preserva uma lista etiquetada com os rótulos na ordem de leitura. Descreva o sentido e a natureza da relação em `relacao`, sem exigir que o leitor interprete a posição ou a cor. As setas são artefatos porque a legenda e a lista já comunicam a mesma relação. Use frases legíveis e teste a largura dos rótulos. O exemplo reutilizável está no [JSON de Governance](conteudo/agentic-workflow-governance.json).

O gerador cobre os casos acima. Para ramificações, mapas mentais ou figuras cujo significado não possa ser expresso pelo componente linear, avalie uma extensão específica quando houver necessidade. Figuras informativas independentes exigem `Figure` e `Alt` ou representação semântica equivalente devidamente validada. A versão atual recusa imagens rasterizadas no PDF.

## Produção

Pré-requisitos: Python 3.12, fontes DejaVu Sans e Serif e dependências de [requirements.txt](requirements.txt). Use um ambiente virtual. No Linux, instale o pacote de fontes DejaVu ou informe `SKILLS_FONT_DIR` com o diretório dos três arquivos TTF. O renderizador não depende de serviço externo.

```sh
cd docs/guias-visuais
python -m pip install -r requirements.txt
python gerar.py conteudo/delegation-context-skill.json delegation-context-skill-guia-rapido-padrao-v1.2.0.pdf
python validar.py conteudo/delegation-context-skill.json delegation-context-skill-guia-rapido-padrao-v1.2.0.pdf
```

1. Consulte o catálogo e o `SKILL.md` da versão vigente. Copie um dos exemplos em [conteudo/](conteudo/) e preencha o JSON com a explicação e a demonstração apropriadas.
2. Reuse [gerar.py](gerar.py). Em novos guias, altere o conteúdo em JSON. O gerador compõe os componentes e suas etiquetas no mesmo fluxo. Use `<identificador>-guia-rapido-padrao-v<versão-do-padrão>.pdf` no PDF e a versão funcional da Skill no cabeçalho.
3. Rode [validar.py](validar.py). Renderize todas as páginas, inspecione a versão normal e uma prévia de 390 px, teste a URL e compare o exemplo com a fonte técnica. O PDF A4 mantém paginação fixa e pode exigir zoom no celular.
4. Registre a versão funcional da Skill, a versão visual e a localização do PDF. Salve o guia validado em `Meu Drive / Skills`. Atualize esta especificação e sua versão somente ao alterar o padrão comum.

## Acessibilidade

O gerador usa PDF 1.7, `pt-BR`, título nos metadados, fontes incorporadas e texto selecionável. Titula H1–H3 em ordem, marca parágrafos e listas, vincula a anotação do link à estrutura e mantém a ordem de foco baseada na estrutura. Em conversas, a ordem é usuário, mensagem, assistente e resposta, repetida por turno. As formas decorativas são artefatos.

O template trabalha com texto e vetores. Se um recurso exigir imagem informativa, estenda o gerador para produzir `Figure` com `Alt` e teste a leitura antes de publicar. Se usar tabelas futuramente, implemente cabeçalhos e associações semânticas. O validador atual recusa imagens não previstas. Use PDF/UA (ISO 14289) como referência. O PDF inclui metadados XMP com identificação PDF/UA-1 e título coerente com Info. Execute o perfil explícito `ua1` do veraPDF para verificar os requisitos automatizáveis. Consulte o [registro da correção técnica](CORRECAO-XMP-1.2.0.md) para os testes e limites da avaliação. A validação automatizada não representa certificação formal PDF/UA.

O [relatório comparativo da v1.2.0](IMPLEMENTACAO-1.2.0.md) registra o diagnóstico, as verificações e os limites da validação. A [v1.1.0](https://github.com/Jadsonjg/ecosystem-agent-skills/blob/8fa4471c3af8bd248b7cbdde758a7951e79711fe/docs/guias-visuais/README.md) e seu [relatório](IMPLEMENTACAO-1.1.0.md) permanecem disponíveis. Consulte o [padrão histórico v1.0.0](https://github.com/Jadsonjg/ecosystem-agent-skills/blob/4b2ba9dff58d5526789c9420b6e6a44474c918fe/docs/guias-visuais/README.md) e seu [relatório](IMPLEMENTACAO.md).
