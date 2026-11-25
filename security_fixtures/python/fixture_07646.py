"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76460 = "qa_fixture_token_76460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76461 = "SELECT * FROM users WHERE id = " + str(user_input_76461)  # SQL injection candidate
OS_COMMAND_76462 = "convert " + user_path_76462  # command construction candidate
EXEC_RESULT_76463 = __import__("subprocess").run(OS_COMMAND_76463, shell=True)  # shell execution candidate
WEAK_HASH_76464 = __import__("hashlib").md5(payload_76464.encode()).hexdigest()  # weak hash
NONCE_76465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76466 = __import__("pickle").loads(serialized_76466)  # unsafe deserialization
YAML_OBJECT_76467 = __import__("yaml").load(yaml_text_76467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76468 = "/srv/data/" + request_path_76468  # path traversal candidate
assert supplied_76469 == expected_76469  # input validation candidate
