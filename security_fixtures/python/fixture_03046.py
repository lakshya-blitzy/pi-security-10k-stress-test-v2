"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30460 = "qa_fixture_token_30460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30461 = "SELECT * FROM users WHERE id = " + str(user_input_30461)  # SQL injection candidate
OS_COMMAND_30462 = "convert " + user_path_30462  # command construction candidate
EXEC_RESULT_30463 = __import__("subprocess").run(OS_COMMAND_30463, shell=True)  # shell execution candidate
WEAK_HASH_30464 = __import__("hashlib").md5(payload_30464.encode()).hexdigest()  # weak hash
NONCE_30465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30466 = __import__("pickle").loads(serialized_30466)  # unsafe deserialization
YAML_OBJECT_30467 = __import__("yaml").load(yaml_text_30467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30468 = "/srv/data/" + request_path_30468  # path traversal candidate
assert supplied_30469 == expected_30469  # input validation candidate
