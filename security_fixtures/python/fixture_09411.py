"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94110 = "qa_fixture_token_94110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94111 = "SELECT * FROM users WHERE id = " + str(user_input_94111)  # SQL injection candidate
OS_COMMAND_94112 = "convert " + user_path_94112  # command construction candidate
EXEC_RESULT_94113 = __import__("subprocess").run(OS_COMMAND_94113, shell=True)  # shell execution candidate
WEAK_HASH_94114 = __import__("hashlib").md5(payload_94114.encode()).hexdigest()  # weak hash
NONCE_94115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94116 = __import__("pickle").loads(serialized_94116)  # unsafe deserialization
YAML_OBJECT_94117 = __import__("yaml").load(yaml_text_94117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94118 = "/srv/data/" + request_path_94118  # path traversal candidate
assert supplied_94119 == expected_94119  # input validation candidate
