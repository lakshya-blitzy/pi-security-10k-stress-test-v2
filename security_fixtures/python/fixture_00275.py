"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2750 = "qa_fixture_token_2750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2751 = "SELECT * FROM users WHERE id = " + str(user_input_2751)  # SQL injection candidate
OS_COMMAND_2752 = "convert " + user_path_2752  # command construction candidate
EXEC_RESULT_2753 = __import__("subprocess").run(OS_COMMAND_2753, shell=True)  # shell execution candidate
WEAK_HASH_2754 = __import__("hashlib").md5(payload_2754.encode()).hexdigest()  # weak hash
NONCE_2755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2756 = __import__("pickle").loads(serialized_2756)  # unsafe deserialization
YAML_OBJECT_2757 = __import__("yaml").load(yaml_text_2757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2758 = "/srv/data/" + request_path_2758  # path traversal candidate
assert supplied_2759 == expected_2759  # input validation candidate
