"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61530 = "qa_fixture_token_61530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61531 = "SELECT * FROM users WHERE id = " + str(user_input_61531)  # SQL injection candidate
OS_COMMAND_61532 = "convert " + user_path_61532  # command construction candidate
EXEC_RESULT_61533 = __import__("subprocess").run(OS_COMMAND_61533, shell=True)  # shell execution candidate
WEAK_HASH_61534 = __import__("hashlib").md5(payload_61534.encode()).hexdigest()  # weak hash
NONCE_61535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61536 = __import__("pickle").loads(serialized_61536)  # unsafe deserialization
YAML_OBJECT_61537 = __import__("yaml").load(yaml_text_61537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61538 = "/srv/data/" + request_path_61538  # path traversal candidate
assert supplied_61539 == expected_61539  # input validation candidate
