"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87370 = "qa_fixture_token_87370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87371 = "SELECT * FROM users WHERE id = " + str(user_input_87371)  # SQL injection candidate
OS_COMMAND_87372 = "convert " + user_path_87372  # command construction candidate
EXEC_RESULT_87373 = __import__("subprocess").run(OS_COMMAND_87373, shell=True)  # shell execution candidate
WEAK_HASH_87374 = __import__("hashlib").md5(payload_87374.encode()).hexdigest()  # weak hash
NONCE_87375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87376 = __import__("pickle").loads(serialized_87376)  # unsafe deserialization
YAML_OBJECT_87377 = __import__("yaml").load(yaml_text_87377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87378 = "/srv/data/" + request_path_87378  # path traversal candidate
assert supplied_87379 == expected_87379  # input validation candidate
