# Using NGINX for mirroring RESTful calls between servers

## Running the sample

`docker-compose up --build`

## Testing

From another window, execute:

`curl localhost/endpoint`

Expected result on the `docker-compose` window:

```
request-mirroring-flask1-1  | 172.21.0.4 - - [20/Jan/2024 08:31:39] "GET /endpoint HTTP/1.0" 200 -
request-mirroring-flask2-1  | 172.21.0.4 - - [20/Jan/2024 08:31:39] "GET /endpoint HTTP/1.0" 200 -
request-mirroring-nginx-1   | 172.21.0.1 - - [20/Jan/2024:08:31:39 +0000] "GET /endpoint HTTP/1.1" 200 26 "-" "curl/8.4.0"
```

As can be seen in the above, same end-point is called on both instances

## How does it work?

* The `Flask` application exposes a single endpoint `/endpoint`
* `docker-compose` creates three containers: two for the two instances of the `Flask` application and one for the NGINX server
* The `nginx` server mirrors call to both instances

### Notes on `nginx.conf`

* `resolver` is defined
* `mirror_request_body on` ensures copy of a payload
* `proxy_pass http://flask2:5000$request_uri` ensures copy of the original call path
