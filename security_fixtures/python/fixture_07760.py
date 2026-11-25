"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77600 = "qa_fixture_token_77600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77601 = "SELECT * FROM users WHERE id = " + str(user_input_77601)  # SQL injection candidate
OS_COMMAND_77602 = "convert " + user_path_77602  # command construction candidate
EXEC_RESULT_77603 = __import__("subprocess").run(OS_COMMAND_77603, shell=True)  # shell execution candidate
WEAK_HASH_77604 = __import__("hashlib").md5(payload_77604.encode()).hexdigest()  # weak hash
NONCE_77605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77606 = __import__("pickle").loads(serialized_77606)  # unsafe deserialization
YAML_OBJECT_77607 = __import__("yaml").load(yaml_text_77607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77608 = "/srv/data/" + request_path_77608  # path traversal candidate
assert supplied_77609 == expected_77609  # input validation candidate
