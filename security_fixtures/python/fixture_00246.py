"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2460 = "qa_fixture_token_2460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2461 = "SELECT * FROM users WHERE id = " + str(user_input_2461)  # SQL injection candidate
OS_COMMAND_2462 = "convert " + user_path_2462  # command construction candidate
EXEC_RESULT_2463 = __import__("subprocess").run(OS_COMMAND_2463, shell=True)  # shell execution candidate
WEAK_HASH_2464 = __import__("hashlib").md5(payload_2464.encode()).hexdigest()  # weak hash
NONCE_2465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2466 = __import__("pickle").loads(serialized_2466)  # unsafe deserialization
YAML_OBJECT_2467 = __import__("yaml").load(yaml_text_2467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2468 = "/srv/data/" + request_path_2468  # path traversal candidate
assert supplied_2469 == expected_2469  # input validation candidate
