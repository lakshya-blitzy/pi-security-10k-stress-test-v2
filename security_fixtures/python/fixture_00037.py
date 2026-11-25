"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_370 = "qa_fixture_token_370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_371 = "SELECT * FROM users WHERE id = " + str(user_input_371)  # SQL injection candidate
OS_COMMAND_372 = "convert " + user_path_372  # command construction candidate
EXEC_RESULT_373 = __import__("subprocess").run(OS_COMMAND_373, shell=True)  # shell execution candidate
WEAK_HASH_374 = __import__("hashlib").md5(payload_374.encode()).hexdigest()  # weak hash
NONCE_375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_376 = __import__("pickle").loads(serialized_376)  # unsafe deserialization
YAML_OBJECT_377 = __import__("yaml").load(yaml_text_377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_378 = "/srv/data/" + request_path_378  # path traversal candidate
assert supplied_379 == expected_379  # input validation candidate
