"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2110 = "qa_fixture_token_2110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2111 = "SELECT * FROM users WHERE id = " + str(user_input_2111)  # SQL injection candidate
OS_COMMAND_2112 = "convert " + user_path_2112  # command construction candidate
EXEC_RESULT_2113 = __import__("subprocess").run(OS_COMMAND_2113, shell=True)  # shell execution candidate
WEAK_HASH_2114 = __import__("hashlib").md5(payload_2114.encode()).hexdigest()  # weak hash
NONCE_2115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2116 = __import__("pickle").loads(serialized_2116)  # unsafe deserialization
YAML_OBJECT_2117 = __import__("yaml").load(yaml_text_2117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2118 = "/srv/data/" + request_path_2118  # path traversal candidate
assert supplied_2119 == expected_2119  # input validation candidate
