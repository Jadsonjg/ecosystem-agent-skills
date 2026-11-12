# Relatório de implementação · Padrão Visual 1.0.0

**Data:** 12/11/2026
**Estado:** padrão documental e visual vigente.
**Referência oficial:** [Padrão Visual da Biblioteca de Skills](README.md).

## Ajustes e preservações

Mantivemos o cabeçalho institucional em verde-escuro, os títulos serifados, a composição editorial, os cards e a conversa em fundo escuro com balões azuis. Os cards passaram de 99 para 115 pt, com corpo de 10,5 pt. A conversa passou a ocupar a altura necessária ao conteúdo, com mensagens mais concisas. O encerramento ganhou exemplos adicionais de quando a Skill é dispensável e o texto de referência solicitado.

O guia de Delegation Context mantém os três campos de informações adicionais e o bloco de execução. O de Criticidade mostra a entrada em 6/10 quando nenhum nível tem precedência e a mudança temporária para 10/10. A demonstração agora sinaliza o nível, como alterá-lo, a escala e a preservação do nível padrão durante a mudança temporária, conforme o `SKILL.md`. A revisão foi documental e visual.

## Geração e resultados

O conteúdo está separado do layout nos arquivos JSON de [conteudo/](conteudo/). ReportLab 4.4.9 compõe as páginas e marca o conteúdo na origem. pypdf 6.21.4 grava o catálogo e a árvore semântica, com mapa de conteúdo e referências das anotações. O PDF 1.7 resultante preserva texto e formas vetoriais. A geração funciona localmente com Python 3.12 e as fontes DejaVu.

| Verificação | Ferramenta e resultado |
| --- | --- |
| Renderização e proporção | Poppler e inspeção das duas páginas finais em tamanho normal e a 390 px. Nenhum corte ou sobreposição observados. O A4 pode exigir zoom em tela estreita. |
| Fidelidade didática | Conferência com os dois `SKILL.md` do catálogo, nos caminhos verificados no commit `14ba972`. Os exemplos são fictícios. |
| Etiquetas e leitura | `validar.py`, pypdf e PyMuPDF 1.26.6. Delegation com 39 blocos semânticos e 16 artefatos. Criticidade com 38 blocos semânticos e 12 artefatos. Árvore, ordem dos MCIDs e mapa de parentesco conferidos, com títulos, listas, parágrafos e um link estruturado por guia. |
| Texto, idioma e fonte | `validar.py`, `pdfinfo` e `pdffonts`. Idioma `pt-BR`, texto pesquisável, A4, Tagged PDF 1.7 e fontes DejaVu incorporadas com mapeamento Unicode. |
| Contraste | Cálculo por luminância relativa. Texto no balão azul com 5,70:1, texto na conversa escura com 13,63:1 e rótulos dos participantes com 7,77:1. |
| Navegação | Link da última página associado à etiqueta `Link` e à ordem de foco estrutural. Destinos confirmados no repositório. |
| Reprodutibilidade | Geração dos dois guias a partir de seus JSONs e teste adicional de duas páginas. O teste passou com 44 blocos semânticos, 19 artefatos e o link na última página. |

O método foi validado pelos critérios estruturais deste projeto. A avaliação não incluiu certificação formal PDF/UA, teste com leitor de tela ou validação de tabelas e imagens informativas. Nenhum dos dois guias inclui tabelas ou imagens. O guia de produção define como tratar esses elementos quando forem necessários.

## Registro dos guias

Pasta operacional: **Meu Drive / Skills**. As edições desta tabela são os guias do padrão visual 1.0.0. As versões funcionais das Skills permanecem 1.1.0.

| Skill | Edição do guia | Arquivo |
| --- | --- | --- |
| Delegation Context Skill 1.1.0 | Padrão visual 1.0.0 | `delegation-context-skill-guia-rapido-padrao-v1.0.0.pdf` |
| Nível de Criticidade 1.1.0 | Padrão visual 1.0.0 | `nivel-de-criticidade-guia-rapido-padrao-v1.0.0.pdf` |
