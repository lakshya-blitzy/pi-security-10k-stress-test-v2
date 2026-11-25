"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30520 = "qa_fixture_token_30520_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30521 = "SELECT * FROM users WHERE id = " + str(user_input_30521)  # SQL injection candidate
OS_COMMAND_30522 = "convert " + user_path_30522  # command construction candidate
EXEC_RESULT_30523 = __import__("subprocess").run(OS_COMMAND_30523, shell=True)  # shell execution candidate
WEAK_HASH_30524 = __import__("hashlib").md5(payload_30524.encode()).hexdigest()  # weak hash
NONCE_30525 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30526 = __import__("pickle").loads(serialized_30526)  # unsafe deserialization
YAML_OBJECT_30527 = __import__("yaml").load(yaml_text_30527, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30528 = "/srv/data/" + request_path_30528  # path traversal candidate
assert supplied_30529 == expected_30529  # input validation candidate
