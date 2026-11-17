# 🛡️ DIO Agent - Especialização em Cibersegurança & AppSec

Repositório evoluído a partir do projeto base [DIO Agent](https://github.com/digitalinnovationone/dio-agent), especializado para atuar como um **mentor de cibersegurança e AppSec** metódico e analítico.

---

## 🚀 Sobre a Especialização
Nesta evolução, o agente deixa de fornecer respostas diretas ou automatizadas de forma irresponsável. Ele foi configurado para adotar uma postura defensiva e pedagógica, que:
1. **Exige contexto** do ambiente, escopo e criticidade antes de sugerir qualquer ação.
2. Realiza uma **análise de risco estruturada**, avaliando:
   - **Vulnerabilidade** (a falha conceitual).
   - **Impacto** (o dano potencial).
   - **Probabilidade** (a facilidade de exploração).
   - **Severidade** (nível de criticidade).
3. Orienta correções seguras baseadas em frameworks de mercado (como OWASP Top 10 e MITRE ATT&CK).

---

## 📂 Arquivos Criados e Alterados

* **`skills/vulnerability-analysis/SKILL.md`**: Define as diretrizes e regras de comportamento do agente para a análise de falhas.
* **`skills/vulnerability-analysis/README.md`**: Documentação explicativa da skill para humanos.
* **`agent/knowledge/security-basics.md`**: Base conceitual de segurança (Vulnerabilidade, Ameaça, Risco e Tríade CIA).
* **`agent/persona.md`**: Ajustado para moldar o agente como um mentor sênior de segurança defensiva.
* **`AGENTS.md`**: Atualizado com o registro da nova skill na tabela de mapeamento.
* **`app.py`**: Script de laboratório contendo uma falha de login vulnerável a SQL Injection para testes práticos.

---

## 🔬 Evidências e Testes (Lab)

### 1. Cenário Vulnerável (`app.py`)
O script simula uma consulta de autenticação utilizando concatenação direta de strings, permitindo o bypass de login através de SQL Injection clássico (`' OR '1'='1`).
* **Print da Execução / Análise:** ![Estrutura do Projeto](imagens/estrutura-projeto.png)
![Teste de SQL Injection](imagens/teste-sql-injection.png)

### 2. Postura Analítica do Agente
Ao receber o código vulnerável, o agente especializado pausa, solicita o contexto e estrutura a avaliação de risco antes de propor a refatoração segura com consultas parametrizadas.

---

## 🛠️ Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/nome-do-repositorio.git
   cd nome-do-repositorio