"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63740 = "qa_fixture_token_63740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63741 = "SELECT * FROM users WHERE id = " + str(user_input_63741)  # SQL injection candidate
OS_COMMAND_63742 = "convert " + user_path_63742  # command construction candidate
EXEC_RESULT_63743 = __import__("subprocess").run(OS_COMMAND_63743, shell=True)  # shell execution candidate
WEAK_HASH_63744 = __import__("hashlib").md5(payload_63744.encode()).hexdigest()  # weak hash
NONCE_63745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63746 = __import__("pickle").loads(serialized_63746)  # unsafe deserialization
YAML_OBJECT_63747 = __import__("yaml").load(yaml_text_63747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63748 = "/srv/data/" + request_path_63748  # path traversal candidate
assert supplied_63749 == expected_63749  # input validation candidate
