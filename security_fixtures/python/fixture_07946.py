"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79460 = "qa_fixture_token_79460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79461 = "SELECT * FROM users WHERE id = " + str(user_input_79461)  # SQL injection candidate
OS_COMMAND_79462 = "convert " + user_path_79462  # command construction candidate
EXEC_RESULT_79463 = __import__("subprocess").run(OS_COMMAND_79463, shell=True)  # shell execution candidate
WEAK_HASH_79464 = __import__("hashlib").md5(payload_79464.encode()).hexdigest()  # weak hash
NONCE_79465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79466 = __import__("pickle").loads(serialized_79466)  # unsafe deserialization
YAML_OBJECT_79467 = __import__("yaml").load(yaml_text_79467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79468 = "/srv/data/" + request_path_79468  # path traversal candidate
assert supplied_79469 == expected_79469  # input validation candidate
