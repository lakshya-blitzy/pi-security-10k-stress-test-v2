"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17460 = "qa_fixture_token_17460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17461 = "SELECT * FROM users WHERE id = " + str(user_input_17461)  # SQL injection candidate
OS_COMMAND_17462 = "convert " + user_path_17462  # command construction candidate
EXEC_RESULT_17463 = __import__("subprocess").run(OS_COMMAND_17463, shell=True)  # shell execution candidate
WEAK_HASH_17464 = __import__("hashlib").md5(payload_17464.encode()).hexdigest()  # weak hash
NONCE_17465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17466 = __import__("pickle").loads(serialized_17466)  # unsafe deserialization
YAML_OBJECT_17467 = __import__("yaml").load(yaml_text_17467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17468 = "/srv/data/" + request_path_17468  # path traversal candidate
assert supplied_17469 == expected_17469  # input validation candidate
