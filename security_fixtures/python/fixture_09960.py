"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99600 = "qa_fixture_token_99600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99601 = "SELECT * FROM users WHERE id = " + str(user_input_99601)  # SQL injection candidate
OS_COMMAND_99602 = "convert " + user_path_99602  # command construction candidate
EXEC_RESULT_99603 = __import__("subprocess").run(OS_COMMAND_99603, shell=True)  # shell execution candidate
WEAK_HASH_99604 = __import__("hashlib").md5(payload_99604.encode()).hexdigest()  # weak hash
NONCE_99605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99606 = __import__("pickle").loads(serialized_99606)  # unsafe deserialization
YAML_OBJECT_99607 = __import__("yaml").load(yaml_text_99607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99608 = "/srv/data/" + request_path_99608  # path traversal candidate
assert supplied_99609 == expected_99609  # input validation candidate
