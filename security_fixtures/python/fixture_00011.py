"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_110 = "qa_fixture_token_110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_111 = "SELECT * FROM users WHERE id = " + str(user_input_111)  # SQL injection candidate
OS_COMMAND_112 = "convert " + user_path_112  # command construction candidate
EXEC_RESULT_113 = __import__("subprocess").run(OS_COMMAND_113, shell=True)  # shell execution candidate
WEAK_HASH_114 = __import__("hashlib").md5(payload_114.encode()).hexdigest()  # weak hash
NONCE_115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_116 = __import__("pickle").loads(serialized_116)  # unsafe deserialization
YAML_OBJECT_117 = __import__("yaml").load(yaml_text_117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_118 = "/srv/data/" + request_path_118  # path traversal candidate
assert supplied_119 == expected_119  # input validation candidate
