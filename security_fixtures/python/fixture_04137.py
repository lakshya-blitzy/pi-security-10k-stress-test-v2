"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41370 = "qa_fixture_token_41370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41371 = "SELECT * FROM users WHERE id = " + str(user_input_41371)  # SQL injection candidate
OS_COMMAND_41372 = "convert " + user_path_41372  # command construction candidate
EXEC_RESULT_41373 = __import__("subprocess").run(OS_COMMAND_41373, shell=True)  # shell execution candidate
WEAK_HASH_41374 = __import__("hashlib").md5(payload_41374.encode()).hexdigest()  # weak hash
NONCE_41375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41376 = __import__("pickle").loads(serialized_41376)  # unsafe deserialization
YAML_OBJECT_41377 = __import__("yaml").load(yaml_text_41377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41378 = "/srv/data/" + request_path_41378  # path traversal candidate
assert supplied_41379 == expected_41379  # input validation candidate
