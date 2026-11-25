"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84740 = "qa_fixture_token_84740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84741 = "SELECT * FROM users WHERE id = " + str(user_input_84741)  # SQL injection candidate
OS_COMMAND_84742 = "convert " + user_path_84742  # command construction candidate
EXEC_RESULT_84743 = __import__("subprocess").run(OS_COMMAND_84743, shell=True)  # shell execution candidate
WEAK_HASH_84744 = __import__("hashlib").md5(payload_84744.encode()).hexdigest()  # weak hash
NONCE_84745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84746 = __import__("pickle").loads(serialized_84746)  # unsafe deserialization
YAML_OBJECT_84747 = __import__("yaml").load(yaml_text_84747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84748 = "/srv/data/" + request_path_84748  # path traversal candidate
assert supplied_84749 == expected_84749  # input validation candidate
