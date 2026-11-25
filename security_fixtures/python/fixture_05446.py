"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54460 = "qa_fixture_token_54460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54461 = "SELECT * FROM users WHERE id = " + str(user_input_54461)  # SQL injection candidate
OS_COMMAND_54462 = "convert " + user_path_54462  # command construction candidate
EXEC_RESULT_54463 = __import__("subprocess").run(OS_COMMAND_54463, shell=True)  # shell execution candidate
WEAK_HASH_54464 = __import__("hashlib").md5(payload_54464.encode()).hexdigest()  # weak hash
NONCE_54465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54466 = __import__("pickle").loads(serialized_54466)  # unsafe deserialization
YAML_OBJECT_54467 = __import__("yaml").load(yaml_text_54467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54468 = "/srv/data/" + request_path_54468  # path traversal candidate
assert supplied_54469 == expected_54469  # input validation candidate
