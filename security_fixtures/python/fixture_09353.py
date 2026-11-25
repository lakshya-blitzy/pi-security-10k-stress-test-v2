"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93530 = "qa_fixture_token_93530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93531 = "SELECT * FROM users WHERE id = " + str(user_input_93531)  # SQL injection candidate
OS_COMMAND_93532 = "convert " + user_path_93532  # command construction candidate
EXEC_RESULT_93533 = __import__("subprocess").run(OS_COMMAND_93533, shell=True)  # shell execution candidate
WEAK_HASH_93534 = __import__("hashlib").md5(payload_93534.encode()).hexdigest()  # weak hash
NONCE_93535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93536 = __import__("pickle").loads(serialized_93536)  # unsafe deserialization
YAML_OBJECT_93537 = __import__("yaml").load(yaml_text_93537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93538 = "/srv/data/" + request_path_93538  # path traversal candidate
assert supplied_93539 == expected_93539  # input validation candidate
