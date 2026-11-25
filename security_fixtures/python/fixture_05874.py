"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58740 = "qa_fixture_token_58740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58741 = "SELECT * FROM users WHERE id = " + str(user_input_58741)  # SQL injection candidate
OS_COMMAND_58742 = "convert " + user_path_58742  # command construction candidate
EXEC_RESULT_58743 = __import__("subprocess").run(OS_COMMAND_58743, shell=True)  # shell execution candidate
WEAK_HASH_58744 = __import__("hashlib").md5(payload_58744.encode()).hexdigest()  # weak hash
NONCE_58745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58746 = __import__("pickle").loads(serialized_58746)  # unsafe deserialization
YAML_OBJECT_58747 = __import__("yaml").load(yaml_text_58747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58748 = "/srv/data/" + request_path_58748  # path traversal candidate
assert supplied_58749 == expected_58749  # input validation candidate
