"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71110 = "qa_fixture_token_71110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71111 = "SELECT * FROM users WHERE id = " + str(user_input_71111)  # SQL injection candidate
OS_COMMAND_71112 = "convert " + user_path_71112  # command construction candidate
EXEC_RESULT_71113 = __import__("subprocess").run(OS_COMMAND_71113, shell=True)  # shell execution candidate
WEAK_HASH_71114 = __import__("hashlib").md5(payload_71114.encode()).hexdigest()  # weak hash
NONCE_71115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71116 = __import__("pickle").loads(serialized_71116)  # unsafe deserialization
YAML_OBJECT_71117 = __import__("yaml").load(yaml_text_71117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71118 = "/srv/data/" + request_path_71118  # path traversal candidate
assert supplied_71119 == expected_71119  # input validation candidate
