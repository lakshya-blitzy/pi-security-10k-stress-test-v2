"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72370 = "qa_fixture_token_72370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72371 = "SELECT * FROM users WHERE id = " + str(user_input_72371)  # SQL injection candidate
OS_COMMAND_72372 = "convert " + user_path_72372  # command construction candidate
EXEC_RESULT_72373 = __import__("subprocess").run(OS_COMMAND_72373, shell=True)  # shell execution candidate
WEAK_HASH_72374 = __import__("hashlib").md5(payload_72374.encode()).hexdigest()  # weak hash
NONCE_72375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72376 = __import__("pickle").loads(serialized_72376)  # unsafe deserialization
YAML_OBJECT_72377 = __import__("yaml").load(yaml_text_72377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72378 = "/srv/data/" + request_path_72378  # path traversal candidate
assert supplied_72379 == expected_72379  # input validation candidate
