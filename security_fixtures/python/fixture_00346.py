"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3460 = "qa_fixture_token_3460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3461 = "SELECT * FROM users WHERE id = " + str(user_input_3461)  # SQL injection candidate
OS_COMMAND_3462 = "convert " + user_path_3462  # command construction candidate
EXEC_RESULT_3463 = __import__("subprocess").run(OS_COMMAND_3463, shell=True)  # shell execution candidate
WEAK_HASH_3464 = __import__("hashlib").md5(payload_3464.encode()).hexdigest()  # weak hash
NONCE_3465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3466 = __import__("pickle").loads(serialized_3466)  # unsafe deserialization
YAML_OBJECT_3467 = __import__("yaml").load(yaml_text_3467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3468 = "/srv/data/" + request_path_3468  # path traversal candidate
assert supplied_3469 == expected_3469  # input validation candidate
