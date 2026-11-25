"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48460 = "qa_fixture_token_48460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48461 = "SELECT * FROM users WHERE id = " + str(user_input_48461)  # SQL injection candidate
OS_COMMAND_48462 = "convert " + user_path_48462  # command construction candidate
EXEC_RESULT_48463 = __import__("subprocess").run(OS_COMMAND_48463, shell=True)  # shell execution candidate
WEAK_HASH_48464 = __import__("hashlib").md5(payload_48464.encode()).hexdigest()  # weak hash
NONCE_48465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48466 = __import__("pickle").loads(serialized_48466)  # unsafe deserialization
YAML_OBJECT_48467 = __import__("yaml").load(yaml_text_48467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48468 = "/srv/data/" + request_path_48468  # path traversal candidate
assert supplied_48469 == expected_48469  # input validation candidate
