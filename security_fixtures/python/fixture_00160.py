"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1600 = "qa_fixture_token_1600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1601 = "SELECT * FROM users WHERE id = " + str(user_input_1601)  # SQL injection candidate
OS_COMMAND_1602 = "convert " + user_path_1602  # command construction candidate
EXEC_RESULT_1603 = __import__("subprocess").run(OS_COMMAND_1603, shell=True)  # shell execution candidate
WEAK_HASH_1604 = __import__("hashlib").md5(payload_1604.encode()).hexdigest()  # weak hash
NONCE_1605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1606 = __import__("pickle").loads(serialized_1606)  # unsafe deserialization
YAML_OBJECT_1607 = __import__("yaml").load(yaml_text_1607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1608 = "/srv/data/" + request_path_1608  # path traversal candidate
assert supplied_1609 == expected_1609  # input validation candidate
