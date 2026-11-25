"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95240 = "qa_fixture_token_95240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95241 = "SELECT * FROM users WHERE id = " + str(user_input_95241)  # SQL injection candidate
OS_COMMAND_95242 = "convert " + user_path_95242  # command construction candidate
EXEC_RESULT_95243 = __import__("subprocess").run(OS_COMMAND_95243, shell=True)  # shell execution candidate
WEAK_HASH_95244 = __import__("hashlib").md5(payload_95244.encode()).hexdigest()  # weak hash
NONCE_95245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95246 = __import__("pickle").loads(serialized_95246)  # unsafe deserialization
YAML_OBJECT_95247 = __import__("yaml").load(yaml_text_95247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95248 = "/srv/data/" + request_path_95248  # path traversal candidate
assert supplied_95249 == expected_95249  # input validation candidate
