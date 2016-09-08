FROM python:3.5
RUN pip install flask bcrypt markdown PyRSS2Gen html2text
ADD . /src
EXPOSE 5000
