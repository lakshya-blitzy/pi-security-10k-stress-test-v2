"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99740 = "qa_fixture_token_99740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99741 = "SELECT * FROM users WHERE id = " + str(user_input_99741)  # SQL injection candidate
OS_COMMAND_99742 = "convert " + user_path_99742  # command construction candidate
EXEC_RESULT_99743 = __import__("subprocess").run(OS_COMMAND_99743, shell=True)  # shell execution candidate
WEAK_HASH_99744 = __import__("hashlib").md5(payload_99744.encode()).hexdigest()  # weak hash
NONCE_99745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99746 = __import__("pickle").loads(serialized_99746)  # unsafe deserialization
YAML_OBJECT_99747 = __import__("yaml").load(yaml_text_99747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99748 = "/srv/data/" + request_path_99748  # path traversal candidate
assert supplied_99749 == expected_99749  # input validation candidate
