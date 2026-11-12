# Correção técnica de XMP · Padrão Visual 1.2.0

**Data:** 12/11/2026
**Escopo:** geração e validação de metadados dos três Guias Rápidos.

A auditoria dos PDFs da v1.2.0 encontrou ausência de XMP em todos os catálogos. O veraPDF reprovou a regra ISO 14289-1:2014, cláusula 7.1, teste 8. A correção mantém a versão do padrão e as versões funcionais das Skills.

- [Gerador](gerar.py) e [metadados](metadados.py) emitem um fluxo `/Metadata` de subtipo `/XML`, com `pdfuaid:part=1` e título `dc:title` em `x-default`, derivado do título Info.
- [Validador](validar.py) confere o tipo do fluxo, XML bem formado, identificador e coerência do título com o guia e o título Info. As verificações estruturais anteriores continuam em execução.
- [Teste de regressão](test_metadados.py) aceita título Unicode com caracteres especiais e rejeita seis casos: XMP ausente, subtipo incorreto, XML malformado, parte PDF/UA incorreta, título XMP incorreto e divergência do título Info.

## Revalidação

| Guia | veraPDF 1.28.2, perfil `ua1` | Regras aprovadas | Verificações aprovadas | Falhas |
| --- | --- | ---: | ---: | ---: |
| Delegation Context Skill | `isCompliant=true` | 106 | 3.955 | 0 |
| Agentic Workflow Governance | `isCompliant=true` | 106 | 3.659 | 0 |
| Nível de Criticidade | `isCompliant=true` | 106 | 3.979 | 0 |

O lote terminou com três resultados conformes ao perfil automatizado, zero falhas de análise e zero exceções. O validador interno passou nos três. A comparação com os PDFs originais confirmados no Drive mostrou pixels idênticos a 72 e 144 dpi, fluxos de conteúdo de página idênticos, o mesmo texto extraído, os mesmos links e a mesma árvore lógica de etiquetas. Os campos Info preservam os valores anteriores, exceto datas de geração.

Os resultados descrevem conformidade com as regras **automatizadas** do perfil executado. A leitura funcional com tecnologia assistiva, a análise de critérios humanos, o PAC e a certificação independente ficaram fora desta correção.

## Reproduzir

```sh
python3 -m unittest -v test_metadados.py
python3 gerar.py conteudo/nivel-de-criticidade.json nivel-de-criticidade.pdf
python3 validar.py conteudo/nivel-de-criticidade.json nivel-de-criticidade.pdf
verapdf --flavour ua1 --format xml nivel-de-criticidade.pdf
```

## Edições corrigidas

Os arquivos com sufixo `-v1.2.0-xmp.pdf` em **Meu Drive / Skills** são as edições corrigidas. As edições originais permanecem disponíveis para histórico e reprodução da auditoria inicial.

| Arquivo corrigido | SHA-256 |
| --- | --- |
| `delegation-context-skill-guia-rapido-padrao-v1.2.0-xmp.pdf` | `94b64e2bf1d48793c3cc985035e4c7e3c2d68009e7a3687a0c1376e1197fdb80` |
| `agentic-workflow-governance-guia-rapido-padrao-v1.2.0-xmp.pdf` | `b4f441414a447bc10b8338e60546d412a32228888ea8e6c79b601f0f9085ddf4` |
| `nivel-de-criticidade-guia-rapido-padrao-v1.2.0-xmp.pdf` | `e39464cd57840d6fbc88d225c40c4963a09f8b165fb63e5b049a6cdec6628297` |
