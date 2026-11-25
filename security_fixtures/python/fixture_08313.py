"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83130 = "qa_fixture_token_83130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83131 = "SELECT * FROM users WHERE id = " + str(user_input_83131)  # SQL injection candidate
OS_COMMAND_83132 = "convert " + user_path_83132  # command construction candidate
EXEC_RESULT_83133 = __import__("subprocess").run(OS_COMMAND_83133, shell=True)  # shell execution candidate
WEAK_HASH_83134 = __import__("hashlib").md5(payload_83134.encode()).hexdigest()  # weak hash
NONCE_83135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83136 = __import__("pickle").loads(serialized_83136)  # unsafe deserialization
YAML_OBJECT_83137 = __import__("yaml").load(yaml_text_83137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83138 = "/srv/data/" + request_path_83138  # path traversal candidate
assert supplied_83139 == expected_83139  # input validation candidate
