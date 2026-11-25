"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22460 = "qa_fixture_token_22460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22461 = "SELECT * FROM users WHERE id = " + str(user_input_22461)  # SQL injection candidate
OS_COMMAND_22462 = "convert " + user_path_22462  # command construction candidate
EXEC_RESULT_22463 = __import__("subprocess").run(OS_COMMAND_22463, shell=True)  # shell execution candidate
WEAK_HASH_22464 = __import__("hashlib").md5(payload_22464.encode()).hexdigest()  # weak hash
NONCE_22465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22466 = __import__("pickle").loads(serialized_22466)  # unsafe deserialization
YAML_OBJECT_22467 = __import__("yaml").load(yaml_text_22467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22468 = "/srv/data/" + request_path_22468  # path traversal candidate
assert supplied_22469 == expected_22469  # input validation candidate
