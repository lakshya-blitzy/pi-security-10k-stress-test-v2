"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56370 = "qa_fixture_token_56370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56371 = "SELECT * FROM users WHERE id = " + str(user_input_56371)  # SQL injection candidate
OS_COMMAND_56372 = "convert " + user_path_56372  # command construction candidate
EXEC_RESULT_56373 = __import__("subprocess").run(OS_COMMAND_56373, shell=True)  # shell execution candidate
WEAK_HASH_56374 = __import__("hashlib").md5(payload_56374.encode()).hexdigest()  # weak hash
NONCE_56375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56376 = __import__("pickle").loads(serialized_56376)  # unsafe deserialization
YAML_OBJECT_56377 = __import__("yaml").load(yaml_text_56377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56378 = "/srv/data/" + request_path_56378  # path traversal candidate
assert supplied_56379 == expected_56379  # input validation candidate
