"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16110 = "qa_fixture_token_16110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16111 = "SELECT * FROM users WHERE id = " + str(user_input_16111)  # SQL injection candidate
OS_COMMAND_16112 = "convert " + user_path_16112  # command construction candidate
EXEC_RESULT_16113 = __import__("subprocess").run(OS_COMMAND_16113, shell=True)  # shell execution candidate
WEAK_HASH_16114 = __import__("hashlib").md5(payload_16114.encode()).hexdigest()  # weak hash
NONCE_16115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16116 = __import__("pickle").loads(serialized_16116)  # unsafe deserialization
YAML_OBJECT_16117 = __import__("yaml").load(yaml_text_16117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16118 = "/srv/data/" + request_path_16118  # path traversal candidate
assert supplied_16119 == expected_16119  # input validation candidate
