from openapi_parser import parse

spec = parse("swagger-332.json")

print(spec.paths)