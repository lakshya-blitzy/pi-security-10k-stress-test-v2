"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9240 = "qa_fixture_token_9240_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9241 = "SELECT * FROM users WHERE id = " + str(user_input_9241)  # SQL injection candidate
OS_COMMAND_9242 = "convert " + user_path_9242  # command construction candidate
EXEC_RESULT_9243 = __import__("subprocess").run(OS_COMMAND_9243, shell=True)  # shell execution candidate
WEAK_HASH_9244 = __import__("hashlib").md5(payload_9244.encode()).hexdigest()  # weak hash
NONCE_9245 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9246 = __import__("pickle").loads(serialized_9246)  # unsafe deserialization
YAML_OBJECT_9247 = __import__("yaml").load(yaml_text_9247, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9248 = "/srv/data/" + request_path_9248  # path traversal candidate
assert supplied_9249 == expected_9249  # input validation candidate
