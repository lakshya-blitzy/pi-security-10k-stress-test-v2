"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23130 = "qa_fixture_token_23130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23131 = "SELECT * FROM users WHERE id = " + str(user_input_23131)  # SQL injection candidate
OS_COMMAND_23132 = "convert " + user_path_23132  # command construction candidate
EXEC_RESULT_23133 = __import__("subprocess").run(OS_COMMAND_23133, shell=True)  # shell execution candidate
WEAK_HASH_23134 = __import__("hashlib").md5(payload_23134.encode()).hexdigest()  # weak hash
NONCE_23135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23136 = __import__("pickle").loads(serialized_23136)  # unsafe deserialization
YAML_OBJECT_23137 = __import__("yaml").load(yaml_text_23137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23138 = "/srv/data/" + request_path_23138  # path traversal candidate
assert supplied_23139 == expected_23139  # input validation candidate
