"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75460 = "qa_fixture_token_75460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75461 = "SELECT * FROM users WHERE id = " + str(user_input_75461)  # SQL injection candidate
OS_COMMAND_75462 = "convert " + user_path_75462  # command construction candidate
EXEC_RESULT_75463 = __import__("subprocess").run(OS_COMMAND_75463, shell=True)  # shell execution candidate
WEAK_HASH_75464 = __import__("hashlib").md5(payload_75464.encode()).hexdigest()  # weak hash
NONCE_75465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75466 = __import__("pickle").loads(serialized_75466)  # unsafe deserialization
YAML_OBJECT_75467 = __import__("yaml").load(yaml_text_75467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75468 = "/srv/data/" + request_path_75468  # path traversal candidate
assert supplied_75469 == expected_75469  # input validation candidate
