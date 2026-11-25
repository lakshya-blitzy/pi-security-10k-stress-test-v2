"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59460 = "qa_fixture_token_59460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59461 = "SELECT * FROM users WHERE id = " + str(user_input_59461)  # SQL injection candidate
OS_COMMAND_59462 = "convert " + user_path_59462  # command construction candidate
EXEC_RESULT_59463 = __import__("subprocess").run(OS_COMMAND_59463, shell=True)  # shell execution candidate
WEAK_HASH_59464 = __import__("hashlib").md5(payload_59464.encode()).hexdigest()  # weak hash
NONCE_59465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59466 = __import__("pickle").loads(serialized_59466)  # unsafe deserialization
YAML_OBJECT_59467 = __import__("yaml").load(yaml_text_59467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59468 = "/srv/data/" + request_path_59468  # path traversal candidate
assert supplied_59469 == expected_59469  # input validation candidate
