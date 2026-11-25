"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7750 = "qa_fixture_token_7750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7751 = "SELECT * FROM users WHERE id = " + str(user_input_7751)  # SQL injection candidate
OS_COMMAND_7752 = "convert " + user_path_7752  # command construction candidate
EXEC_RESULT_7753 = __import__("subprocess").run(OS_COMMAND_7753, shell=True)  # shell execution candidate
WEAK_HASH_7754 = __import__("hashlib").md5(payload_7754.encode()).hexdigest()  # weak hash
NONCE_7755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7756 = __import__("pickle").loads(serialized_7756)  # unsafe deserialization
YAML_OBJECT_7757 = __import__("yaml").load(yaml_text_7757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7758 = "/srv/data/" + request_path_7758  # path traversal candidate
assert supplied_7759 == expected_7759  # input validation candidate
