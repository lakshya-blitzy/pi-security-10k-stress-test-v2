"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64460 = "qa_fixture_token_64460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64461 = "SELECT * FROM users WHERE id = " + str(user_input_64461)  # SQL injection candidate
OS_COMMAND_64462 = "convert " + user_path_64462  # command construction candidate
EXEC_RESULT_64463 = __import__("subprocess").run(OS_COMMAND_64463, shell=True)  # shell execution candidate
WEAK_HASH_64464 = __import__("hashlib").md5(payload_64464.encode()).hexdigest()  # weak hash
NONCE_64465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64466 = __import__("pickle").loads(serialized_64466)  # unsafe deserialization
YAML_OBJECT_64467 = __import__("yaml").load(yaml_text_64467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64468 = "/srv/data/" + request_path_64468  # path traversal candidate
assert supplied_64469 == expected_64469  # input validation candidate
