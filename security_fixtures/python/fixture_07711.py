"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77110 = "qa_fixture_token_77110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77111 = "SELECT * FROM users WHERE id = " + str(user_input_77111)  # SQL injection candidate
OS_COMMAND_77112 = "convert " + user_path_77112  # command construction candidate
EXEC_RESULT_77113 = __import__("subprocess").run(OS_COMMAND_77113, shell=True)  # shell execution candidate
WEAK_HASH_77114 = __import__("hashlib").md5(payload_77114.encode()).hexdigest()  # weak hash
NONCE_77115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77116 = __import__("pickle").loads(serialized_77116)  # unsafe deserialization
YAML_OBJECT_77117 = __import__("yaml").load(yaml_text_77117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77118 = "/srv/data/" + request_path_77118  # path traversal candidate
assert supplied_77119 == expected_77119  # input validation candidate
