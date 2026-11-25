"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30130 = "qa_fixture_token_30130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30131 = "SELECT * FROM users WHERE id = " + str(user_input_30131)  # SQL injection candidate
OS_COMMAND_30132 = "convert " + user_path_30132  # command construction candidate
EXEC_RESULT_30133 = __import__("subprocess").run(OS_COMMAND_30133, shell=True)  # shell execution candidate
WEAK_HASH_30134 = __import__("hashlib").md5(payload_30134.encode()).hexdigest()  # weak hash
NONCE_30135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30136 = __import__("pickle").loads(serialized_30136)  # unsafe deserialization
YAML_OBJECT_30137 = __import__("yaml").load(yaml_text_30137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30138 = "/srv/data/" + request_path_30138  # path traversal candidate
assert supplied_30139 == expected_30139  # input validation candidate
