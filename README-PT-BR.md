# Telegram Message Mirror Bot 🔄

Script de automação desenvolvido em Python utilizando a biblioteca Telethon, projetado para espelhar mensagens de forma assíncrona entre canais e grupos do Telegram.

## 🚀 Funcionalidades

*   **Espelhamento 1-para-1:** Lê de uma origem e envia instantaneamente para um destino.
*   **Recuperação de Histórico:** Se executado do zero, o bot copia todo o histórico passado em ordem cronológica.
*   **Memória Persistente:** Se o computador for desligado, o bot grava a última mensagem lida e recomeça exatamente de onde parou.
*   **Suporte a Fóruns (Tópicos):** Identifica se o grupo de origem possui tópicos/subgrupos, cria as mesmas abas automaticamente no grupo de destino e encaminha os conteúdos para o local correto.
*   **Anti-Banimento Nativo:** Sistema de filas e atrasos (delays) estruturados para mimetizar comportamento humano e respeitar o *Rate Limit* do Telegram.

## ⚙️ Instalação e Uso

1. Clone o repositório para o seu computador.
2. Instale os requisitos através do comando:
   ```bash
   pip install -r requirements.txt
   ```
3. Abra o arquivo `bot.py` e insira suas credenciais do Telegram (`API_ID`, `API_HASH`) obtidas no site oficial my.telegram.org.
4. Configure as variáveis `CANAL_ORIGEM` e `CANAL_DESTINO` com o @username ou o ID numérico correspondente.
5. Execute o script:
   ```bash
   python bot.py
   ```

## 🔑 Como obter suas Credenciais e IDs

Para que o bot funcione corretamente, você precisará preencher algumas variáveis no arquivo `bot.py`. Siga os passos abaixo para encontrar essas informações:

### 1. Obtendo `API_ID` e `API_HASH`
Estas credenciais identificam o seu script junto aos servidores do Telegram.
1. Acesse o portal oficial para desenvolvedores: [my.telegram.org](https://my.telegram.org).
2. Faça login informando o seu número de telefone (com código do país, ex: `+5511...`) e o código recebido no seu aplicativo do Telegram.
3. Clique em **API development tools**.
4. Se for a primeira vez, preencha o formulário para criar um novo aplicativo (o nome e a plataforma podem ser qualquer um, por exemplo: *MeuApp* e *Desktop*).
5. Copie os valores que aparecerão na tela: **`App api_id`** (um número curto) e **`App api_hash`** (uma sequência longa de letras e números).

### 2. Obtendo `CANAL_ORIGEM` e `CANAL_DESTINO`
A forma de preencher essas variáveis depende da privacidade do canal ou grupo.
*   **Para Canais/Grupos PÚBLICOS:**
    *   Basta usar o link de convite ou nome de usuário da página.
    *   *Como colocar no código:* `CANAL_ORIGEM = '@nome_do_canal'` (Sempre entre aspas e com a arroba).
*   **Para Canais/Grupos PRIVADOS:**
    *   Canais privados não possuem `@username`. Você precisará do **ID numérico** escondido.
    *   Abra o [Telegram Web](https://web.telegram.org) no navegador do seu computador.
    *   Acesse o canal ou grupo desejado.
    *   Olhe para a **barra de endereços do seu navegador**. Você verá uma URL parecida com esta: `https://web.telegram.org/a/#-1001234567890`.
    *   Copie a sequência numérica inteira, **incluindo o sinal de menos e o 100** (ex: `-1001234567890`).
    *   *Como colocar no código:* `CANAL_ORIGEM = -1001234567890` (Por ser um número inteiro, **NÃO use aspas**).

## 👤 Autoria e desenvolvimento
Script de automação desenvolvido de forma independente por Pablo Phillipe Cândido dos Santos, destinado ao espelhamento contínuo de mensagens entre canais e grupos do Telegram. A ferramenta permite a cópia de histórico pregresso e o encaminhamento em tempo real, com suporte à criação e roteamento automático de subgrupos (tópicos de fórum), garantindo a fidelidade e organização no local de destino.

O desenvolvimento contou com a utilização de ferramentas de inteligência artificial generativa como recurso auxiliar no processo de desenvolvimento, mantendo-se sob responsabilidade do autor a concepção, implementação, integração e verificação do projeto.

**Currículo Lattes:** http://lattes.cnpq.br/9500873674712528
