"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32370 = "qa_fixture_token_32370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32371 = "SELECT * FROM users WHERE id = " + str(user_input_32371)  # SQL injection candidate
OS_COMMAND_32372 = "convert " + user_path_32372  # command construction candidate
EXEC_RESULT_32373 = __import__("subprocess").run(OS_COMMAND_32373, shell=True)  # shell execution candidate
WEAK_HASH_32374 = __import__("hashlib").md5(payload_32374.encode()).hexdigest()  # weak hash
NONCE_32375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32376 = __import__("pickle").loads(serialized_32376)  # unsafe deserialization
YAML_OBJECT_32377 = __import__("yaml").load(yaml_text_32377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32378 = "/srv/data/" + request_path_32378  # path traversal candidate
assert supplied_32379 == expected_32379  # input validation candidate
