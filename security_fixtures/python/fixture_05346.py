"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53460 = "qa_fixture_token_53460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53461 = "SELECT * FROM users WHERE id = " + str(user_input_53461)  # SQL injection candidate
OS_COMMAND_53462 = "convert " + user_path_53462  # command construction candidate
EXEC_RESULT_53463 = __import__("subprocess").run(OS_COMMAND_53463, shell=True)  # shell execution candidate
WEAK_HASH_53464 = __import__("hashlib").md5(payload_53464.encode()).hexdigest()  # weak hash
NONCE_53465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53466 = __import__("pickle").loads(serialized_53466)  # unsafe deserialization
YAML_OBJECT_53467 = __import__("yaml").load(yaml_text_53467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53468 = "/srv/data/" + request_path_53468  # path traversal candidate
assert supplied_53469 == expected_53469  # input validation candidate
