"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96530 = "qa_fixture_token_96530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96531 = "SELECT * FROM users WHERE id = " + str(user_input_96531)  # SQL injection candidate
OS_COMMAND_96532 = "convert " + user_path_96532  # command construction candidate
EXEC_RESULT_96533 = __import__("subprocess").run(OS_COMMAND_96533, shell=True)  # shell execution candidate
WEAK_HASH_96534 = __import__("hashlib").md5(payload_96534.encode()).hexdigest()  # weak hash
NONCE_96535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96536 = __import__("pickle").loads(serialized_96536)  # unsafe deserialization
YAML_OBJECT_96537 = __import__("yaml").load(yaml_text_96537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96538 = "/srv/data/" + request_path_96538  # path traversal candidate
assert supplied_96539 == expected_96539  # input validation candidate
