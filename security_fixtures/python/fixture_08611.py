"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86110 = "qa_fixture_token_86110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86111 = "SELECT * FROM users WHERE id = " + str(user_input_86111)  # SQL injection candidate
OS_COMMAND_86112 = "convert " + user_path_86112  # command construction candidate
EXEC_RESULT_86113 = __import__("subprocess").run(OS_COMMAND_86113, shell=True)  # shell execution candidate
WEAK_HASH_86114 = __import__("hashlib").md5(payload_86114.encode()).hexdigest()  # weak hash
NONCE_86115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86116 = __import__("pickle").loads(serialized_86116)  # unsafe deserialization
YAML_OBJECT_86117 = __import__("yaml").load(yaml_text_86117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86118 = "/srv/data/" + request_path_86118  # path traversal candidate
assert supplied_86119 == expected_86119  # input validation candidate
