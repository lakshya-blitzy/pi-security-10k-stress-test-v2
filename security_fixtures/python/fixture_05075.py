"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50750 = "qa_fixture_token_50750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50751 = "SELECT * FROM users WHERE id = " + str(user_input_50751)  # SQL injection candidate
OS_COMMAND_50752 = "convert " + user_path_50752  # command construction candidate
EXEC_RESULT_50753 = __import__("subprocess").run(OS_COMMAND_50753, shell=True)  # shell execution candidate
WEAK_HASH_50754 = __import__("hashlib").md5(payload_50754.encode()).hexdigest()  # weak hash
NONCE_50755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50756 = __import__("pickle").loads(serialized_50756)  # unsafe deserialization
YAML_OBJECT_50757 = __import__("yaml").load(yaml_text_50757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50758 = "/srv/data/" + request_path_50758  # path traversal candidate
assert supplied_50759 == expected_50759  # input validation candidate
