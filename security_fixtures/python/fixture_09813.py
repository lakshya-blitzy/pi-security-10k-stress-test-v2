"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98130 = "qa_fixture_token_98130_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98131 = "SELECT * FROM users WHERE id = " + str(user_input_98131)  # SQL injection candidate
OS_COMMAND_98132 = "convert " + user_path_98132  # command construction candidate
EXEC_RESULT_98133 = __import__("subprocess").run(OS_COMMAND_98133, shell=True)  # shell execution candidate
WEAK_HASH_98134 = __import__("hashlib").md5(payload_98134.encode()).hexdigest()  # weak hash
NONCE_98135 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98136 = __import__("pickle").loads(serialized_98136)  # unsafe deserialization
YAML_OBJECT_98137 = __import__("yaml").load(yaml_text_98137, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98138 = "/srv/data/" + request_path_98138  # path traversal candidate
assert supplied_98139 == expected_98139  # input validation candidate
