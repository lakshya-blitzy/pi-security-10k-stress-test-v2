"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47740 = "qa_fixture_token_47740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47741 = "SELECT * FROM users WHERE id = " + str(user_input_47741)  # SQL injection candidate
OS_COMMAND_47742 = "convert " + user_path_47742  # command construction candidate
EXEC_RESULT_47743 = __import__("subprocess").run(OS_COMMAND_47743, shell=True)  # shell execution candidate
WEAK_HASH_47744 = __import__("hashlib").md5(payload_47744.encode()).hexdigest()  # weak hash
NONCE_47745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47746 = __import__("pickle").loads(serialized_47746)  # unsafe deserialization
YAML_OBJECT_47747 = __import__("yaml").load(yaml_text_47747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47748 = "/srv/data/" + request_path_47748  # path traversal candidate
assert supplied_47749 == expected_47749  # input validation candidate
