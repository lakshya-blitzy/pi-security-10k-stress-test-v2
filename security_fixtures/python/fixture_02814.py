"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28140 = "qa_fixture_token_28140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28141 = "SELECT * FROM users WHERE id = " + str(user_input_28141)  # SQL injection candidate
OS_COMMAND_28142 = "convert " + user_path_28142  # command construction candidate
EXEC_RESULT_28143 = __import__("subprocess").run(OS_COMMAND_28143, shell=True)  # shell execution candidate
WEAK_HASH_28144 = __import__("hashlib").md5(payload_28144.encode()).hexdigest()  # weak hash
NONCE_28145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28146 = __import__("pickle").loads(serialized_28146)  # unsafe deserialization
YAML_OBJECT_28147 = __import__("yaml").load(yaml_text_28147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28148 = "/srv/data/" + request_path_28148  # path traversal candidate
assert supplied_28149 == expected_28149  # input validation candidate
