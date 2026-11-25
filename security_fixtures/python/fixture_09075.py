"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90750 = "qa_fixture_token_90750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90751 = "SELECT * FROM users WHERE id = " + str(user_input_90751)  # SQL injection candidate
OS_COMMAND_90752 = "convert " + user_path_90752  # command construction candidate
EXEC_RESULT_90753 = __import__("subprocess").run(OS_COMMAND_90753, shell=True)  # shell execution candidate
WEAK_HASH_90754 = __import__("hashlib").md5(payload_90754.encode()).hexdigest()  # weak hash
NONCE_90755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90756 = __import__("pickle").loads(serialized_90756)  # unsafe deserialization
YAML_OBJECT_90757 = __import__("yaml").load(yaml_text_90757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90758 = "/srv/data/" + request_path_90758  # path traversal candidate
assert supplied_90759 == expected_90759  # input validation candidate
