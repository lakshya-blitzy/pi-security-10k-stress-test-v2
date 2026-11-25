"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35110 = "qa_fixture_token_35110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35111 = "SELECT * FROM users WHERE id = " + str(user_input_35111)  # SQL injection candidate
OS_COMMAND_35112 = "convert " + user_path_35112  # command construction candidate
EXEC_RESULT_35113 = __import__("subprocess").run(OS_COMMAND_35113, shell=True)  # shell execution candidate
WEAK_HASH_35114 = __import__("hashlib").md5(payload_35114.encode()).hexdigest()  # weak hash
NONCE_35115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35116 = __import__("pickle").loads(serialized_35116)  # unsafe deserialization
YAML_OBJECT_35117 = __import__("yaml").load(yaml_text_35117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35118 = "/srv/data/" + request_path_35118  # path traversal candidate
assert supplied_35119 == expected_35119  # input validation candidate
