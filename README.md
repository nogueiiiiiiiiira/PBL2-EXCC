# 🏠 Sistema de Casa Inteligente com Flask

Este projeto é uma **aplicação web desenvolvida em Flask** que simula o controle de uma casa inteligente, permitindo o gerenciamento de usuários, sensores, atuadores, integração com MQTT para comunicação em tempo real, upload de arquivos e tratamento de erros.

---

## 📋 Funcionalidades Principais

### ✅ **Autenticação e Gerenciamento de Usuários**
- Login com validação de credenciais
- Cadastro, listagem e remoção de usuários
- Controle de acesso via `flask_login`

### 🎛️ **Gerenciamento de Dispositivos**
- **Sensores**: Cadastro, listagem e remoção
- **Atuadores**: Cadastro, listagem e remoção
- Interface web para controle dos dispositivos

### 📡 **Comunicação MQTT em Tempo Real**
- Conexão com broker MQTT (`mqtt-dashboard.com` ou broker local)
- Subscribe no tópico `/aula_flask/`
- Publicação de mensagens para controle de dispositivos
- Interface em tempo real para monitoramento de sensores

### 🖼️ **Upload de Arquivos**
- Upload de imagens para o diretório `static/img/`
- Interface simples com formulário HTML

### ⚠️ **Tratamento de Erros**
- Páginas personalizadas para erros HTTP (404, 401, 405, etc.)
- Redirecionamento adequado para melhor experiência do usuário

### 🎨 **Templates com Jinja2**
- Sistema de herança de templates com `base.html`
- Organização modular do código HTML
- Passagem de dados dinâmicos (listas e dicionários) para as views

---

## 🔧 Tecnologias Utilizadas

- **Flask** - Framework web principal
- **Flask-Login** - Gerenciamento de sessões de usuário
- **Flask-MQTT** - Integração com protocolo MQTT
- **Flask-SocketIO** - Comunicação em tempo real
- **Jinja2** - Sistema de templates
- **Werkzeug** - WSGI toolkit
- **uWSGI** - Servidor de aplicação (opcional para produção)

---

## 🚀 Como Executar

### 1. **Instalação das Dependências**
```bash
pip install flask flask-login flask-mqtt flask-socketio
```

### 2. **Execução da Aplicação**
```bash
python app.py
```

### 3. **Acesso à Aplicação**
```
http://localhost:8080
```

---

## 📊 Fluxo da Aplicação

1. **Login** → Usuário faz autenticação no sistema
2. **Dashboard** → Acesso ao menu principal com todas as funcionalidades
3. **Gerenciamento** → Cadastro/listagem/remoção de usuários, sensores e atuadores
4. **MQTT** → Monitoramento em tempo real e controle de dispositivos
5. **Upload** → Envio de arquivos para o servidor
6. **Tratamento de Erros** → Páginas personalizadas para situações de erro

---

## 🔌 Integração MQTT

### **Configuração do Broker**
```python
app.config['MQTT_BROKER_URL'] = 'mqtt-dashboard.com'  # Broker público
app.config['MQTT_BROKER_PORT'] = 1883
```

### **Funcionalidades MQTT**
- **Subscribe**: Recebe dados de sensores em tempo real
- **Publish**: Envia comandos para atuadores (ex: ligar/desligar LED)
- **Tópicos**: `/aula_flask/` para comunicação geral

---

## 🎯 Casos de Uso

### **Para Estudantes**
- Aprender desenvolvimento web com Flask
- Entender comunicação MQTT em aplicações IoT
- Praticar conceitos de autenticação e sessões
- Desenvolver interfaces com templates Jinja2

### **Para Projetos IoT**
- Controlar sensores e atuadores remotamente
- Monitorar dados em tempo real
- Gerenciar múltiplos usuários e dispositivos

---

Este projeto serve como **base completa** para o desenvolvimento de sistemas de casas inteligentes, combinando conceitos de web development, IoT e comunicação em tempo real de forma prática e educativa. 🏡✨