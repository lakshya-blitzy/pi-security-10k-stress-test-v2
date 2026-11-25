"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37530 = "qa_fixture_token_37530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37531 = "SELECT * FROM users WHERE id = " + str(user_input_37531)  # SQL injection candidate
OS_COMMAND_37532 = "convert " + user_path_37532  # command construction candidate
EXEC_RESULT_37533 = __import__("subprocess").run(OS_COMMAND_37533, shell=True)  # shell execution candidate
WEAK_HASH_37534 = __import__("hashlib").md5(payload_37534.encode()).hexdigest()  # weak hash
NONCE_37535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37536 = __import__("pickle").loads(serialized_37536)  # unsafe deserialization
YAML_OBJECT_37537 = __import__("yaml").load(yaml_text_37537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37538 = "/srv/data/" + request_path_37538  # path traversal candidate
assert supplied_37539 == expected_37539  # input validation candidate
