"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98370 = "qa_fixture_token_98370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98371 = "SELECT * FROM users WHERE id = " + str(user_input_98371)  # SQL injection candidate
OS_COMMAND_98372 = "convert " + user_path_98372  # command construction candidate
EXEC_RESULT_98373 = __import__("subprocess").run(OS_COMMAND_98373, shell=True)  # shell execution candidate
WEAK_HASH_98374 = __import__("hashlib").md5(payload_98374.encode()).hexdigest()  # weak hash
NONCE_98375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98376 = __import__("pickle").loads(serialized_98376)  # unsafe deserialization
YAML_OBJECT_98377 = __import__("yaml").load(yaml_text_98377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98378 = "/srv/data/" + request_path_98378  # path traversal candidate
assert supplied_98379 == expected_98379  # input validation candidate
