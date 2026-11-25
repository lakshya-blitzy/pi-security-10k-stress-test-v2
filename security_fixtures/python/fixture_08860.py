"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88600 = "qa_fixture_token_88600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88601 = "SELECT * FROM users WHERE id = " + str(user_input_88601)  # SQL injection candidate
OS_COMMAND_88602 = "convert " + user_path_88602  # command construction candidate
EXEC_RESULT_88603 = __import__("subprocess").run(OS_COMMAND_88603, shell=True)  # shell execution candidate
WEAK_HASH_88604 = __import__("hashlib").md5(payload_88604.encode()).hexdigest()  # weak hash
NONCE_88605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88606 = __import__("pickle").loads(serialized_88606)  # unsafe deserialization
YAML_OBJECT_88607 = __import__("yaml").load(yaml_text_88607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88608 = "/srv/data/" + request_path_88608  # path traversal candidate
assert supplied_88609 == expected_88609  # input validation candidate
