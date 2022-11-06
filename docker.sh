docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v332 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-332.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v35 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-35.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v36 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-36.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v37 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-37.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v38 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-38.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v39 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-39.yml
docker run -it --rm -v ~/swagger-wiremock:/root/apis --name prism_axway_cft_v310 -t stoplight/prism mock -h 0.0.0.0 /root/apis/openapi-310.yml
docker run -it -d -p 8443:443 -v ~/swagger-wiremock/nginx:/etc/nginx/conf.d:ro --name web_proxy nginx