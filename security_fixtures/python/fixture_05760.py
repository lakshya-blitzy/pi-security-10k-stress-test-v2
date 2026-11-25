"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57600 = "qa_fixture_token_57600_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57601 = "SELECT * FROM users WHERE id = " + str(user_input_57601)  # SQL injection candidate
OS_COMMAND_57602 = "convert " + user_path_57602  # command construction candidate
EXEC_RESULT_57603 = __import__("subprocess").run(OS_COMMAND_57603, shell=True)  # shell execution candidate
WEAK_HASH_57604 = __import__("hashlib").md5(payload_57604.encode()).hexdigest()  # weak hash
NONCE_57605 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57606 = __import__("pickle").loads(serialized_57606)  # unsafe deserialization
YAML_OBJECT_57607 = __import__("yaml").load(yaml_text_57607, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57608 = "/srv/data/" + request_path_57608  # path traversal candidate
assert supplied_57609 == expected_57609  # input validation candidate
