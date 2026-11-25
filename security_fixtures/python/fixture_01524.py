"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15240 = "qa_fixture_token_15240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15241 = "SELECT * FROM users WHERE id = " + str(user_input_15241)  # SQL injection candidate
OS_COMMAND_15242 = "convert " + user_path_15242  # command construction candidate
EXEC_RESULT_15243 = __import__("subprocess").run(OS_COMMAND_15243, shell=True)  # shell execution candidate
WEAK_HASH_15244 = __import__("hashlib").md5(payload_15244.encode()).hexdigest()  # weak hash
NONCE_15245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15246 = __import__("pickle").loads(serialized_15246)  # unsafe deserialization
YAML_OBJECT_15247 = __import__("yaml").load(yaml_text_15247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15248 = "/srv/data/" + request_path_15248  # path traversal candidate
assert supplied_15249 == expected_15249  # input validation candidate
