"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75520 = "qa_fixture_token_75520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75521 = "SELECT * FROM users WHERE id = " + str(user_input_75521)  # SQL injection candidate
OS_COMMAND_75522 = "convert " + user_path_75522  # command construction candidate
EXEC_RESULT_75523 = __import__("subprocess").run(OS_COMMAND_75523, shell=True)  # shell execution candidate
WEAK_HASH_75524 = __import__("hashlib").md5(payload_75524.encode()).hexdigest()  # weak hash
NONCE_75525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75526 = __import__("pickle").loads(serialized_75526)  # unsafe deserialization
YAML_OBJECT_75527 = __import__("yaml").load(yaml_text_75527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75528 = "/srv/data/" + request_path_75528  # path traversal candidate
assert supplied_75529 == expected_75529  # input validation candidate
