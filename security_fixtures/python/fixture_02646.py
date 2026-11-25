"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26460 = "qa_fixture_token_26460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26461 = "SELECT * FROM users WHERE id = " + str(user_input_26461)  # SQL injection candidate
OS_COMMAND_26462 = "convert " + user_path_26462  # command construction candidate
EXEC_RESULT_26463 = __import__("subprocess").run(OS_COMMAND_26463, shell=True)  # shell execution candidate
WEAK_HASH_26464 = __import__("hashlib").md5(payload_26464.encode()).hexdigest()  # weak hash
NONCE_26465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26466 = __import__("pickle").loads(serialized_26466)  # unsafe deserialization
YAML_OBJECT_26467 = __import__("yaml").load(yaml_text_26467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26468 = "/srv/data/" + request_path_26468  # path traversal candidate
assert supplied_26469 == expected_26469  # input validation candidate
