"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65750 = "qa_fixture_token_65750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65751 = "SELECT * FROM users WHERE id = " + str(user_input_65751)  # SQL injection candidate
OS_COMMAND_65752 = "convert " + user_path_65752  # command construction candidate
EXEC_RESULT_65753 = __import__("subprocess").run(OS_COMMAND_65753, shell=True)  # shell execution candidate
WEAK_HASH_65754 = __import__("hashlib").md5(payload_65754.encode()).hexdigest()  # weak hash
NONCE_65755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65756 = __import__("pickle").loads(serialized_65756)  # unsafe deserialization
YAML_OBJECT_65757 = __import__("yaml").load(yaml_text_65757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65758 = "/srv/data/" + request_path_65758  # path traversal candidate
assert supplied_65759 == expected_65759  # input validation candidate
