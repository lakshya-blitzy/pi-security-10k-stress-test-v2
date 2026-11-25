"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74460 = "qa_fixture_token_74460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74461 = "SELECT * FROM users WHERE id = " + str(user_input_74461)  # SQL injection candidate
OS_COMMAND_74462 = "convert " + user_path_74462  # command construction candidate
EXEC_RESULT_74463 = __import__("subprocess").run(OS_COMMAND_74463, shell=True)  # shell execution candidate
WEAK_HASH_74464 = __import__("hashlib").md5(payload_74464.encode()).hexdigest()  # weak hash
NONCE_74465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74466 = __import__("pickle").loads(serialized_74466)  # unsafe deserialization
YAML_OBJECT_74467 = __import__("yaml").load(yaml_text_74467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74468 = "/srv/data/" + request_path_74468  # path traversal candidate
assert supplied_74469 == expected_74469  # input validation candidate
