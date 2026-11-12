# Padrão Visual da Biblioteca de Skills

**Versão vigente: 1.0.0 · 12/11/2026**
**Escopo:** Guias Rápidos da Biblioteca de Skills do Ecossistema IA & Operações.

Este diretório é a referência oficial para escrever, gerar e conferir novos guias. A especificação da Skill correspondente em `skills/<identificador>/SKILL.md` define seu funcionamento. Este padrão define como apresentá-lo.

## Composição fixa

1. Cabeçalho institucional verde-escuro, nome e versão da Skill, título didático e uma frase introdutória. A edição oficial usa “BIBLIOTECA DE SKILLS”. Em propostas, indique “PROPOSTA VISUAL — NÃO OFICIAL”.
2. Três cards, nesta ordem: **Para que serve?**, **O que resolve?**, **Como se aplica?**. Use linguagem para leigos, com uma ideia por card. No A4, os três ficam lado a lado. Sintetize o texto antes de alterar o tamanho da fonte.
3. Demonstração prática. Identifique o cenário e apresente uma situação concreta e fiel à Skill.
4. **Quando não usar?** Mostre de um a três exemplos breves. Indique em que situações a Skill é dispensável.
5. Referência ao fim da última página. “Para mais informações sobre a Skill:” e, na linha seguinte, o link “Consultar a pasta oficial no GitHub.”. Confira o destino no catálogo e no repositório.

O template implementa margens de 42 pt, vão de 12 pt entre cards, cabeçalho de 154 pt e corpo dos cards de 10,5 pt com entrelinha de 15 pt. Título principal em DejaVu Serif 29 pt, seções em DejaVu Serif 15,5–19 pt ou DejaVu Sans Bold conforme o componente, corpo e rótulos em DejaVu Sans. O espaço dos componentes intermediários segue o conteúdo. As medidas do gerador são a implementação de referência.

| Cor | Uso |
| --- | --- |
| `#143B36` | Cabeçalho, títulos funcionais e link final |
| `#F7F7F2` / `#FFFFFF` | Papel e cards |
| `#202A26` / `#4B5A53` | Texto e informação secundária |
| `#E8F1E9` / `#CFDAD2` | Realces e divisórias |
| `#212121` / `#1E5AAD` | Fundo da conversa e balão do usuário |
| `#ECECEC` / `#B4B4B4` | Texto e rótulos da conversa |

## Escolha dos componentes

- **Conteúdo adicional:** use o bloco de dois a quatro itens quando o leitor precisar entender uma sequência, escala, regra ou estrutura antes da demonstração. Use itens numerados somente quando a ordem fizer parte do conceito.
- **Conversa:** prefira quando a interação mostrar como ativar uma Skill, mudar um parâmetro ou obter uma resposta estruturada. Use mensagens curtas, contexto fictício, balão azul à direita e resposta aberta sobre o fundo escuro. Identifique sempre “Você” e “Assistente” em texto. Na configuração de rigor, demonstre os avisos de mudança pertinentes.
- **Demonstração sem conversa:** para Skills centradas em um processo ou resultado, use um caso comentado no bloco textual `paragrafos`. A combinação desse bloco com a sequência em `adicional` cobre um processo linear. Para uma decisão ramificada, descreva as opções e seus critérios em ordem lógica. Adote um diagrama somente se ele comunicar relações que o texto não deixa claras. Use rótulos textuais e registre uma descrição equivalente.
- **Economia visual:** mantenha apenas recursos que cumprem uma função diferente. Uma escala pode explicar os níveis, e a conversa pode mostrar como mudar de nível. Dispense ambos quando um caso curto já demonstrar a aplicação.
- **Paginação:** tente uma página A4. Use duas se a continuação trouxer ganho didático e a síntese tornar o exemplo incompleto. Com `duas_paginas: true`, inclua `demonstracao_inicial` para a primeira parte do caso e `demonstracao` para a continuação. Os cards aparecem apenas na primeira página. A segunda usa cabeçalho compacto, e o encerramento fica no fim. O gerador recusa conteúdo que extrapole a área útil. Mais de duas páginas exige autorização expressa do Operador.

## Produção

Pré-requisitos: Python 3.12, fontes DejaVu Sans e Serif e dependências de [requirements.txt](requirements.txt). Use um ambiente virtual. No Linux, instale o pacote de fontes DejaVu ou informe `SKILLS_FONT_DIR` com o diretório dos três arquivos TTF. O renderizador não depende de serviço externo.

```sh
cd docs/guias-visuais
python -m pip install -r requirements.txt
python gerar.py conteudo/delegation-context-skill.json delegation-context-skill-guia-rapido-padrao-v1.0.0.pdf
python validar.py conteudo/delegation-context-skill.json delegation-context-skill-guia-rapido-padrao-v1.0.0.pdf
```

1. Consulte o catálogo e o `SKILL.md` da versão vigente. Copie um dos exemplos em [conteudo/](conteudo/) e preencha o JSON com a explicação e a demonstração apropriadas.
2. Reuse [gerar.py](gerar.py). Em novos guias, altere o conteúdo em JSON. O gerador compõe os componentes e suas etiquetas no mesmo fluxo. Use `<identificador>-guia-rapido-padrao-v<versão-do-padrão>.pdf` no PDF e a versão funcional da Skill no cabeçalho.
3. Rode [validar.py](validar.py). Renderize todas as páginas, inspecione a versão normal e uma prévia de 390 px, teste a URL e compare o exemplo com a fonte técnica. O PDF A4 mantém paginação fixa e pode exigir zoom no celular.
4. Registre a versão funcional da Skill, a versão visual e a localização do PDF. Salve o guia validado em `Meu Drive / Skills`. Atualize esta especificação e sua versão somente ao alterar o padrão comum.

## Acessibilidade

O gerador usa PDF 1.7, `pt-BR`, título nos metadados, fontes incorporadas e texto selecionável. Titula H1–H3 em ordem, marca parágrafos e listas, vincula a anotação do link à estrutura e mantém a ordem de foco baseada na estrutura. Em conversas, a ordem é usuário, mensagem, assistente e resposta, repetida por turno. As formas decorativas são artefatos.

A versão 1.0.0 trabalha com texto e vetores. Se um recurso exigir imagem informativa, estenda o gerador para produzir `Figure` com `Alt` e teste a leitura antes de publicar. Se usar tabelas futuramente, implemente cabeçalhos e associações semânticas. O validador atual recusa imagens não previstas. Use PDF/UA (ISO 14289) como referência. A validação implementada cobre os requisitos documentados e não representa certificação formal PDF/UA.

O [relatório de implementação](IMPLEMENTACAO.md) registra os testes, as limitações e os dois guias da edição inicial.
