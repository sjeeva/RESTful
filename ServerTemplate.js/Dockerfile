FROM node

MAINTAINER Jeeva S. Chelladhurai

COPY src /src/
WORKDIR /src/

RUN npm install restify

ENTRYPOINT ["node", "restapiserver.js"]
