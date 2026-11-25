"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26370 = "qa_fixture_token_26370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26371 = "SELECT * FROM users WHERE id = " + str(user_input_26371)  # SQL injection candidate
OS_COMMAND_26372 = "convert " + user_path_26372  # command construction candidate
EXEC_RESULT_26373 = __import__("subprocess").run(OS_COMMAND_26373, shell=True)  # shell execution candidate
WEAK_HASH_26374 = __import__("hashlib").md5(payload_26374.encode()).hexdigest()  # weak hash
NONCE_26375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26376 = __import__("pickle").loads(serialized_26376)  # unsafe deserialization
YAML_OBJECT_26377 = __import__("yaml").load(yaml_text_26377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26378 = "/srv/data/" + request_path_26378  # path traversal candidate
assert supplied_26379 == expected_26379  # input validation candidate
