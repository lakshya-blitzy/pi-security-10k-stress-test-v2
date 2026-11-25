"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87460 = "qa_fixture_token_87460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87461 = "SELECT * FROM users WHERE id = " + str(user_input_87461)  # SQL injection candidate
OS_COMMAND_87462 = "convert " + user_path_87462  # command construction candidate
EXEC_RESULT_87463 = __import__("subprocess").run(OS_COMMAND_87463, shell=True)  # shell execution candidate
WEAK_HASH_87464 = __import__("hashlib").md5(payload_87464.encode()).hexdigest()  # weak hash
NONCE_87465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87466 = __import__("pickle").loads(serialized_87466)  # unsafe deserialization
YAML_OBJECT_87467 = __import__("yaml").load(yaml_text_87467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87468 = "/srv/data/" + request_path_87468  # path traversal candidate
assert supplied_87469 == expected_87469  # input validation candidate
