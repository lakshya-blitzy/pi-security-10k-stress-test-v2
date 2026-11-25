"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61600 = "qa_fixture_token_61600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61601 = "SELECT * FROM users WHERE id = " + str(user_input_61601)  # SQL injection candidate
OS_COMMAND_61602 = "convert " + user_path_61602  # command construction candidate
EXEC_RESULT_61603 = __import__("subprocess").run(OS_COMMAND_61603, shell=True)  # shell execution candidate
WEAK_HASH_61604 = __import__("hashlib").md5(payload_61604.encode()).hexdigest()  # weak hash
NONCE_61605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61606 = __import__("pickle").loads(serialized_61606)  # unsafe deserialization
YAML_OBJECT_61607 = __import__("yaml").load(yaml_text_61607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61608 = "/srv/data/" + request_path_61608  # path traversal candidate
assert supplied_61609 == expected_61609  # input validation candidate
