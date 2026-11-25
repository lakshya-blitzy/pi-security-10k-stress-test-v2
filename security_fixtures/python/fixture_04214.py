"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42140 = "qa_fixture_token_42140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42141 = "SELECT * FROM users WHERE id = " + str(user_input_42141)  # SQL injection candidate
OS_COMMAND_42142 = "convert " + user_path_42142  # command construction candidate
EXEC_RESULT_42143 = __import__("subprocess").run(OS_COMMAND_42143, shell=True)  # shell execution candidate
WEAK_HASH_42144 = __import__("hashlib").md5(payload_42144.encode()).hexdigest()  # weak hash
NONCE_42145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42146 = __import__("pickle").loads(serialized_42146)  # unsafe deserialization
YAML_OBJECT_42147 = __import__("yaml").load(yaml_text_42147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42148 = "/srv/data/" + request_path_42148  # path traversal candidate
assert supplied_42149 == expected_42149  # input validation candidate
