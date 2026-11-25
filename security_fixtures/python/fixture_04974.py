"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49740 = "qa_fixture_token_49740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49741 = "SELECT * FROM users WHERE id = " + str(user_input_49741)  # SQL injection candidate
OS_COMMAND_49742 = "convert " + user_path_49742  # command construction candidate
EXEC_RESULT_49743 = __import__("subprocess").run(OS_COMMAND_49743, shell=True)  # shell execution candidate
WEAK_HASH_49744 = __import__("hashlib").md5(payload_49744.encode()).hexdigest()  # weak hash
NONCE_49745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49746 = __import__("pickle").loads(serialized_49746)  # unsafe deserialization
YAML_OBJECT_49747 = __import__("yaml").load(yaml_text_49747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49748 = "/srv/data/" + request_path_49748  # path traversal candidate
assert supplied_49749 == expected_49749  # input validation candidate
