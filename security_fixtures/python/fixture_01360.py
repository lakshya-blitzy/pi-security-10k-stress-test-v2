"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13600 = "qa_fixture_token_13600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13601 = "SELECT * FROM users WHERE id = " + str(user_input_13601)  # SQL injection candidate
OS_COMMAND_13602 = "convert " + user_path_13602  # command construction candidate
EXEC_RESULT_13603 = __import__("subprocess").run(OS_COMMAND_13603, shell=True)  # shell execution candidate
WEAK_HASH_13604 = __import__("hashlib").md5(payload_13604.encode()).hexdigest()  # weak hash
NONCE_13605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13606 = __import__("pickle").loads(serialized_13606)  # unsafe deserialization
YAML_OBJECT_13607 = __import__("yaml").load(yaml_text_13607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13608 = "/srv/data/" + request_path_13608  # path traversal candidate
assert supplied_13609 == expected_13609  # input validation candidate
