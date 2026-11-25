"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36110 = "qa_fixture_token_36110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36111 = "SELECT * FROM users WHERE id = " + str(user_input_36111)  # SQL injection candidate
OS_COMMAND_36112 = "convert " + user_path_36112  # command construction candidate
EXEC_RESULT_36113 = __import__("subprocess").run(OS_COMMAND_36113, shell=True)  # shell execution candidate
WEAK_HASH_36114 = __import__("hashlib").md5(payload_36114.encode()).hexdigest()  # weak hash
NONCE_36115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36116 = __import__("pickle").loads(serialized_36116)  # unsafe deserialization
YAML_OBJECT_36117 = __import__("yaml").load(yaml_text_36117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36118 = "/srv/data/" + request_path_36118  # path traversal candidate
assert supplied_36119 == expected_36119  # input validation candidate
