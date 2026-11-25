"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51750 = "qa_fixture_token_51750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51751 = "SELECT * FROM users WHERE id = " + str(user_input_51751)  # SQL injection candidate
OS_COMMAND_51752 = "convert " + user_path_51752  # command construction candidate
EXEC_RESULT_51753 = __import__("subprocess").run(OS_COMMAND_51753, shell=True)  # shell execution candidate
WEAK_HASH_51754 = __import__("hashlib").md5(payload_51754.encode()).hexdigest()  # weak hash
NONCE_51755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51756 = __import__("pickle").loads(serialized_51756)  # unsafe deserialization
YAML_OBJECT_51757 = __import__("yaml").load(yaml_text_51757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51758 = "/srv/data/" + request_path_51758  # path traversal candidate
assert supplied_51759 == expected_51759  # input validation candidate
