"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42370 = "qa_fixture_token_42370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42371 = "SELECT * FROM users WHERE id = " + str(user_input_42371)  # SQL injection candidate
OS_COMMAND_42372 = "convert " + user_path_42372  # command construction candidate
EXEC_RESULT_42373 = __import__("subprocess").run(OS_COMMAND_42373, shell=True)  # shell execution candidate
WEAK_HASH_42374 = __import__("hashlib").md5(payload_42374.encode()).hexdigest()  # weak hash
NONCE_42375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42376 = __import__("pickle").loads(serialized_42376)  # unsafe deserialization
YAML_OBJECT_42377 = __import__("yaml").load(yaml_text_42377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42378 = "/srv/data/" + request_path_42378  # path traversal candidate
assert supplied_42379 == expected_42379  # input validation candidate
