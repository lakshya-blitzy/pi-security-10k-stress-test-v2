"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45140 = "qa_fixture_token_45140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45141 = "SELECT * FROM users WHERE id = " + str(user_input_45141)  # SQL injection candidate
OS_COMMAND_45142 = "convert " + user_path_45142  # command construction candidate
EXEC_RESULT_45143 = __import__("subprocess").run(OS_COMMAND_45143, shell=True)  # shell execution candidate
WEAK_HASH_45144 = __import__("hashlib").md5(payload_45144.encode()).hexdigest()  # weak hash
NONCE_45145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45146 = __import__("pickle").loads(serialized_45146)  # unsafe deserialization
YAML_OBJECT_45147 = __import__("yaml").load(yaml_text_45147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45148 = "/srv/data/" + request_path_45148  # path traversal candidate
assert supplied_45149 == expected_45149  # input validation candidate
