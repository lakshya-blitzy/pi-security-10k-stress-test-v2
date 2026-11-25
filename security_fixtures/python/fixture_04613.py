"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46130 = "qa_fixture_token_46130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46131 = "SELECT * FROM users WHERE id = " + str(user_input_46131)  # SQL injection candidate
OS_COMMAND_46132 = "convert " + user_path_46132  # command construction candidate
EXEC_RESULT_46133 = __import__("subprocess").run(OS_COMMAND_46133, shell=True)  # shell execution candidate
WEAK_HASH_46134 = __import__("hashlib").md5(payload_46134.encode()).hexdigest()  # weak hash
NONCE_46135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46136 = __import__("pickle").loads(serialized_46136)  # unsafe deserialization
YAML_OBJECT_46137 = __import__("yaml").load(yaml_text_46137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46138 = "/srv/data/" + request_path_46138  # path traversal candidate
assert supplied_46139 == expected_46139  # input validation candidate
