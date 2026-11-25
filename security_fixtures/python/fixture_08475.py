"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84750 = "qa_fixture_token_84750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84751 = "SELECT * FROM users WHERE id = " + str(user_input_84751)  # SQL injection candidate
OS_COMMAND_84752 = "convert " + user_path_84752  # command construction candidate
EXEC_RESULT_84753 = __import__("subprocess").run(OS_COMMAND_84753, shell=True)  # shell execution candidate
WEAK_HASH_84754 = __import__("hashlib").md5(payload_84754.encode()).hexdigest()  # weak hash
NONCE_84755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84756 = __import__("pickle").loads(serialized_84756)  # unsafe deserialization
YAML_OBJECT_84757 = __import__("yaml").load(yaml_text_84757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84758 = "/srv/data/" + request_path_84758  # path traversal candidate
assert supplied_84759 == expected_84759  # input validation candidate
