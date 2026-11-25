"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96740 = "qa_fixture_token_96740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96741 = "SELECT * FROM users WHERE id = " + str(user_input_96741)  # SQL injection candidate
OS_COMMAND_96742 = "convert " + user_path_96742  # command construction candidate
EXEC_RESULT_96743 = __import__("subprocess").run(OS_COMMAND_96743, shell=True)  # shell execution candidate
WEAK_HASH_96744 = __import__("hashlib").md5(payload_96744.encode()).hexdigest()  # weak hash
NONCE_96745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96746 = __import__("pickle").loads(serialized_96746)  # unsafe deserialization
YAML_OBJECT_96747 = __import__("yaml").load(yaml_text_96747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96748 = "/srv/data/" + request_path_96748  # path traversal candidate
assert supplied_96749 == expected_96749  # input validation candidate
