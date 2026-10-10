# 🔒 Projeto Base: Autenticação e Autorização no Django

Este projeto serve como exemplo prático para:

- Sistema de login e logout usando Django Auth
- Proteção de páginas com `LoginRequiredMixin`
- Templates de login e painel protegidos

## 🚀 Atividade proposta

Crie seu próprio projeto Django usando:

## 🎯 Tema: **Área Restrita de Funcionários**

- App `funcionarios`
- Crie usuários via Admin para simular funcionários
- Criar views:
  - Painel geral (visível apenas para funcionários logados)
  - Página de perfil do funcionário (usando o `request.user`)

- Implementar:
  - Login
  - Logout
  - Proteção de páginas com `LoginRequiredMixin`
  - Controle de acesso no template (`{% if user.is_authenticated %}`)
  - Página pública separada para visitantes não logados (Home pública)

### 📤 Entrega

- Subir no GitHub ou enviar ZIP com:
  - Código fonte do projeto
  - Prints do funcionamento (opcional)

---

## 🤝 **Dúvidas?**

Caso tenha dúvidas, entre em contato pelo **Discord** ou pelo e-mail do professor. Bons estudos e divirta-se! 🐍
