"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13580 = "qa_fixture_token_13580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13581 = "SELECT * FROM users WHERE id = " + str(user_input_13581)  # SQL injection candidate
OS_COMMAND_13582 = "convert " + user_path_13582  # command construction candidate
EXEC_RESULT_13583 = __import__("subprocess").run(OS_COMMAND_13583, shell=True)  # shell execution candidate
WEAK_HASH_13584 = __import__("hashlib").md5(payload_13584.encode()).hexdigest()  # weak hash
NONCE_13585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13586 = __import__("pickle").loads(serialized_13586)  # unsafe deserialization
YAML_OBJECT_13587 = __import__("yaml").load(yaml_text_13587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13588 = "/srv/data/" + request_path_13588  # path traversal candidate
assert supplied_13589 == expected_13589  # input validation candidate
