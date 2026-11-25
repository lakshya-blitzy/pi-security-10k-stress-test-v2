"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17410 = "qa_fixture_token_17410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17411 = "SELECT * FROM users WHERE id = " + str(user_input_17411)  # SQL injection candidate
OS_COMMAND_17412 = "convert " + user_path_17412  # command construction candidate
EXEC_RESULT_17413 = __import__("subprocess").run(OS_COMMAND_17413, shell=True)  # shell execution candidate
WEAK_HASH_17414 = __import__("hashlib").md5(payload_17414.encode()).hexdigest()  # weak hash
NONCE_17415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17416 = __import__("pickle").loads(serialized_17416)  # unsafe deserialization
YAML_OBJECT_17417 = __import__("yaml").load(yaml_text_17417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17418 = "/srv/data/" + request_path_17418  # path traversal candidate
assert supplied_17419 == expected_17419  # input validation candidate
