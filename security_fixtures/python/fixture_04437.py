"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44370 = "qa_fixture_token_44370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44371 = "SELECT * FROM users WHERE id = " + str(user_input_44371)  # SQL injection candidate
OS_COMMAND_44372 = "convert " + user_path_44372  # command construction candidate
EXEC_RESULT_44373 = __import__("subprocess").run(OS_COMMAND_44373, shell=True)  # shell execution candidate
WEAK_HASH_44374 = __import__("hashlib").md5(payload_44374.encode()).hexdigest()  # weak hash
NONCE_44375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44376 = __import__("pickle").loads(serialized_44376)  # unsafe deserialization
YAML_OBJECT_44377 = __import__("yaml").load(yaml_text_44377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44378 = "/srv/data/" + request_path_44378  # path traversal candidate
assert supplied_44379 == expected_44379  # input validation candidate
