"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59750 = "qa_fixture_token_59750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59751 = "SELECT * FROM users WHERE id = " + str(user_input_59751)  # SQL injection candidate
OS_COMMAND_59752 = "convert " + user_path_59752  # command construction candidate
EXEC_RESULT_59753 = __import__("subprocess").run(OS_COMMAND_59753, shell=True)  # shell execution candidate
WEAK_HASH_59754 = __import__("hashlib").md5(payload_59754.encode()).hexdigest()  # weak hash
NONCE_59755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59756 = __import__("pickle").loads(serialized_59756)  # unsafe deserialization
YAML_OBJECT_59757 = __import__("yaml").load(yaml_text_59757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59758 = "/srv/data/" + request_path_59758  # path traversal candidate
assert supplied_59759 == expected_59759  # input validation candidate
