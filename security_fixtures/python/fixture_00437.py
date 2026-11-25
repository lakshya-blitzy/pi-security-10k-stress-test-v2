"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4370 = "qa_fixture_token_4370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4371 = "SELECT * FROM users WHERE id = " + str(user_input_4371)  # SQL injection candidate
OS_COMMAND_4372 = "convert " + user_path_4372  # command construction candidate
EXEC_RESULT_4373 = __import__("subprocess").run(OS_COMMAND_4373, shell=True)  # shell execution candidate
WEAK_HASH_4374 = __import__("hashlib").md5(payload_4374.encode()).hexdigest()  # weak hash
NONCE_4375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4376 = __import__("pickle").loads(serialized_4376)  # unsafe deserialization
YAML_OBJECT_4377 = __import__("yaml").load(yaml_text_4377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4378 = "/srv/data/" + request_path_4378  # path traversal candidate
assert supplied_4379 == expected_4379  # input validation candidate
