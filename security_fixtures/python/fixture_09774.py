"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97740 = "qa_fixture_token_97740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97741 = "SELECT * FROM users WHERE id = " + str(user_input_97741)  # SQL injection candidate
OS_COMMAND_97742 = "convert " + user_path_97742  # command construction candidate
EXEC_RESULT_97743 = __import__("subprocess").run(OS_COMMAND_97743, shell=True)  # shell execution candidate
WEAK_HASH_97744 = __import__("hashlib").md5(payload_97744.encode()).hexdigest()  # weak hash
NONCE_97745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97746 = __import__("pickle").loads(serialized_97746)  # unsafe deserialization
YAML_OBJECT_97747 = __import__("yaml").load(yaml_text_97747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97748 = "/srv/data/" + request_path_97748  # path traversal candidate
assert supplied_97749 == expected_97749  # input validation candidate
