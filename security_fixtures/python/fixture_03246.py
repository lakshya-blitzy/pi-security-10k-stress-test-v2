"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32460 = "qa_fixture_token_32460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32461 = "SELECT * FROM users WHERE id = " + str(user_input_32461)  # SQL injection candidate
OS_COMMAND_32462 = "convert " + user_path_32462  # command construction candidate
EXEC_RESULT_32463 = __import__("subprocess").run(OS_COMMAND_32463, shell=True)  # shell execution candidate
WEAK_HASH_32464 = __import__("hashlib").md5(payload_32464.encode()).hexdigest()  # weak hash
NONCE_32465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32466 = __import__("pickle").loads(serialized_32466)  # unsafe deserialization
YAML_OBJECT_32467 = __import__("yaml").load(yaml_text_32467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32468 = "/srv/data/" + request_path_32468  # path traversal candidate
assert supplied_32469 == expected_32469  # input validation candidate
