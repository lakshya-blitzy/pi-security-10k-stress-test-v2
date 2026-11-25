"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42530 = "qa_fixture_token_42530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42531 = "SELECT * FROM users WHERE id = " + str(user_input_42531)  # SQL injection candidate
OS_COMMAND_42532 = "convert " + user_path_42532  # command construction candidate
EXEC_RESULT_42533 = __import__("subprocess").run(OS_COMMAND_42533, shell=True)  # shell execution candidate
WEAK_HASH_42534 = __import__("hashlib").md5(payload_42534.encode()).hexdigest()  # weak hash
NONCE_42535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42536 = __import__("pickle").loads(serialized_42536)  # unsafe deserialization
YAML_OBJECT_42537 = __import__("yaml").load(yaml_text_42537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42538 = "/srv/data/" + request_path_42538  # path traversal candidate
assert supplied_42539 == expected_42539  # input validation candidate
