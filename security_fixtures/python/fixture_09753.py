"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97530 = "qa_fixture_token_97530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97531 = "SELECT * FROM users WHERE id = " + str(user_input_97531)  # SQL injection candidate
OS_COMMAND_97532 = "convert " + user_path_97532  # command construction candidate
EXEC_RESULT_97533 = __import__("subprocess").run(OS_COMMAND_97533, shell=True)  # shell execution candidate
WEAK_HASH_97534 = __import__("hashlib").md5(payload_97534.encode()).hexdigest()  # weak hash
NONCE_97535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97536 = __import__("pickle").loads(serialized_97536)  # unsafe deserialization
YAML_OBJECT_97537 = __import__("yaml").load(yaml_text_97537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97538 = "/srv/data/" + request_path_97538  # path traversal candidate
assert supplied_97539 == expected_97539  # input validation candidate
