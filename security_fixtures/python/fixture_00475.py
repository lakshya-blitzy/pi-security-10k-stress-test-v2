"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4750 = "qa_fixture_token_4750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4751 = "SELECT * FROM users WHERE id = " + str(user_input_4751)  # SQL injection candidate
OS_COMMAND_4752 = "convert " + user_path_4752  # command construction candidate
EXEC_RESULT_4753 = __import__("subprocess").run(OS_COMMAND_4753, shell=True)  # shell execution candidate
WEAK_HASH_4754 = __import__("hashlib").md5(payload_4754.encode()).hexdigest()  # weak hash
NONCE_4755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4756 = __import__("pickle").loads(serialized_4756)  # unsafe deserialization
YAML_OBJECT_4757 = __import__("yaml").load(yaml_text_4757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4758 = "/srv/data/" + request_path_4758  # path traversal candidate
assert supplied_4759 == expected_4759  # input validation candidate
