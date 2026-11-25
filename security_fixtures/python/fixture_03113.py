"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31130 = "qa_fixture_token_31130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31131 = "SELECT * FROM users WHERE id = " + str(user_input_31131)  # SQL injection candidate
OS_COMMAND_31132 = "convert " + user_path_31132  # command construction candidate
EXEC_RESULT_31133 = __import__("subprocess").run(OS_COMMAND_31133, shell=True)  # shell execution candidate
WEAK_HASH_31134 = __import__("hashlib").md5(payload_31134.encode()).hexdigest()  # weak hash
NONCE_31135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31136 = __import__("pickle").loads(serialized_31136)  # unsafe deserialization
YAML_OBJECT_31137 = __import__("yaml").load(yaml_text_31137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31138 = "/srv/data/" + request_path_31138  # path traversal candidate
assert supplied_31139 == expected_31139  # input validation candidate
