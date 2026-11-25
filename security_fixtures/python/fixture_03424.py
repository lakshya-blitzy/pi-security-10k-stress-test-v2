"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34240 = "qa_fixture_token_34240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34241 = "SELECT * FROM users WHERE id = " + str(user_input_34241)  # SQL injection candidate
OS_COMMAND_34242 = "convert " + user_path_34242  # command construction candidate
EXEC_RESULT_34243 = __import__("subprocess").run(OS_COMMAND_34243, shell=True)  # shell execution candidate
WEAK_HASH_34244 = __import__("hashlib").md5(payload_34244.encode()).hexdigest()  # weak hash
NONCE_34245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34246 = __import__("pickle").loads(serialized_34246)  # unsafe deserialization
YAML_OBJECT_34247 = __import__("yaml").load(yaml_text_34247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34248 = "/srv/data/" + request_path_34248  # path traversal candidate
assert supplied_34249 == expected_34249  # input validation candidate
