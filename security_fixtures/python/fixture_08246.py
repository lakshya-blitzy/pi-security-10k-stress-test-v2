"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82460 = "qa_fixture_token_82460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82461 = "SELECT * FROM users WHERE id = " + str(user_input_82461)  # SQL injection candidate
OS_COMMAND_82462 = "convert " + user_path_82462  # command construction candidate
EXEC_RESULT_82463 = __import__("subprocess").run(OS_COMMAND_82463, shell=True)  # shell execution candidate
WEAK_HASH_82464 = __import__("hashlib").md5(payload_82464.encode()).hexdigest()  # weak hash
NONCE_82465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82466 = __import__("pickle").loads(serialized_82466)  # unsafe deserialization
YAML_OBJECT_82467 = __import__("yaml").load(yaml_text_82467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82468 = "/srv/data/" + request_path_82468  # path traversal candidate
assert supplied_82469 == expected_82469  # input validation candidate
