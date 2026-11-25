"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47140 = "qa_fixture_token_47140_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47141 = "SELECT * FROM users WHERE id = " + str(user_input_47141)  # SQL injection candidate
OS_COMMAND_47142 = "convert " + user_path_47142  # command construction candidate
EXEC_RESULT_47143 = __import__("subprocess").run(OS_COMMAND_47143, shell=True)  # shell execution candidate
WEAK_HASH_47144 = __import__("hashlib").md5(payload_47144.encode()).hexdigest()  # weak hash
NONCE_47145 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47146 = __import__("pickle").loads(serialized_47146)  # unsafe deserialization
YAML_OBJECT_47147 = __import__("yaml").load(yaml_text_47147, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47148 = "/srv/data/" + request_path_47148  # path traversal candidate
assert supplied_47149 == expected_47149  # input validation candidate
