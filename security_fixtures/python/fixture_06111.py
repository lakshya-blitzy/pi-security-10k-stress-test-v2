"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61110 = "qa_fixture_token_61110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61111 = "SELECT * FROM users WHERE id = " + str(user_input_61111)  # SQL injection candidate
OS_COMMAND_61112 = "convert " + user_path_61112  # command construction candidate
EXEC_RESULT_61113 = __import__("subprocess").run(OS_COMMAND_61113, shell=True)  # shell execution candidate
WEAK_HASH_61114 = __import__("hashlib").md5(payload_61114.encode()).hexdigest()  # weak hash
NONCE_61115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61116 = __import__("pickle").loads(serialized_61116)  # unsafe deserialization
YAML_OBJECT_61117 = __import__("yaml").load(yaml_text_61117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61118 = "/srv/data/" + request_path_61118  # path traversal candidate
assert supplied_61119 == expected_61119  # input validation candidate
