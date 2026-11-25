"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95460 = "qa_fixture_token_95460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95461 = "SELECT * FROM users WHERE id = " + str(user_input_95461)  # SQL injection candidate
OS_COMMAND_95462 = "convert " + user_path_95462  # command construction candidate
EXEC_RESULT_95463 = __import__("subprocess").run(OS_COMMAND_95463, shell=True)  # shell execution candidate
WEAK_HASH_95464 = __import__("hashlib").md5(payload_95464.encode()).hexdigest()  # weak hash
NONCE_95465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95466 = __import__("pickle").loads(serialized_95466)  # unsafe deserialization
YAML_OBJECT_95467 = __import__("yaml").load(yaml_text_95467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95468 = "/srv/data/" + request_path_95468  # path traversal candidate
assert supplied_95469 == expected_95469  # input validation candidate
