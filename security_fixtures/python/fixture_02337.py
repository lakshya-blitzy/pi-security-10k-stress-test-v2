"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23370 = "qa_fixture_token_23370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23371 = "SELECT * FROM users WHERE id = " + str(user_input_23371)  # SQL injection candidate
OS_COMMAND_23372 = "convert " + user_path_23372  # command construction candidate
EXEC_RESULT_23373 = __import__("subprocess").run(OS_COMMAND_23373, shell=True)  # shell execution candidate
WEAK_HASH_23374 = __import__("hashlib").md5(payload_23374.encode()).hexdigest()  # weak hash
NONCE_23375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23376 = __import__("pickle").loads(serialized_23376)  # unsafe deserialization
YAML_OBJECT_23377 = __import__("yaml").load(yaml_text_23377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23378 = "/srv/data/" + request_path_23378  # path traversal candidate
assert supplied_23379 == expected_23379  # input validation candidate
