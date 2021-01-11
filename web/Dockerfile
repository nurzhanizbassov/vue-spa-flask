# Config with hot reload
# TODO: change this comment
# Also change 'ng serve' to 'ng serve --host 0.0.0.0 --port 4210' in package.json file

FROM node:12.18.0-slim

WORKDIR /web

COPY package*.json ./

RUN npm install -g @vue/cli && npm install

EXPOSE 8088 

CMD ["npm", "start"]

#Config with nginx, but without hot reload

# FROM node:12.18.0-slim as build
# 
# WORKDIR /someapp
# 
# COPY . .
# 
# RUN npm install && npm run build
# 
# FROM nginx:stable
# 
# COPY --from=build /someapp/dist/web /usr/share/nginx/html
# 
# COPY ./nginx.conf /etc/nginx/conf.d/default.conf
