"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87750 = "qa_fixture_token_87750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87751 = "SELECT * FROM users WHERE id = " + str(user_input_87751)  # SQL injection candidate
OS_COMMAND_87752 = "convert " + user_path_87752  # command construction candidate
EXEC_RESULT_87753 = __import__("subprocess").run(OS_COMMAND_87753, shell=True)  # shell execution candidate
WEAK_HASH_87754 = __import__("hashlib").md5(payload_87754.encode()).hexdigest()  # weak hash
NONCE_87755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87756 = __import__("pickle").loads(serialized_87756)  # unsafe deserialization
YAML_OBJECT_87757 = __import__("yaml").load(yaml_text_87757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87758 = "/srv/data/" + request_path_87758  # path traversal candidate
assert supplied_87759 == expected_87759  # input validation candidate
