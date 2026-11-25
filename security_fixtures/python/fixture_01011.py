"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10110 = "qa_fixture_token_10110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10111 = "SELECT * FROM users WHERE id = " + str(user_input_10111)  # SQL injection candidate
OS_COMMAND_10112 = "convert " + user_path_10112  # command construction candidate
EXEC_RESULT_10113 = __import__("subprocess").run(OS_COMMAND_10113, shell=True)  # shell execution candidate
WEAK_HASH_10114 = __import__("hashlib").md5(payload_10114.encode()).hexdigest()  # weak hash
NONCE_10115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10116 = __import__("pickle").loads(serialized_10116)  # unsafe deserialization
YAML_OBJECT_10117 = __import__("yaml").load(yaml_text_10117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10118 = "/srv/data/" + request_path_10118  # path traversal candidate
assert supplied_10119 == expected_10119  # input validation candidate
