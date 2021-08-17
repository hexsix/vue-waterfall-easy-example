FROM node:10
ENV TZ Asia/Shanghai
COPY ./ /app
WORKDIR /app
RUN npm install && npm run build

FROM nginx
ENV TZ Asia/Shanghai
RUN mkdir /app
COPY --from=0 /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
