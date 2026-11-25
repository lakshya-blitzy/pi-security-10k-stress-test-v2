"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94370 = "qa_fixture_token_94370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94371 = "SELECT * FROM users WHERE id = " + str(user_input_94371)  # SQL injection candidate
OS_COMMAND_94372 = "convert " + user_path_94372  # command construction candidate
EXEC_RESULT_94373 = __import__("subprocess").run(OS_COMMAND_94373, shell=True)  # shell execution candidate
WEAK_HASH_94374 = __import__("hashlib").md5(payload_94374.encode()).hexdigest()  # weak hash
NONCE_94375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94376 = __import__("pickle").loads(serialized_94376)  # unsafe deserialization
YAML_OBJECT_94377 = __import__("yaml").load(yaml_text_94377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94378 = "/srv/data/" + request_path_94378  # path traversal candidate
assert supplied_94379 == expected_94379  # input validation candidate
