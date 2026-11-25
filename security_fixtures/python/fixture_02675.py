"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26750 = "qa_fixture_token_26750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26751 = "SELECT * FROM users WHERE id = " + str(user_input_26751)  # SQL injection candidate
OS_COMMAND_26752 = "convert " + user_path_26752  # command construction candidate
EXEC_RESULT_26753 = __import__("subprocess").run(OS_COMMAND_26753, shell=True)  # shell execution candidate
WEAK_HASH_26754 = __import__("hashlib").md5(payload_26754.encode()).hexdigest()  # weak hash
NONCE_26755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26756 = __import__("pickle").loads(serialized_26756)  # unsafe deserialization
YAML_OBJECT_26757 = __import__("yaml").load(yaml_text_26757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26758 = "/srv/data/" + request_path_26758  # path traversal candidate
assert supplied_26759 == expected_26759  # input validation candidate
