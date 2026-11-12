# Relatório comparativo · Padrão Visual 1.2.0

**Data:** 12/11/2026
**Estado:** versão vigente.
**Referência:** [especificação editorial e visual](README.md).

## Diagnóstico e decisões

| Eixo | v1.1.0 | Decisão na v1.2.0 |
| --- | --- | --- |
| Editorial | Governance descrevia papéis, com pouco sobre autonomia, escalada e parada. Delegation mostrava campos sem distinguir seus destinatários nem explicar bloqueios. Criticidade tinha pouco espaço para explicar autoridade e concordância. | Governance inclui exemplos de autonomia, escalada e parada. Delegation distingue a informação para o Operador do comando para o Executor e explica quando aguardar. Criticidade explicita que o rigor mantém a autoridade e pode confirmar uma decisão. |
| Composição | O rodapé fixo preservava respiro, mas faltava um local para orientação breve depois da demonstração. | Adicionado o bloco opcional `orientacao`, respeitando a área útil. Tamanhos, margens, cores e paginação preservados. |
| Gráfico | A faixa numerada de Governance nomeava os papéis, mas podia sugerir uma fila obrigatória. Os SVGs existentes eram ícones de identificação e não explicavam autoridade. | Reuso da faixa de cards com setas vetoriais e descrição da hierarquia. A ordem permanece interpretável por texto e lista etiquetada. Ícones e imagens externas foram dispensados. |
| Redundância | Governance repetia os quatro papéis em dois blocos. A escala aparecia nas duas respostas de Criticidade. | A demonstração de Governance foi condensada para abrir espaço às decisões. Em Criticidade, a escala foi mantida nas duas sinalizações porque o `SKILL.md` exige um resumo em cada ativação ou mudança demonstrada. |

O diagnóstico usou os três PDFs da v1.1.0, seus JSONs, os três `SKILL.md`, o gerador, o validador, a especificação e os assets no commit `8fa4471`. Detalhes de implementação das Skills ficaram na documentação técnica.

## Validação

| Guia | Páginas A4 | Blocos semânticos | Artefatos | Contraste do cabeçalho | Respiro antes da divisória, v1.1 → v1.2 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Delegation Context Skill | 1 | 40 | 16 | 12,29:1 | 86 → 22 pt |
| Agentic Workflow Governance | 1 | 35 | 14 | 10,94:1 | 154 → 67 pt |
| Nível de Criticidade | 1 | 38 | 12 | 11,75:1 | 27 → 27 pt |

O respiro foi medido entre o último bloco de texto acima do rodapé e sua divisória. É um indicador de revisão, sem meta de ocupação. Os casos adicionais de Governance e Delegation esclarecem condutas que faltavam. Criticidade permaneceu com densidade equivalente.

- **Visual:** páginas renderizadas com Poppler e prévias de 390 px com PyMuPDF. A comparação por pixels com a v1.1.0 confirmou igualdade no cabeçalho, nos três cards e no rodapé. O A4 pode exigir zoom em tela estreita.
- **Reprodução:** segunda geração com os mesmos JSONs produziu a mesma imagem de cada página. A variante de duas páginas passou, com 40 blocos semânticos e link na última página.
- **Acessibilidade estrutural:** pypdf e PyMuPDF conferiram etiquetas, ordem de leitura, texto pesquisável, idioma, contraste e links. A legenda do diagrama é texto pesquisável e os papéis aparecem na ordem da lista. As setas foram marcadas como artefatos. Gerador e validador rejeitaram o diagrama sem descrição.
- **Limites:** a verificação não incluiu leitores de tela nem certificação formal PDF/UA. O suporte gráfico implementado é linear. Ramificações e figuras informativas independentes requerem extensão e validação quando necessárias.

## Artefatos vigentes

As fontes estão em [conteudo/](conteudo/), com [gerador](gerar.py) e [validador](validar.py). Os PDFs estão em **Meu Drive / Skills**. As versões funcionais e os arquivos históricos foram preservados.

- `delegation-context-skill-guia-rapido-padrao-v1.2.0.pdf` · Skill 1.1.0
- `agentic-workflow-governance-guia-rapido-padrao-v1.2.0.pdf` · Skill 2.0.0
- `nivel-de-criticidade-guia-rapido-padrao-v1.2.0.pdf` · Skill 1.1.0
