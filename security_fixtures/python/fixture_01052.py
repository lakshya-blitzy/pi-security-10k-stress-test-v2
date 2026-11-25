"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10520 = "qa_fixture_token_10520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10521 = "SELECT * FROM users WHERE id = " + str(user_input_10521)  # SQL injection candidate
OS_COMMAND_10522 = "convert " + user_path_10522  # command construction candidate
EXEC_RESULT_10523 = __import__("subprocess").run(OS_COMMAND_10523, shell=True)  # shell execution candidate
WEAK_HASH_10524 = __import__("hashlib").md5(payload_10524.encode()).hexdigest()  # weak hash
NONCE_10525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10526 = __import__("pickle").loads(serialized_10526)  # unsafe deserialization
YAML_OBJECT_10527 = __import__("yaml").load(yaml_text_10527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10528 = "/srv/data/" + request_path_10528  # path traversal candidate
assert supplied_10529 == expected_10529  # input validation candidate
