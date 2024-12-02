# Use uma imagem base com Python
FROM python:3.9.2-slim

# Defina o diretório de trabalho no container
WORKDIR /app

# Copie os arquivos do projeto para o container
COPY . /app/

# # Instale as dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


# # Exponha a porta para o Django (8000)
EXPOSE 8000

# # Comando para rodar o servidor
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

