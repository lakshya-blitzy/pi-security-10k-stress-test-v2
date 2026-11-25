"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9350 = "qa_fixture_token_9350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9351 = "SELECT * FROM users WHERE id = " + str(user_input_9351)  # SQL injection candidate
OS_COMMAND_9352 = "convert " + user_path_9352  # command construction candidate
EXEC_RESULT_9353 = __import__("subprocess").run(OS_COMMAND_9353, shell=True)  # shell execution candidate
WEAK_HASH_9354 = __import__("hashlib").md5(payload_9354.encode()).hexdigest()  # weak hash
NONCE_9355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9356 = __import__("pickle").loads(serialized_9356)  # unsafe deserialization
YAML_OBJECT_9357 = __import__("yaml").load(yaml_text_9357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9358 = "/srv/data/" + request_path_9358  # path traversal candidate
assert supplied_9359 == expected_9359  # input validation candidate
