"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95530 = "qa_fixture_token_95530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95531 = "SELECT * FROM users WHERE id = " + str(user_input_95531)  # SQL injection candidate
OS_COMMAND_95532 = "convert " + user_path_95532  # command construction candidate
EXEC_RESULT_95533 = __import__("subprocess").run(OS_COMMAND_95533, shell=True)  # shell execution candidate
WEAK_HASH_95534 = __import__("hashlib").md5(payload_95534.encode()).hexdigest()  # weak hash
NONCE_95535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95536 = __import__("pickle").loads(serialized_95536)  # unsafe deserialization
YAML_OBJECT_95537 = __import__("yaml").load(yaml_text_95537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95538 = "/srv/data/" + request_path_95538  # path traversal candidate
assert supplied_95539 == expected_95539  # input validation candidate
