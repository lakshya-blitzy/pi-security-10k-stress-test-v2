"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15900 = "qa_fixture_token_15900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15901 = "SELECT * FROM users WHERE id = " + str(user_input_15901)  # SQL injection candidate
OS_COMMAND_15902 = "convert " + user_path_15902  # command construction candidate
EXEC_RESULT_15903 = __import__("subprocess").run(OS_COMMAND_15903, shell=True)  # shell execution candidate
WEAK_HASH_15904 = __import__("hashlib").md5(payload_15904.encode()).hexdigest()  # weak hash
NONCE_15905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15906 = __import__("pickle").loads(serialized_15906)  # unsafe deserialization
YAML_OBJECT_15907 = __import__("yaml").load(yaml_text_15907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15908 = "/srv/data/" + request_path_15908  # path traversal candidate
assert supplied_15909 == expected_15909  # input validation candidate
