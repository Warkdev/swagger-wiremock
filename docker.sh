docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v332 -t stoplight/prism mock -h 0.0.0.0 /root/apis/swagger-332.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v35 -t stoplight/prism mock -h 0.0.0.0 /root/apis/swagger-35.yml
docker run -it -d -p 8443:443 -v ~/swagger-wiremock/nginx:/etc/nginx/conf.d:ro --name web_proxy nginx