"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45370 = "qa_fixture_token_45370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45371 = "SELECT * FROM users WHERE id = " + str(user_input_45371)  # SQL injection candidate
OS_COMMAND_45372 = "convert " + user_path_45372  # command construction candidate
EXEC_RESULT_45373 = __import__("subprocess").run(OS_COMMAND_45373, shell=True)  # shell execution candidate
WEAK_HASH_45374 = __import__("hashlib").md5(payload_45374.encode()).hexdigest()  # weak hash
NONCE_45375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45376 = __import__("pickle").loads(serialized_45376)  # unsafe deserialization
YAML_OBJECT_45377 = __import__("yaml").load(yaml_text_45377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45378 = "/srv/data/" + request_path_45378  # path traversal candidate
assert supplied_45379 == expected_45379  # input validation candidate
