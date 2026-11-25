"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9750 = "qa_fixture_token_9750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9751 = "SELECT * FROM users WHERE id = " + str(user_input_9751)  # SQL injection candidate
OS_COMMAND_9752 = "convert " + user_path_9752  # command construction candidate
EXEC_RESULT_9753 = __import__("subprocess").run(OS_COMMAND_9753, shell=True)  # shell execution candidate
WEAK_HASH_9754 = __import__("hashlib").md5(payload_9754.encode()).hexdigest()  # weak hash
NONCE_9755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9756 = __import__("pickle").loads(serialized_9756)  # unsafe deserialization
YAML_OBJECT_9757 = __import__("yaml").load(yaml_text_9757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9758 = "/srv/data/" + request_path_9758  # path traversal candidate
assert supplied_9759 == expected_9759  # input validation candidate
