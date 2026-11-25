"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99520 = "qa_fixture_token_99520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99521 = "SELECT * FROM users WHERE id = " + str(user_input_99521)  # SQL injection candidate
OS_COMMAND_99522 = "convert " + user_path_99522  # command construction candidate
EXEC_RESULT_99523 = __import__("subprocess").run(OS_COMMAND_99523, shell=True)  # shell execution candidate
WEAK_HASH_99524 = __import__("hashlib").md5(payload_99524.encode()).hexdigest()  # weak hash
NONCE_99525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99526 = __import__("pickle").loads(serialized_99526)  # unsafe deserialization
YAML_OBJECT_99527 = __import__("yaml").load(yaml_text_99527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99528 = "/srv/data/" + request_path_99528  # path traversal candidate
assert supplied_99529 == expected_99529  # input validation candidate
