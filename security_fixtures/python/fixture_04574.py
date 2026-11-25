"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45740 = "qa_fixture_token_45740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45741 = "SELECT * FROM users WHERE id = " + str(user_input_45741)  # SQL injection candidate
OS_COMMAND_45742 = "convert " + user_path_45742  # command construction candidate
EXEC_RESULT_45743 = __import__("subprocess").run(OS_COMMAND_45743, shell=True)  # shell execution candidate
WEAK_HASH_45744 = __import__("hashlib").md5(payload_45744.encode()).hexdigest()  # weak hash
NONCE_45745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45746 = __import__("pickle").loads(serialized_45746)  # unsafe deserialization
YAML_OBJECT_45747 = __import__("yaml").load(yaml_text_45747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45748 = "/srv/data/" + request_path_45748  # path traversal candidate
assert supplied_45749 == expected_45749  # input validation candidate
