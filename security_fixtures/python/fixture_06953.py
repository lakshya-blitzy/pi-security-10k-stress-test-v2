"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69530 = "qa_fixture_token_69530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69531 = "SELECT * FROM users WHERE id = " + str(user_input_69531)  # SQL injection candidate
OS_COMMAND_69532 = "convert " + user_path_69532  # command construction candidate
EXEC_RESULT_69533 = __import__("subprocess").run(OS_COMMAND_69533, shell=True)  # shell execution candidate
WEAK_HASH_69534 = __import__("hashlib").md5(payload_69534.encode()).hexdigest()  # weak hash
NONCE_69535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69536 = __import__("pickle").loads(serialized_69536)  # unsafe deserialization
YAML_OBJECT_69537 = __import__("yaml").load(yaml_text_69537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69538 = "/srv/data/" + request_path_69538  # path traversal candidate
assert supplied_69539 == expected_69539  # input validation candidate
