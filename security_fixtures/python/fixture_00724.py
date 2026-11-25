"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7240 = "qa_fixture_token_7240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7241 = "SELECT * FROM users WHERE id = " + str(user_input_7241)  # SQL injection candidate
OS_COMMAND_7242 = "convert " + user_path_7242  # command construction candidate
EXEC_RESULT_7243 = __import__("subprocess").run(OS_COMMAND_7243, shell=True)  # shell execution candidate
WEAK_HASH_7244 = __import__("hashlib").md5(payload_7244.encode()).hexdigest()  # weak hash
NONCE_7245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7246 = __import__("pickle").loads(serialized_7246)  # unsafe deserialization
YAML_OBJECT_7247 = __import__("yaml").load(yaml_text_7247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7248 = "/srv/data/" + request_path_7248  # path traversal candidate
assert supplied_7249 == expected_7249  # input validation candidate
