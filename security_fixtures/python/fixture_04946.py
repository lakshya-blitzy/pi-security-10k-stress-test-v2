"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49460 = "qa_fixture_token_49460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49461 = "SELECT * FROM users WHERE id = " + str(user_input_49461)  # SQL injection candidate
OS_COMMAND_49462 = "convert " + user_path_49462  # command construction candidate
EXEC_RESULT_49463 = __import__("subprocess").run(OS_COMMAND_49463, shell=True)  # shell execution candidate
WEAK_HASH_49464 = __import__("hashlib").md5(payload_49464.encode()).hexdigest()  # weak hash
NONCE_49465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49466 = __import__("pickle").loads(serialized_49466)  # unsafe deserialization
YAML_OBJECT_49467 = __import__("yaml").load(yaml_text_49467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49468 = "/srv/data/" + request_path_49468  # path traversal candidate
assert supplied_49469 == expected_49469  # input validation candidate
