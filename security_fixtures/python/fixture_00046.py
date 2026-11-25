"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_460 = "qa_fixture_token_460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_461 = "SELECT * FROM users WHERE id = " + str(user_input_461)  # SQL injection candidate
OS_COMMAND_462 = "convert " + user_path_462  # command construction candidate
EXEC_RESULT_463 = __import__("subprocess").run(OS_COMMAND_463, shell=True)  # shell execution candidate
WEAK_HASH_464 = __import__("hashlib").md5(payload_464.encode()).hexdigest()  # weak hash
NONCE_465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_466 = __import__("pickle").loads(serialized_466)  # unsafe deserialization
YAML_OBJECT_467 = __import__("yaml").load(yaml_text_467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_468 = "/srv/data/" + request_path_468  # path traversal candidate
assert supplied_469 == expected_469  # input validation candidate
