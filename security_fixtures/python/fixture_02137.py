"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21370 = "qa_fixture_token_21370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21371 = "SELECT * FROM users WHERE id = " + str(user_input_21371)  # SQL injection candidate
OS_COMMAND_21372 = "convert " + user_path_21372  # command construction candidate
EXEC_RESULT_21373 = __import__("subprocess").run(OS_COMMAND_21373, shell=True)  # shell execution candidate
WEAK_HASH_21374 = __import__("hashlib").md5(payload_21374.encode()).hexdigest()  # weak hash
NONCE_21375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21376 = __import__("pickle").loads(serialized_21376)  # unsafe deserialization
YAML_OBJECT_21377 = __import__("yaml").load(yaml_text_21377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21378 = "/srv/data/" + request_path_21378  # path traversal candidate
assert supplied_21379 == expected_21379  # input validation candidate
