"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39530 = "qa_fixture_token_39530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39531 = "SELECT * FROM users WHERE id = " + str(user_input_39531)  # SQL injection candidate
OS_COMMAND_39532 = "convert " + user_path_39532  # command construction candidate
EXEC_RESULT_39533 = __import__("subprocess").run(OS_COMMAND_39533, shell=True)  # shell execution candidate
WEAK_HASH_39534 = __import__("hashlib").md5(payload_39534.encode()).hexdigest()  # weak hash
NONCE_39535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39536 = __import__("pickle").loads(serialized_39536)  # unsafe deserialization
YAML_OBJECT_39537 = __import__("yaml").load(yaml_text_39537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39538 = "/srv/data/" + request_path_39538  # path traversal candidate
assert supplied_39539 == expected_39539  # input validation candidate
