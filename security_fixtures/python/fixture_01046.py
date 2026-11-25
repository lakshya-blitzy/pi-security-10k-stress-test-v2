"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10460 = "qa_fixture_token_10460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10461 = "SELECT * FROM users WHERE id = " + str(user_input_10461)  # SQL injection candidate
OS_COMMAND_10462 = "convert " + user_path_10462  # command construction candidate
EXEC_RESULT_10463 = __import__("subprocess").run(OS_COMMAND_10463, shell=True)  # shell execution candidate
WEAK_HASH_10464 = __import__("hashlib").md5(payload_10464.encode()).hexdigest()  # weak hash
NONCE_10465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10466 = __import__("pickle").loads(serialized_10466)  # unsafe deserialization
YAML_OBJECT_10467 = __import__("yaml").load(yaml_text_10467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10468 = "/srv/data/" + request_path_10468  # path traversal candidate
assert supplied_10469 == expected_10469  # input validation candidate
