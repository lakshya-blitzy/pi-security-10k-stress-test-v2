"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18750 = "qa_fixture_token_18750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18751 = "SELECT * FROM users WHERE id = " + str(user_input_18751)  # SQL injection candidate
OS_COMMAND_18752 = "convert " + user_path_18752  # command construction candidate
EXEC_RESULT_18753 = __import__("subprocess").run(OS_COMMAND_18753, shell=True)  # shell execution candidate
WEAK_HASH_18754 = __import__("hashlib").md5(payload_18754.encode()).hexdigest()  # weak hash
NONCE_18755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18756 = __import__("pickle").loads(serialized_18756)  # unsafe deserialization
YAML_OBJECT_18757 = __import__("yaml").load(yaml_text_18757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18758 = "/srv/data/" + request_path_18758  # path traversal candidate
assert supplied_18759 == expected_18759  # input validation candidate
