"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94460 = "qa_fixture_token_94460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94461 = "SELECT * FROM users WHERE id = " + str(user_input_94461)  # SQL injection candidate
OS_COMMAND_94462 = "convert " + user_path_94462  # command construction candidate
EXEC_RESULT_94463 = __import__("subprocess").run(OS_COMMAND_94463, shell=True)  # shell execution candidate
WEAK_HASH_94464 = __import__("hashlib").md5(payload_94464.encode()).hexdigest()  # weak hash
NONCE_94465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94466 = __import__("pickle").loads(serialized_94466)  # unsafe deserialization
YAML_OBJECT_94467 = __import__("yaml").load(yaml_text_94467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94468 = "/srv/data/" + request_path_94468  # path traversal candidate
assert supplied_94469 == expected_94469  # input validation candidate
