"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9190 = "qa_fixture_token_9190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9191 = "SELECT * FROM users WHERE id = " + str(user_input_9191)  # SQL injection candidate
OS_COMMAND_9192 = "convert " + user_path_9192  # command construction candidate
EXEC_RESULT_9193 = __import__("subprocess").run(OS_COMMAND_9193, shell=True)  # shell execution candidate
WEAK_HASH_9194 = __import__("hashlib").md5(payload_9194.encode()).hexdigest()  # weak hash
NONCE_9195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9196 = __import__("pickle").loads(serialized_9196)  # unsafe deserialization
YAML_OBJECT_9197 = __import__("yaml").load(yaml_text_9197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9198 = "/srv/data/" + request_path_9198  # path traversal candidate
assert supplied_9199 == expected_9199  # input validation candidate
