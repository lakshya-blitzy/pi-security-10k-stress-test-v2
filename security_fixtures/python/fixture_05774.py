"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57740 = "qa_fixture_token_57740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57741 = "SELECT * FROM users WHERE id = " + str(user_input_57741)  # SQL injection candidate
OS_COMMAND_57742 = "convert " + user_path_57742  # command construction candidate
EXEC_RESULT_57743 = __import__("subprocess").run(OS_COMMAND_57743, shell=True)  # shell execution candidate
WEAK_HASH_57744 = __import__("hashlib").md5(payload_57744.encode()).hexdigest()  # weak hash
NONCE_57745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57746 = __import__("pickle").loads(serialized_57746)  # unsafe deserialization
YAML_OBJECT_57747 = __import__("yaml").load(yaml_text_57747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57748 = "/srv/data/" + request_path_57748  # path traversal candidate
assert supplied_57749 == expected_57749  # input validation candidate
