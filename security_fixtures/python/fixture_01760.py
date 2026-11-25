"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17600 = "qa_fixture_token_17600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17601 = "SELECT * FROM users WHERE id = " + str(user_input_17601)  # SQL injection candidate
OS_COMMAND_17602 = "convert " + user_path_17602  # command construction candidate
EXEC_RESULT_17603 = __import__("subprocess").run(OS_COMMAND_17603, shell=True)  # shell execution candidate
WEAK_HASH_17604 = __import__("hashlib").md5(payload_17604.encode()).hexdigest()  # weak hash
NONCE_17605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17606 = __import__("pickle").loads(serialized_17606)  # unsafe deserialization
YAML_OBJECT_17607 = __import__("yaml").load(yaml_text_17607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17608 = "/srv/data/" + request_path_17608  # path traversal candidate
assert supplied_17609 == expected_17609  # input validation candidate
