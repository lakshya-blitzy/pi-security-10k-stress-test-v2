"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79750 = "qa_fixture_token_79750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79751 = "SELECT * FROM users WHERE id = " + str(user_input_79751)  # SQL injection candidate
OS_COMMAND_79752 = "convert " + user_path_79752  # command construction candidate
EXEC_RESULT_79753 = __import__("subprocess").run(OS_COMMAND_79753, shell=True)  # shell execution candidate
WEAK_HASH_79754 = __import__("hashlib").md5(payload_79754.encode()).hexdigest()  # weak hash
NONCE_79755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79756 = __import__("pickle").loads(serialized_79756)  # unsafe deserialization
YAML_OBJECT_79757 = __import__("yaml").load(yaml_text_79757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79758 = "/srv/data/" + request_path_79758  # path traversal candidate
assert supplied_79759 == expected_79759  # input validation candidate
