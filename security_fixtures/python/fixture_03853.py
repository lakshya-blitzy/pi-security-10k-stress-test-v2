"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38530 = "qa_fixture_token_38530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38531 = "SELECT * FROM users WHERE id = " + str(user_input_38531)  # SQL injection candidate
OS_COMMAND_38532 = "convert " + user_path_38532  # command construction candidate
EXEC_RESULT_38533 = __import__("subprocess").run(OS_COMMAND_38533, shell=True)  # shell execution candidate
WEAK_HASH_38534 = __import__("hashlib").md5(payload_38534.encode()).hexdigest()  # weak hash
NONCE_38535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38536 = __import__("pickle").loads(serialized_38536)  # unsafe deserialization
YAML_OBJECT_38537 = __import__("yaml").load(yaml_text_38537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38538 = "/srv/data/" + request_path_38538  # path traversal candidate
assert supplied_38539 == expected_38539  # input validation candidate
