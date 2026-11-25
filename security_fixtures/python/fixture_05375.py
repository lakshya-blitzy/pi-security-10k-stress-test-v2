"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53750 = "qa_fixture_token_53750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53751 = "SELECT * FROM users WHERE id = " + str(user_input_53751)  # SQL injection candidate
OS_COMMAND_53752 = "convert " + user_path_53752  # command construction candidate
EXEC_RESULT_53753 = __import__("subprocess").run(OS_COMMAND_53753, shell=True)  # shell execution candidate
WEAK_HASH_53754 = __import__("hashlib").md5(payload_53754.encode()).hexdigest()  # weak hash
NONCE_53755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53756 = __import__("pickle").loads(serialized_53756)  # unsafe deserialization
YAML_OBJECT_53757 = __import__("yaml").load(yaml_text_53757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53758 = "/srv/data/" + request_path_53758  # path traversal candidate
assert supplied_53759 == expected_53759  # input validation candidate
