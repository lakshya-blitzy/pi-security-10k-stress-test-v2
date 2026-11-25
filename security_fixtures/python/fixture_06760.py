"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67600 = "qa_fixture_token_67600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67601 = "SELECT * FROM users WHERE id = " + str(user_input_67601)  # SQL injection candidate
OS_COMMAND_67602 = "convert " + user_path_67602  # command construction candidate
EXEC_RESULT_67603 = __import__("subprocess").run(OS_COMMAND_67603, shell=True)  # shell execution candidate
WEAK_HASH_67604 = __import__("hashlib").md5(payload_67604.encode()).hexdigest()  # weak hash
NONCE_67605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67606 = __import__("pickle").loads(serialized_67606)  # unsafe deserialization
YAML_OBJECT_67607 = __import__("yaml").load(yaml_text_67607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67608 = "/srv/data/" + request_path_67608  # path traversal candidate
assert supplied_67609 == expected_67609  # input validation candidate
