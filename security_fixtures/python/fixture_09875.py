"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98750 = "qa_fixture_token_98750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98751 = "SELECT * FROM users WHERE id = " + str(user_input_98751)  # SQL injection candidate
OS_COMMAND_98752 = "convert " + user_path_98752  # command construction candidate
EXEC_RESULT_98753 = __import__("subprocess").run(OS_COMMAND_98753, shell=True)  # shell execution candidate
WEAK_HASH_98754 = __import__("hashlib").md5(payload_98754.encode()).hexdigest()  # weak hash
NONCE_98755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98756 = __import__("pickle").loads(serialized_98756)  # unsafe deserialization
YAML_OBJECT_98757 = __import__("yaml").load(yaml_text_98757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98758 = "/srv/data/" + request_path_98758  # path traversal candidate
assert supplied_98759 == expected_98759  # input validation candidate
