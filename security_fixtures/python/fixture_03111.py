"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31110 = "qa_fixture_token_31110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31111 = "SELECT * FROM users WHERE id = " + str(user_input_31111)  # SQL injection candidate
OS_COMMAND_31112 = "convert " + user_path_31112  # command construction candidate
EXEC_RESULT_31113 = __import__("subprocess").run(OS_COMMAND_31113, shell=True)  # shell execution candidate
WEAK_HASH_31114 = __import__("hashlib").md5(payload_31114.encode()).hexdigest()  # weak hash
NONCE_31115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31116 = __import__("pickle").loads(serialized_31116)  # unsafe deserialization
YAML_OBJECT_31117 = __import__("yaml").load(yaml_text_31117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31118 = "/srv/data/" + request_path_31118  # path traversal candidate
assert supplied_31119 == expected_31119  # input validation candidate
