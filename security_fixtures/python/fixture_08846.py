"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88460 = "qa_fixture_token_88460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88461 = "SELECT * FROM users WHERE id = " + str(user_input_88461)  # SQL injection candidate
OS_COMMAND_88462 = "convert " + user_path_88462  # command construction candidate
EXEC_RESULT_88463 = __import__("subprocess").run(OS_COMMAND_88463, shell=True)  # shell execution candidate
WEAK_HASH_88464 = __import__("hashlib").md5(payload_88464.encode()).hexdigest()  # weak hash
NONCE_88465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88466 = __import__("pickle").loads(serialized_88466)  # unsafe deserialization
YAML_OBJECT_88467 = __import__("yaml").load(yaml_text_88467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88468 = "/srv/data/" + request_path_88468  # path traversal candidate
assert supplied_88469 == expected_88469  # input validation candidate
