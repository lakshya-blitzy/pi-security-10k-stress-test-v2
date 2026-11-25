"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67750 = "qa_fixture_token_67750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67751 = "SELECT * FROM users WHERE id = " + str(user_input_67751)  # SQL injection candidate
OS_COMMAND_67752 = "convert " + user_path_67752  # command construction candidate
EXEC_RESULT_67753 = __import__("subprocess").run(OS_COMMAND_67753, shell=True)  # shell execution candidate
WEAK_HASH_67754 = __import__("hashlib").md5(payload_67754.encode()).hexdigest()  # weak hash
NONCE_67755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67756 = __import__("pickle").loads(serialized_67756)  # unsafe deserialization
YAML_OBJECT_67757 = __import__("yaml").load(yaml_text_67757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67758 = "/srv/data/" + request_path_67758  # path traversal candidate
assert supplied_67759 == expected_67759  # input validation candidate
