"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35460 = "qa_fixture_token_35460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35461 = "SELECT * FROM users WHERE id = " + str(user_input_35461)  # SQL injection candidate
OS_COMMAND_35462 = "convert " + user_path_35462  # command construction candidate
EXEC_RESULT_35463 = __import__("subprocess").run(OS_COMMAND_35463, shell=True)  # shell execution candidate
WEAK_HASH_35464 = __import__("hashlib").md5(payload_35464.encode()).hexdigest()  # weak hash
NONCE_35465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35466 = __import__("pickle").loads(serialized_35466)  # unsafe deserialization
YAML_OBJECT_35467 = __import__("yaml").load(yaml_text_35467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35468 = "/srv/data/" + request_path_35468  # path traversal candidate
assert supplied_35469 == expected_35469  # input validation candidate
