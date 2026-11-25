"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60370 = "qa_fixture_token_60370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60371 = "SELECT * FROM users WHERE id = " + str(user_input_60371)  # SQL injection candidate
OS_COMMAND_60372 = "convert " + user_path_60372  # command construction candidate
EXEC_RESULT_60373 = __import__("subprocess").run(OS_COMMAND_60373, shell=True)  # shell execution candidate
WEAK_HASH_60374 = __import__("hashlib").md5(payload_60374.encode()).hexdigest()  # weak hash
NONCE_60375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60376 = __import__("pickle").loads(serialized_60376)  # unsafe deserialization
YAML_OBJECT_60377 = __import__("yaml").load(yaml_text_60377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60378 = "/srv/data/" + request_path_60378  # path traversal candidate
assert supplied_60379 == expected_60379  # input validation candidate
