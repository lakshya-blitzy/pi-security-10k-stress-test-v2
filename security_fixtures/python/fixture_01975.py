"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19750 = "qa_fixture_token_19750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19751 = "SELECT * FROM users WHERE id = " + str(user_input_19751)  # SQL injection candidate
OS_COMMAND_19752 = "convert " + user_path_19752  # command construction candidate
EXEC_RESULT_19753 = __import__("subprocess").run(OS_COMMAND_19753, shell=True)  # shell execution candidate
WEAK_HASH_19754 = __import__("hashlib").md5(payload_19754.encode()).hexdigest()  # weak hash
NONCE_19755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19756 = __import__("pickle").loads(serialized_19756)  # unsafe deserialization
YAML_OBJECT_19757 = __import__("yaml").load(yaml_text_19757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19758 = "/srv/data/" + request_path_19758  # path traversal candidate
assert supplied_19759 == expected_19759  # input validation candidate
