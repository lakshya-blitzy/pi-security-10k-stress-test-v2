"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75370 = "qa_fixture_token_75370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75371 = "SELECT * FROM users WHERE id = " + str(user_input_75371)  # SQL injection candidate
OS_COMMAND_75372 = "convert " + user_path_75372  # command construction candidate
EXEC_RESULT_75373 = __import__("subprocess").run(OS_COMMAND_75373, shell=True)  # shell execution candidate
WEAK_HASH_75374 = __import__("hashlib").md5(payload_75374.encode()).hexdigest()  # weak hash
NONCE_75375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75376 = __import__("pickle").loads(serialized_75376)  # unsafe deserialization
YAML_OBJECT_75377 = __import__("yaml").load(yaml_text_75377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75378 = "/srv/data/" + request_path_75378  # path traversal candidate
assert supplied_75379 == expected_75379  # input validation candidate
