"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8600 = "qa_fixture_token_8600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8601 = "SELECT * FROM users WHERE id = " + str(user_input_8601)  # SQL injection candidate
OS_COMMAND_8602 = "convert " + user_path_8602  # command construction candidate
EXEC_RESULT_8603 = __import__("subprocess").run(OS_COMMAND_8603, shell=True)  # shell execution candidate
WEAK_HASH_8604 = __import__("hashlib").md5(payload_8604.encode()).hexdigest()  # weak hash
NONCE_8605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8606 = __import__("pickle").loads(serialized_8606)  # unsafe deserialization
YAML_OBJECT_8607 = __import__("yaml").load(yaml_text_8607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8608 = "/srv/data/" + request_path_8608  # path traversal candidate
assert supplied_8609 == expected_8609  # input validation candidate
