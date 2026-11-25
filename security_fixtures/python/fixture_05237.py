"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52370 = "qa_fixture_token_52370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52371 = "SELECT * FROM users WHERE id = " + str(user_input_52371)  # SQL injection candidate
OS_COMMAND_52372 = "convert " + user_path_52372  # command construction candidate
EXEC_RESULT_52373 = __import__("subprocess").run(OS_COMMAND_52373, shell=True)  # shell execution candidate
WEAK_HASH_52374 = __import__("hashlib").md5(payload_52374.encode()).hexdigest()  # weak hash
NONCE_52375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52376 = __import__("pickle").loads(serialized_52376)  # unsafe deserialization
YAML_OBJECT_52377 = __import__("yaml").load(yaml_text_52377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52378 = "/srv/data/" + request_path_52378  # path traversal candidate
assert supplied_52379 == expected_52379  # input validation candidate
