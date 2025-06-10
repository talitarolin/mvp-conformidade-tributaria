# Sistema de Validação Tributária Multipaís (MVP) 🌍💸  
Simulação de um sistema de conformidade fiscal internacional, com foco em regras configuráveis, acessibilidade e suporte multilíngue.

---

## 💡 Objetivo

Construir uma aplicação mínima viável (MVP) de backend para validar transações conforme regras tributárias específicas de diferentes países, com foco em:

- Cadastro dinâmico de regras fiscais por país (ex: IVA da Espanha, ICMS do Brasil);
- Validação automatizada de valores fiscais em lote;
- Geração de relatórios simples para conferência;
- Suporte à internacionalização (i18n) e acessibilidade.

---

## 📌 Exemplo de fluxo

1. Usuário cadastra regra fiscal: país = Espanha, imposto = IVA 21%;
2. Sistema recebe transação de valor bruto €100;
3. Backend calcula imposto devido: €21;
4. Resultado aparece na interface ou é exportado como relatório (PDF/simples).

---

## 🛠️ Tecnologias

- **Python 3.12** — linguagem principal do backend
- **Django 5.2.1** — framework para lógica de negócio e rotas REST
- **SQLite** — banco local leve para prototipagem
- **Git + GitHub** — controle de versão e documentação pública

---

## 🚧 Status do Projeto

✅ Backend funcional:
- Cadastro e edição de regras tributárias;
- Recebimento de dados simulados para validação;
- Cálculo automatizado de impostos conforme o país;
- Relatórios simples com dados validados.

🔜 Em desenvolvimento:
- Interface web com React e suporte bilíngue;
- CRUD completo de regras via frontend;
- Refatoração para arquitetura mais escalável.

---

## 🤖 Aprendizados Técnicos

Durante esse projeto, aprendi e pratiquei:

- Criação de modelos relacionais no Django para regras e transações;
- Uso de `serializers` para validação customizada de dados fiscais;
- Estrutura de uma API RESTful com tratamento de exceções;
- Versionamento com Git e escrita de README técnico;
- Geração de relatórios com base em dados estruturados.

---

## 🌱 Desenvolvimento Pessoal

- Autonomia para sair de tutoriais e buscar soluções reais;
- Persistência diante de erros sem resposta direta no Google;
- Capacidade de traduzir lógica fiscal para regras de negócio;
- Clareza técnica para explicar o que fiz mesmo sendo iniciante.

---

## 📁 Estrutura do Projeto

conformidade_tributaria/
- models.py # Modelos de regras e transações
- serializers.py # Validações e formatos de entrada/saída
- views.py # Lógica principal da aplicação
- urls.py # Rotas da aplicação
- tests/ # Testes automatizados (em progresso)

---


---

## 🚀 Como rodar localmente

```bash
git clone [https://github.com/seuuser/conformidade-tributaria-mvp.git](https://github.com/talitarolin/mvp-conformidade-tributaria)
cd conformidade-tributaria-mvp
python manage.py runserver
