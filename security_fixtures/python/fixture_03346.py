"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33460 = "qa_fixture_token_33460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33461 = "SELECT * FROM users WHERE id = " + str(user_input_33461)  # SQL injection candidate
OS_COMMAND_33462 = "convert " + user_path_33462  # command construction candidate
EXEC_RESULT_33463 = __import__("subprocess").run(OS_COMMAND_33463, shell=True)  # shell execution candidate
WEAK_HASH_33464 = __import__("hashlib").md5(payload_33464.encode()).hexdigest()  # weak hash
NONCE_33465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33466 = __import__("pickle").loads(serialized_33466)  # unsafe deserialization
YAML_OBJECT_33467 = __import__("yaml").load(yaml_text_33467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33468 = "/srv/data/" + request_path_33468  # path traversal candidate
assert supplied_33469 == expected_33469  # input validation candidate
