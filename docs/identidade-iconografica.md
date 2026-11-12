# Identidade iconográfica das Skills

**Estado** · Implementação de desenvolvimento. Três identidades em piloto. A versão funcional de cada Skill e o padrão PDF v1.2.0 são independentes do estado da identidade.

## Entrada do fluxo

Na etapa 4 da criação autorizada, prepare a especificação canônica, a entrada usual em `skills.json` e o JSON do guia em `docs/guias-visuais/conteudo/<id>.json`. Leia a finalidade e os limites da Skill. Proponha um conceito que permita reconhecê-la sem sua cor e desenhe uma vez o mestre em `skills/<id>/assets/identity/icone.svg`. Em revisão funcional, conserve o mestre quando o conceito permanecer adequado.

Use SVG autocontido com `viewBox="0 0 24 24"`, largura e altura 24, título descritivo e um path sem preenchimento. O traço é 1,6, com terminações e cantos arredondados. Use a cor já registrada no guia, preserve margem interna e revise a leitura a 16 e 24 px. Reutilize a estrutura de um mestre existente. Para fundo escuro use branco, para fundo claro use a cor institucional e para contexto neutro use a variante monocromática.

Instale as dependências fixadas em `docs/guias-visuais/requirements.txt`, use as fontes do padrão vigente e disponibilize o veraPDF quando houver revisão de publicação. Da raiz, execute:

```sh
python3 scripts/identidade.py prepare <id> --output <pasta-de-previas>
python3 scripts/identidade.py check
python3 tests/validate_catalog.py
python3 -m unittest discover -s tests -p test_identidade.py
```

`prepare` sincroniza variantes SVG, PNG transparente de 512 px, SHA-256 do mestre e do PNG, catálogo visual e trechos marcados de README. Gera os guias e executa o validador interno. Se encontrar veraPDF, executa `ua1`, registra o XML e reprova resultado sem conformidade automatizada. Se estiver indisponível, registra a pendência. `build` atualiza os arquivos de identidade sem gerar guias. `check` somente verifica. Sem IDs, o comando atua sobre todas as entradas. As decisões criativas ficam com o agente encarregado da criação. As tarefas determinísticas passam pelo script.

As prévias são geradas com o ícone piloto. O modo normal do gerador consulta o catálogo e exibe automaticamente identidades aprovadas. O símbolo fica no primeiro cabeçalho, como artefato vetorial decorativo, com o nome em texto. Os PDFs de avaliação devem ficar fora da pasta oficial do Drive.

## Publicação e continuidade

Use uma cópia de trabalho isolada por alteração. Faça commit de mestre, derivados, catálogo e documentação juntos e publique somente no branch autorizado, com atualização que falhe se a referência remota tiver avançado. Em caso de conflito, releia o catálogo remoto, reconcilie alterações e execute `check` novamente. Arquivos locais são trocados individualmente de forma atômica. Se houver interrupção, repita `prepare` na mesma cópia de trabalho antes de qualquer publicação.

Para oficializar, obtenha a decisão do Operador sobre os conceitos, confira a prancha em tamanho reduzido, valide os três guias incluindo o perfil automatizado PDF/UA-1 e revise a diferença do commit. Registre explicitamente `approved` apenas nas identidades autorizadas, execute as verificações novamente e publique nos destinos autorizados. Mudanças posteriores em identidade aprovada são detectadas pelo pipeline e exigem revisão explícita. Os assets legados de interface ficam fora dessa troca. Instalações nativas seguem seu próprio fluxo.

## Recuperação em conversas

Consulte `skills.json` em uma revisão publicada. O par commit e caminho em `icon_png` determina a URL estável, e `asset_sha256` identifica o PNG. Para resolver automaticamente a partir do catálogo da mesma revisão:

```sh
python3 scripts/identidade.py resolve --commit <sha-completo>
python3 scripts/identidade.py verify-remote --commit <sha-completo>
```

Use `--allow-pilot` somente em ensaios autorizados. A revisão informada deve corresponder ao catálogo consultado. Recupere por HTTPS, confira o tipo de conteúdo e a assinatura do arquivo e, quando possível, compare SHA-256. Em superfícies com renderização de arquivos, use o PNG recuperado. Em fundo escuro com SVG disponível, prefira a variante negativa. Quando só houver suporte a PNG, confira o contraste na superfície usada. Se o ambiente não puder carregar ou exibir o asset, use o nome textual.

> Ao apresentar nominalmente uma Skill do ecossistema, consulte o catálogo oficial em Jadsonjg/ecosystem-agent-skills. Exiba o ícone aprovado e recuperado junto ao nome textual quando a interface oferecer suporte. Use a variante adequada ao fundo. Quando faltar acesso, aprovação ou suporte, use somente o nome. Preserve código, comandos, URLs, identificadores e dados estruturados. Não use emojis, símbolos genéricos ou links isolados como substitutos.

A mesma instrução pode ser incorporada à inicialização de agentes, instruções de projetos aderentes ou personalização autorizada. Forneça acesso ao catálogo por meio disponível na superfície. Nenhum desses mecanismos garante a renderização. Metadados nativos de interface são independentes do corpo da resposta.

## Teste integral

**PENDENTE DE TESTE REAL — AGUARDANDO FUTURA DEMANDA DO OPERADOR.** O primeiro teste integral começa quando uma nova Skill real for solicitada e autorizada. Valide sua portabilidade e conclua o fluxo normal de criação e publicação. Para propagação conversacional, teste uma conversa independente que receba a convenção pela configuração e pergunte sobre a Skill sem fornecer arquivo ou URL. Registre separadamente identificação, localização, download, exibição observada e integridade do arquivo.
