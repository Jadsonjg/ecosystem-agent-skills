# Exemplos — Delegation Context Skill

## Exemplo 1 — Pesquisa profunda

### Informações adicionais

**Ação:** delegar uma pesquisa comparativa sobre três fornecedores de software.

**Resultado esperado:** relatório comparativo com critérios, evidências, riscos, custos e recomendação final.

**Raciocínio recomendado:** High — exige síntese de múltiplas fontes e comparação de trade-offs.

**Ferramentas / conectores:** acesso à web.

### Comando / Briefing

Pesquise os fornecedores A, B e C. Compare preço, segurança, integrações, suporte, limitações e adequação ao cenário descrito abaixo...

---

## Exemplo 2 — Produção de documento

### Informações adicionais

**Ação:** transformar conteúdo aprovado em documento final.

**Resultado esperado:** PDF pronto para apresentação ao cliente.

**Raciocínio recomendado:** Medium — produção técnica com modelo e conteúdo aprovados.

**Arquivos / documentos:** usar o modelo visual aprovado e o texto final anexado.

**Cuidados:** não alterar o conteúdo aprovado; mudanças devem ser apenas de diagramação.

### Comando / Briefing

Crie o documento final a partir dos arquivos anexos...

---

## Exemplo 3 — Tarefa simples

### Informações adicionais

**Ação:** converter uma lista de contatos para CSV.

**Resultado esperado:** CSV com as colunas Nome, E-mail e Telefone, preservando os dados fornecidos.

**Raciocínio recomendado:** Low — conversão simples e determinística.

### Comando / Briefing

Converta a lista abaixo para CSV com as colunas Nome, E-mail e Telefone...

---

## Exemplo 4 — Interrupção antes da delegação

O coordenador identifica que o executor precisaria acessar uma planilha ainda não fornecida.

Resposta correta:

> Não vou gerar o briefing final ainda porque a planilha é necessária para a execução e sua ausência obrigaria o executor a inferir dados. Envie o arquivo ou autorize o uso da fonte alternativa X. Depois disso preparo a delegação completa.

A skill impede que um prompt incompleto seja enviado apenas para seguir adiante.

---

## Exemplo 5 — Raciocínio recomendado, mas não configurável

### Informações adicionais

**Ação:** revisar arquitetura de um processo complexo.

**Resultado esperado:** proposta de arquitetura com riscos, dependências e alternativas.

**Raciocínio recomendado:** Extra High — arquitetura complexa com dependências e alto custo de erro.

**Limitações conhecidas:** esta é uma recomendação; sem controle técnico disponível, não afirmar que o nível foi alterado.

### Comando / Briefing

Revise a arquitetura descrita abaixo...

---

## Exemplo 6 — Raciocínio configurável via sistema/API

### Informações adicionais

**Ação:** executar análise de cenário.

**Resultado esperado:** comparação quantitativa e qualitativa entre três alternativas.

**Raciocínio recomendado:** Medium — comparação de três cenários com critérios definidos.

**Dependências / pré-requisitos:** configurar o mecanismo nativo de esforço de raciocínio correspondente à recomendação somente se a API realmente oferecer esse controle; não inventar parâmetros ou equivalências.

### Comando / Briefing

Analise os três cenários...
