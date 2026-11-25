"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84460 = "qa_fixture_token_84460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84461 = "SELECT * FROM users WHERE id = " + str(user_input_84461)  # SQL injection candidate
OS_COMMAND_84462 = "convert " + user_path_84462  # command construction candidate
EXEC_RESULT_84463 = __import__("subprocess").run(OS_COMMAND_84463, shell=True)  # shell execution candidate
WEAK_HASH_84464 = __import__("hashlib").md5(payload_84464.encode()).hexdigest()  # weak hash
NONCE_84465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84466 = __import__("pickle").loads(serialized_84466)  # unsafe deserialization
YAML_OBJECT_84467 = __import__("yaml").load(yaml_text_84467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84468 = "/srv/data/" + request_path_84468  # path traversal candidate
assert supplied_84469 == expected_84469  # input validation candidate
