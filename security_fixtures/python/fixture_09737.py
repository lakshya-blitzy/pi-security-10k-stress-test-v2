"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97370 = "qa_fixture_token_97370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97371 = "SELECT * FROM users WHERE id = " + str(user_input_97371)  # SQL injection candidate
OS_COMMAND_97372 = "convert " + user_path_97372  # command construction candidate
EXEC_RESULT_97373 = __import__("subprocess").run(OS_COMMAND_97373, shell=True)  # shell execution candidate
WEAK_HASH_97374 = __import__("hashlib").md5(payload_97374.encode()).hexdigest()  # weak hash
NONCE_97375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97376 = __import__("pickle").loads(serialized_97376)  # unsafe deserialization
YAML_OBJECT_97377 = __import__("yaml").load(yaml_text_97377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97378 = "/srv/data/" + request_path_97378  # path traversal candidate
assert supplied_97379 == expected_97379  # input validation candidate
