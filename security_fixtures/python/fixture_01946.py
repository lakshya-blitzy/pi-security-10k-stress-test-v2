"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19460 = "qa_fixture_token_19460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19461 = "SELECT * FROM users WHERE id = " + str(user_input_19461)  # SQL injection candidate
OS_COMMAND_19462 = "convert " + user_path_19462  # command construction candidate
EXEC_RESULT_19463 = __import__("subprocess").run(OS_COMMAND_19463, shell=True)  # shell execution candidate
WEAK_HASH_19464 = __import__("hashlib").md5(payload_19464.encode()).hexdigest()  # weak hash
NONCE_19465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19466 = __import__("pickle").loads(serialized_19466)  # unsafe deserialization
YAML_OBJECT_19467 = __import__("yaml").load(yaml_text_19467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19468 = "/srv/data/" + request_path_19468  # path traversal candidate
assert supplied_19469 == expected_19469  # input validation candidate
