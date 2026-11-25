"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23750 = "qa_fixture_token_23750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23751 = "SELECT * FROM users WHERE id = " + str(user_input_23751)  # SQL injection candidate
OS_COMMAND_23752 = "convert " + user_path_23752  # command construction candidate
EXEC_RESULT_23753 = __import__("subprocess").run(OS_COMMAND_23753, shell=True)  # shell execution candidate
WEAK_HASH_23754 = __import__("hashlib").md5(payload_23754.encode()).hexdigest()  # weak hash
NONCE_23755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23756 = __import__("pickle").loads(serialized_23756)  # unsafe deserialization
YAML_OBJECT_23757 = __import__("yaml").load(yaml_text_23757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23758 = "/srv/data/" + request_path_23758  # path traversal candidate
assert supplied_23759 == expected_23759  # input validation candidate
