FROM node:6.5

MAINTAINER Jeeva S. Chelladhurai

COPY src /src/
WORKDIR /src/

RUN npm install restify

ENTRYPOINT ["node", "restapiserver.js"]
