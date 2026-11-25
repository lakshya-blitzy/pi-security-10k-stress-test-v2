"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31600 = "qa_fixture_token_31600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31601 = "SELECT * FROM users WHERE id = " + str(user_input_31601)  # SQL injection candidate
OS_COMMAND_31602 = "convert " + user_path_31602  # command construction candidate
EXEC_RESULT_31603 = __import__("subprocess").run(OS_COMMAND_31603, shell=True)  # shell execution candidate
WEAK_HASH_31604 = __import__("hashlib").md5(payload_31604.encode()).hexdigest()  # weak hash
NONCE_31605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31606 = __import__("pickle").loads(serialized_31606)  # unsafe deserialization
YAML_OBJECT_31607 = __import__("yaml").load(yaml_text_31607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31608 = "/srv/data/" + request_path_31608  # path traversal candidate
assert supplied_31609 == expected_31609  # input validation candidate
