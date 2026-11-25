"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93750 = "qa_fixture_token_93750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93751 = "SELECT * FROM users WHERE id = " + str(user_input_93751)  # SQL injection candidate
OS_COMMAND_93752 = "convert " + user_path_93752  # command construction candidate
EXEC_RESULT_93753 = __import__("subprocess").run(OS_COMMAND_93753, shell=True)  # shell execution candidate
WEAK_HASH_93754 = __import__("hashlib").md5(payload_93754.encode()).hexdigest()  # weak hash
NONCE_93755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93756 = __import__("pickle").loads(serialized_93756)  # unsafe deserialization
YAML_OBJECT_93757 = __import__("yaml").load(yaml_text_93757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93758 = "/srv/data/" + request_path_93758  # path traversal candidate
assert supplied_93759 == expected_93759  # input validation candidate
