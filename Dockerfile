FROM ubuntu:18.04
FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /django


RUN     pip install pytest-asyncio
RUN     pip install selenium
RUN     pip install pytest
RUN     pip install psycopg2-binary
RUN     pip install PyVirtualDisplay
RUN     pip install xvfbwrapper

# add latest stable chrome installation

# Set up the Chrome PPA
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package list and install chrome
RUN apt-get update -y
RUN apt-get install -y google-chrome-stable

RUN apt-get install -y libnss3 libgconf-2-4



# Set up Chromedriver Environment variables
ENV CHROMEDRIVER_VERSION  91.0.4472.101
ENV CHROMEDRIVER_DIR /chromedriver
RUN mkdir $CHROMEDRIVER_DIR

# # # Download and install Chromedriver
RUN wget -q --continue -P $CHROMEDRIVER_DIR "http://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip"
RUN unzip $CHROMEDRIVER_DIR/chromedriver* -d $CHROMEDRIVER_DIR

# # unzip chromedriver_linux64.zip

# # # Put Chromedriver into the PATH
ENV PATH $CHROMEDRIVER_DIR:$PATH


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
