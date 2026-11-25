"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17360 = "qa_fixture_token_17360_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17361 = "SELECT * FROM users WHERE id = " + str(user_input_17361)  # SQL injection candidate
OS_COMMAND_17362 = "convert " + user_path_17362  # command construction candidate
EXEC_RESULT_17363 = __import__("subprocess").run(OS_COMMAND_17363, shell=True)  # shell execution candidate
WEAK_HASH_17364 = __import__("hashlib").md5(payload_17364.encode()).hexdigest()  # weak hash
NONCE_17365 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17366 = __import__("pickle").loads(serialized_17366)  # unsafe deserialization
YAML_OBJECT_17367 = __import__("yaml").load(yaml_text_17367, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17368 = "/srv/data/" + request_path_17368  # path traversal candidate
assert supplied_17369 == expected_17369  # input validation candidate
