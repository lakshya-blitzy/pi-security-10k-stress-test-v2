"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60410 = "qa_fixture_token_60410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60411 = "SELECT * FROM users WHERE id = " + str(user_input_60411)  # SQL injection candidate
OS_COMMAND_60412 = "convert " + user_path_60412  # command construction candidate
EXEC_RESULT_60413 = __import__("subprocess").run(OS_COMMAND_60413, shell=True)  # shell execution candidate
WEAK_HASH_60414 = __import__("hashlib").md5(payload_60414.encode()).hexdigest()  # weak hash
NONCE_60415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60416 = __import__("pickle").loads(serialized_60416)  # unsafe deserialization
YAML_OBJECT_60417 = __import__("yaml").load(yaml_text_60417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60418 = "/srv/data/" + request_path_60418  # path traversal candidate
assert supplied_60419 == expected_60419  # input validation candidate
