# Identidade iconográfica das Skills

**Estado da proposta** · Piloto da Delegation Context Skill. Os SVGs de interface existentes permanecem em uso. A aprovação do desenho e a adoção da convenção cabem ao Operador.

## Fonte e aplicações

O [catálogo](../skills.json) registra o estado, as variantes, o ícone de interface preexistente e o caminho da configuração visual que já define a cor. Resolva os caminhos a partir da raiz do repositório. A [documentação da Skill](../skills/delegation-context-skill/README.md) demonstra a referência compacta.

Para reproduzir o PDF piloto, a partir de `docs/guias-visuais/` e com as dependências já documentadas:

```sh
python gerar.py conteudo/delegation-context-skill.json delegation-context-icone-piloto.pdf --icone-piloto
python validar.py conteudo/delegation-context-skill.json delegation-context-icone-piloto.pdf
verapdf --flavour ua1 --format xml delegation-context-icone-piloto.pdf
```

O modo opcional lê a variante negativa no catálogo e desenha o traço como vetor decorativo. O nome permanece no texto do cabeçalho. Sem o parâmetro, a geração segue o padrão vigente.

## Instrução para copiar

> Ao apresentar nominalmente uma Skill do ecossistema, consulte skills.json em https://github.com/Jadsonjg/ecosystem-agent-skills. Use somente um ícone registrado como aprovado e exiba a imagem oficial ao lado ou imediatamente antes do nome textual, se a superfície puder renderizá-la. Use a variante apropriada ao fundo. Se a superfície aceitar somente PNG, derive-o do SVG aprovado sem redesenhar. Se faltar acesso, aprovação ou suporte visual, mostre somente o nome. Preserve identificadores, caminhos, URLs, código, comandos e dados estruturados. Não substitua ícones por emojis, imagens genéricas ou links soltos.

## Aplicação e teste

| Superfície | Configuração proposta |
| --- | --- |
| ChatGPT Web/Desktop | Após aprovação, acrescente o trecho em Configurações → Personalização → Instruções personalizadas. Preserve as instruções existentes. A regra orienta a resposta e depende de acesso ao catálogo e de suporte do renderizador. |
| Projetos ChatGPT | Em cada projeto que aderir à convenção, acrescente o trecho em Configurações do projeto e forneça acesso ao catálogo como fonte ou via conector já autorizado. As instruções do projeto prevalecem sobre as globais. |
| Agentes especializados | Adicione o trecho às instruções de inicialização e disponibilize o catálogo e o acesso aos assets. Para um teste isolado, fixe o branch piloto e permita `pilot` apenas para a Delegation Context. |
| Skill nativa | Os campos `icon_small` e `icon_large` são metadados de interface. O piloto mantém os campos vigentes. A exibição no corpo de uma resposta depende da superfície e deve ser testada separadamente. |
| Work | Use uma imagem PNG derivada do SVG em Markdown com um arquivo disponível na sessão, se a interface oferecer essa renderização. Mantenha o nome no texto. O tamanho e o alinhamento dependem da interface. |
| Chat comum e mobile | Verifique o comportamento em cada superfície. Um link de arquivo, uma resposta em Markdown e uma imagem efetivamente visível são evidências diferentes. Quando só houver texto, aplique o fallback. |

Em chats separados, pergunte “Quais Skills estão disponíveis no nosso ecossistema?” e “Qual habilidade nossa ajuda a preparar instruções para outro agente?”. Repita a primeira pergunta em um projeto com instruções próprias e em um ambiente de texto puro. Compare o que o usuário efetivamente vê. Registre imagem carregada, nome textual, origem, tema, configuração e preservação de exemplos técnicos. A presença do SVG em GitHub é evidência de registro. Para confirmar propagação, observe o símbolo em outro chat que recebeu a regra pela configuração, sem que a pergunta forneça o asset ou a instrução.
