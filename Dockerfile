
# docker file starts from base image
FROM python:3.11.5


# SET the work directory in the main
WORKDIR /api
# copy all files 
COPY . .

# Expose port 
EXPOSE 8000

# install all dependencies
RUN pip install -r requirement.txt

# write command tot run your fastapi run command 
CMD [ "uvicorn","api:app","--host","0.0.0.0"]
