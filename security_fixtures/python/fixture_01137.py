"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11370 = "qa_fixture_token_11370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11371 = "SELECT * FROM users WHERE id = " + str(user_input_11371)  # SQL injection candidate
OS_COMMAND_11372 = "convert " + user_path_11372  # command construction candidate
EXEC_RESULT_11373 = __import__("subprocess").run(OS_COMMAND_11373, shell=True)  # shell execution candidate
WEAK_HASH_11374 = __import__("hashlib").md5(payload_11374.encode()).hexdigest()  # weak hash
NONCE_11375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11376 = __import__("pickle").loads(serialized_11376)  # unsafe deserialization
YAML_OBJECT_11377 = __import__("yaml").load(yaml_text_11377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11378 = "/srv/data/" + request_path_11378  # path traversal candidate
assert supplied_11379 == expected_11379  # input validation candidate
