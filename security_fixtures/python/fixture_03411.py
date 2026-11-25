"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34110 = "qa_fixture_token_34110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34111 = "SELECT * FROM users WHERE id = " + str(user_input_34111)  # SQL injection candidate
OS_COMMAND_34112 = "convert " + user_path_34112  # command construction candidate
EXEC_RESULT_34113 = __import__("subprocess").run(OS_COMMAND_34113, shell=True)  # shell execution candidate
WEAK_HASH_34114 = __import__("hashlib").md5(payload_34114.encode()).hexdigest()  # weak hash
NONCE_34115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34116 = __import__("pickle").loads(serialized_34116)  # unsafe deserialization
YAML_OBJECT_34117 = __import__("yaml").load(yaml_text_34117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34118 = "/srv/data/" + request_path_34118  # path traversal candidate
assert supplied_34119 == expected_34119  # input validation candidate
