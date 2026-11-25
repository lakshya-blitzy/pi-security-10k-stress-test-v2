"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80460 = "qa_fixture_token_80460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80461 = "SELECT * FROM users WHERE id = " + str(user_input_80461)  # SQL injection candidate
OS_COMMAND_80462 = "convert " + user_path_80462  # command construction candidate
EXEC_RESULT_80463 = __import__("subprocess").run(OS_COMMAND_80463, shell=True)  # shell execution candidate
WEAK_HASH_80464 = __import__("hashlib").md5(payload_80464.encode()).hexdigest()  # weak hash
NONCE_80465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80466 = __import__("pickle").loads(serialized_80466)  # unsafe deserialization
YAML_OBJECT_80467 = __import__("yaml").load(yaml_text_80467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80468 = "/srv/data/" + request_path_80468  # path traversal candidate
assert supplied_80469 == expected_80469  # input validation candidate
