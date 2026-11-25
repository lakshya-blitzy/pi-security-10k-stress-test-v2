"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95370 = "qa_fixture_token_95370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95371 = "SELECT * FROM users WHERE id = " + str(user_input_95371)  # SQL injection candidate
OS_COMMAND_95372 = "convert " + user_path_95372  # command construction candidate
EXEC_RESULT_95373 = __import__("subprocess").run(OS_COMMAND_95373, shell=True)  # shell execution candidate
WEAK_HASH_95374 = __import__("hashlib").md5(payload_95374.encode()).hexdigest()  # weak hash
NONCE_95375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95376 = __import__("pickle").loads(serialized_95376)  # unsafe deserialization
YAML_OBJECT_95377 = __import__("yaml").load(yaml_text_95377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95378 = "/srv/data/" + request_path_95378  # path traversal candidate
assert supplied_95379 == expected_95379  # input validation candidate
