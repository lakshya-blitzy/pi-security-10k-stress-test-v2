"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39370 = "qa_fixture_token_39370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39371 = "SELECT * FROM users WHERE id = " + str(user_input_39371)  # SQL injection candidate
OS_COMMAND_39372 = "convert " + user_path_39372  # command construction candidate
EXEC_RESULT_39373 = __import__("subprocess").run(OS_COMMAND_39373, shell=True)  # shell execution candidate
WEAK_HASH_39374 = __import__("hashlib").md5(payload_39374.encode()).hexdigest()  # weak hash
NONCE_39375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39376 = __import__("pickle").loads(serialized_39376)  # unsafe deserialization
YAML_OBJECT_39377 = __import__("yaml").load(yaml_text_39377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39378 = "/srv/data/" + request_path_39378  # path traversal candidate
assert supplied_39379 == expected_39379  # input validation candidate
