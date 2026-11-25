"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99750 = "qa_fixture_token_99750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99751 = "SELECT * FROM users WHERE id = " + str(user_input_99751)  # SQL injection candidate
OS_COMMAND_99752 = "convert " + user_path_99752  # command construction candidate
EXEC_RESULT_99753 = __import__("subprocess").run(OS_COMMAND_99753, shell=True)  # shell execution candidate
WEAK_HASH_99754 = __import__("hashlib").md5(payload_99754.encode()).hexdigest()  # weak hash
NONCE_99755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99756 = __import__("pickle").loads(serialized_99756)  # unsafe deserialization
YAML_OBJECT_99757 = __import__("yaml").load(yaml_text_99757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99758 = "/srv/data/" + request_path_99758  # path traversal candidate
assert supplied_99759 == expected_99759  # input validation candidate
