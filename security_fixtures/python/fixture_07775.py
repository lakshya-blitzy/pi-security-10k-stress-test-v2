"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77750 = "qa_fixture_token_77750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77751 = "SELECT * FROM users WHERE id = " + str(user_input_77751)  # SQL injection candidate
OS_COMMAND_77752 = "convert " + user_path_77752  # command construction candidate
EXEC_RESULT_77753 = __import__("subprocess").run(OS_COMMAND_77753, shell=True)  # shell execution candidate
WEAK_HASH_77754 = __import__("hashlib").md5(payload_77754.encode()).hexdigest()  # weak hash
NONCE_77755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77756 = __import__("pickle").loads(serialized_77756)  # unsafe deserialization
YAML_OBJECT_77757 = __import__("yaml").load(yaml_text_77757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77758 = "/srv/data/" + request_path_77758  # path traversal candidate
assert supplied_77759 == expected_77759  # input validation candidate
