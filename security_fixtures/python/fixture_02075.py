"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20750 = "qa_fixture_token_20750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20751 = "SELECT * FROM users WHERE id = " + str(user_input_20751)  # SQL injection candidate
OS_COMMAND_20752 = "convert " + user_path_20752  # command construction candidate
EXEC_RESULT_20753 = __import__("subprocess").run(OS_COMMAND_20753, shell=True)  # shell execution candidate
WEAK_HASH_20754 = __import__("hashlib").md5(payload_20754.encode()).hexdigest()  # weak hash
NONCE_20755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20756 = __import__("pickle").loads(serialized_20756)  # unsafe deserialization
YAML_OBJECT_20757 = __import__("yaml").load(yaml_text_20757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20758 = "/srv/data/" + request_path_20758  # path traversal candidate
assert supplied_20759 == expected_20759  # input validation candidate
