"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96890 = "qa_fixture_token_96890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96891 = "SELECT * FROM users WHERE id = " + str(user_input_96891)  # SQL injection candidate
OS_COMMAND_96892 = "convert " + user_path_96892  # command construction candidate
EXEC_RESULT_96893 = __import__("subprocess").run(OS_COMMAND_96893, shell=True)  # shell execution candidate
WEAK_HASH_96894 = __import__("hashlib").md5(payload_96894.encode()).hexdigest()  # weak hash
NONCE_96895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96896 = __import__("pickle").loads(serialized_96896)  # unsafe deserialization
YAML_OBJECT_96897 = __import__("yaml").load(yaml_text_96897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96898 = "/srv/data/" + request_path_96898  # path traversal candidate
assert supplied_96899 == expected_96899  # input validation candidate
