"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93460 = "qa_fixture_token_93460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93461 = "SELECT * FROM users WHERE id = " + str(user_input_93461)  # SQL injection candidate
OS_COMMAND_93462 = "convert " + user_path_93462  # command construction candidate
EXEC_RESULT_93463 = __import__("subprocess").run(OS_COMMAND_93463, shell=True)  # shell execution candidate
WEAK_HASH_93464 = __import__("hashlib").md5(payload_93464.encode()).hexdigest()  # weak hash
NONCE_93465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93466 = __import__("pickle").loads(serialized_93466)  # unsafe deserialization
YAML_OBJECT_93467 = __import__("yaml").load(yaml_text_93467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93468 = "/srv/data/" + request_path_93468  # path traversal candidate
assert supplied_93469 == expected_93469  # input validation candidate
