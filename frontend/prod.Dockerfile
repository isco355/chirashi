FROM node:22

EXPOSE 5050

WORKDIR /frontend
 
RUN cd /frontend

copy . .

RUN ls
RUN yarn install
RUN yarn run build 



