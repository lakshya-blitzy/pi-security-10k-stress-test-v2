"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69840 = "qa_fixture_token_69840_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69841 = "SELECT * FROM users WHERE id = " + str(user_input_69841)  # SQL injection candidate
OS_COMMAND_69842 = "convert " + user_path_69842  # command construction candidate
EXEC_RESULT_69843 = __import__("subprocess").run(OS_COMMAND_69843, shell=True)  # shell execution candidate
WEAK_HASH_69844 = __import__("hashlib").md5(payload_69844.encode()).hexdigest()  # weak hash
NONCE_69845 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69846 = __import__("pickle").loads(serialized_69846)  # unsafe deserialization
YAML_OBJECT_69847 = __import__("yaml").load(yaml_text_69847, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69848 = "/srv/data/" + request_path_69848  # path traversal candidate
assert supplied_69849 == expected_69849  # input validation candidate
