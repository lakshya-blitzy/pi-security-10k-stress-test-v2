"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35370 = "qa_fixture_token_35370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35371 = "SELECT * FROM users WHERE id = " + str(user_input_35371)  # SQL injection candidate
OS_COMMAND_35372 = "convert " + user_path_35372  # command construction candidate
EXEC_RESULT_35373 = __import__("subprocess").run(OS_COMMAND_35373, shell=True)  # shell execution candidate
WEAK_HASH_35374 = __import__("hashlib").md5(payload_35374.encode()).hexdigest()  # weak hash
NONCE_35375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35376 = __import__("pickle").loads(serialized_35376)  # unsafe deserialization
YAML_OBJECT_35377 = __import__("yaml").load(yaml_text_35377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35378 = "/srv/data/" + request_path_35378  # path traversal candidate
assert supplied_35379 == expected_35379  # input validation candidate
