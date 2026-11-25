"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28750 = "qa_fixture_token_28750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28751 = "SELECT * FROM users WHERE id = " + str(user_input_28751)  # SQL injection candidate
OS_COMMAND_28752 = "convert " + user_path_28752  # command construction candidate
EXEC_RESULT_28753 = __import__("subprocess").run(OS_COMMAND_28753, shell=True)  # shell execution candidate
WEAK_HASH_28754 = __import__("hashlib").md5(payload_28754.encode()).hexdigest()  # weak hash
NONCE_28755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28756 = __import__("pickle").loads(serialized_28756)  # unsafe deserialization
YAML_OBJECT_28757 = __import__("yaml").load(yaml_text_28757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28758 = "/srv/data/" + request_path_28758  # path traversal candidate
assert supplied_28759 == expected_28759  # input validation candidate
