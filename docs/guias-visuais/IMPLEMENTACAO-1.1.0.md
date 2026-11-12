# Implementação · Padrão Visual 1.1.0

**Data:** 12/11/2026
**Estado:** versão vigente da evolução cromática.
**Referência:** [Padrão Visual da Biblioteca de Skills](README.md).

## Alterações

O gerador usa a cor institucional de cada arquivo de conteúdo no cabeçalho principal e compacto, títulos funcionais, destaques do conteúdo adicional e link final. Todo texto do cabeçalho usa branco. O validador confere contraste e compara as cores registradas com as do cabeçalho e dos títulos e link do PDF. Os arquivos antigos sem a chave continuam geráveis com o verde histórico.

As superfícies fixas, as fontes, o layout, a paginação, as conversas e o processo de geração do Tagged PDF continuam com o mesmo template. Os guias Delegation e Criticidade conservam conteúdo e geometria. O guia Governance usa o componente textual de demonstração e distingue os quatro papéis conforme seu `SKILL.md`.

## Verificações

| Skill | Cor | Branco | Papel | Realce claro | A4 | Blocos semânticos | Artefatos |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Delegation Context Skill | `#143B36` | 12,29:1 | 11,44:1 | 10,65:1 | 1 pág. | 39 | 16 |
| Agentic Workflow Governance | `#233D63` | 10,94:1 | 10,18:1 | 9,48:1 | 1 pág. | 33 | 15 |
| Nível de Criticidade | `#59273F` | 11,75:1 | 10,94:1 | 10,18:1 | 1 pág. | 38 | 12 |

- **Renderização:** as três páginas foram renderizadas com Poppler e revisadas visualmente. Foi gerada também uma prévia de 390 px com PyMuPDF. O A4 pode exigir zoom em telas estreitas.
- **Regressão:** nos guias Delegation e Criticidade, PyMuPDF confirmou igualdade de texto, fontes e coordenadas, igualdade de pixels na conversa e os mesmos destinos dos links da v1.0.0.
- **Reprodução:** a segunda geração de cada guia produziu a mesma imagem de página. O teste de duas páginas confirmou a cor azul no cabeçalho compacto e o link na última página.
- **Rejeição:** valores inválidos ou claros foram rejeitados, assim como um PDF cuja cor do cabeçalho divergia da configuração.
- **Acessibilidade estrutural:** o validador confirmou PDF 1.7 etiquetado, idioma `pt-BR`, hierarquia de títulos, ordem de leitura, texto pesquisável, artefatos decorativos e um link estruturado em cada guia. As verificações foram estruturais e visuais, sem certificação formal PDF/UA ou teste com leitor de tela.

## Registro

Os guias vigentes estão em **Meu Drive / Skills**. Os PDFs da v1.0.0 foram preservados como histórico. As versões funcionais permanecem 1.1.0 para Delegation e Criticidade e 2.0.0 para Governance.

- `delegation-context-skill-guia-rapido-padrao-v1.1.0.pdf`
- `agentic-workflow-governance-guia-rapido-padrao-v1.1.0.pdf`
- `nivel-de-criticidade-guia-rapido-padrao-v1.1.0.pdf`
