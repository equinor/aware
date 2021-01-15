FROM node:12-alpine
RUN npm install -g serve
WORKDIR /code

ADD package.json yarn.lock /code/
RUN yarn install --frozen-lockfile
ADD public /code/public
ADD src /code/src

RUN yarn build
EXPOSE 3000
CMD ["serve", "-s", "build"]
