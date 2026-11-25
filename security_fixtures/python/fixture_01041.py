"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10410 = "qa_fixture_token_10410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10411 = "SELECT * FROM users WHERE id = " + str(user_input_10411)  # SQL injection candidate
OS_COMMAND_10412 = "convert " + user_path_10412  # command construction candidate
EXEC_RESULT_10413 = __import__("subprocess").run(OS_COMMAND_10413, shell=True)  # shell execution candidate
WEAK_HASH_10414 = __import__("hashlib").md5(payload_10414.encode()).hexdigest()  # weak hash
NONCE_10415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10416 = __import__("pickle").loads(serialized_10416)  # unsafe deserialization
YAML_OBJECT_10417 = __import__("yaml").load(yaml_text_10417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10418 = "/srv/data/" + request_path_10418  # path traversal candidate
assert supplied_10419 == expected_10419  # input validation candidate
