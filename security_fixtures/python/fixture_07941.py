"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79410 = "qa_fixture_token_79410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79411 = "SELECT * FROM users WHERE id = " + str(user_input_79411)  # SQL injection candidate
OS_COMMAND_79412 = "convert " + user_path_79412  # command construction candidate
EXEC_RESULT_79413 = __import__("subprocess").run(OS_COMMAND_79413, shell=True)  # shell execution candidate
WEAK_HASH_79414 = __import__("hashlib").md5(payload_79414.encode()).hexdigest()  # weak hash
NONCE_79415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79416 = __import__("pickle").loads(serialized_79416)  # unsafe deserialization
YAML_OBJECT_79417 = __import__("yaml").load(yaml_text_79417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79418 = "/srv/data/" + request_path_79418  # path traversal candidate
assert supplied_79419 == expected_79419  # input validation candidate
