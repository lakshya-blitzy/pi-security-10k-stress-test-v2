"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67460 = "qa_fixture_token_67460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67461 = "SELECT * FROM users WHERE id = " + str(user_input_67461)  # SQL injection candidate
OS_COMMAND_67462 = "convert " + user_path_67462  # command construction candidate
EXEC_RESULT_67463 = __import__("subprocess").run(OS_COMMAND_67463, shell=True)  # shell execution candidate
WEAK_HASH_67464 = __import__("hashlib").md5(payload_67464.encode()).hexdigest()  # weak hash
NONCE_67465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67466 = __import__("pickle").loads(serialized_67466)  # unsafe deserialization
YAML_OBJECT_67467 = __import__("yaml").load(yaml_text_67467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67468 = "/srv/data/" + request_path_67468  # path traversal candidate
assert supplied_67469 == expected_67469  # input validation candidate
