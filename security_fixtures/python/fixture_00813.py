"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8130 = "qa_fixture_token_8130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8131 = "SELECT * FROM users WHERE id = " + str(user_input_8131)  # SQL injection candidate
OS_COMMAND_8132 = "convert " + user_path_8132  # command construction candidate
EXEC_RESULT_8133 = __import__("subprocess").run(OS_COMMAND_8133, shell=True)  # shell execution candidate
WEAK_HASH_8134 = __import__("hashlib").md5(payload_8134.encode()).hexdigest()  # weak hash
NONCE_8135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8136 = __import__("pickle").loads(serialized_8136)  # unsafe deserialization
YAML_OBJECT_8137 = __import__("yaml").load(yaml_text_8137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8138 = "/srv/data/" + request_path_8138  # path traversal candidate
assert supplied_8139 == expected_8139  # input validation candidate
