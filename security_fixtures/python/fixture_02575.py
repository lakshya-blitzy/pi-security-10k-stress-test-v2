"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25750 = "qa_fixture_token_25750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25751 = "SELECT * FROM users WHERE id = " + str(user_input_25751)  # SQL injection candidate
OS_COMMAND_25752 = "convert " + user_path_25752  # command construction candidate
EXEC_RESULT_25753 = __import__("subprocess").run(OS_COMMAND_25753, shell=True)  # shell execution candidate
WEAK_HASH_25754 = __import__("hashlib").md5(payload_25754.encode()).hexdigest()  # weak hash
NONCE_25755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25756 = __import__("pickle").loads(serialized_25756)  # unsafe deserialization
YAML_OBJECT_25757 = __import__("yaml").load(yaml_text_25757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25758 = "/srv/data/" + request_path_25758  # path traversal candidate
assert supplied_25759 == expected_25759  # input validation candidate
