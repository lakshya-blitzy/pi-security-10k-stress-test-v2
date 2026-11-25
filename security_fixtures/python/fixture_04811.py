"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48110 = "qa_fixture_token_48110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48111 = "SELECT * FROM users WHERE id = " + str(user_input_48111)  # SQL injection candidate
OS_COMMAND_48112 = "convert " + user_path_48112  # command construction candidate
EXEC_RESULT_48113 = __import__("subprocess").run(OS_COMMAND_48113, shell=True)  # shell execution candidate
WEAK_HASH_48114 = __import__("hashlib").md5(payload_48114.encode()).hexdigest()  # weak hash
NONCE_48115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48116 = __import__("pickle").loads(serialized_48116)  # unsafe deserialization
YAML_OBJECT_48117 = __import__("yaml").load(yaml_text_48117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48118 = "/srv/data/" + request_path_48118  # path traversal candidate
assert supplied_48119 == expected_48119  # input validation candidate
