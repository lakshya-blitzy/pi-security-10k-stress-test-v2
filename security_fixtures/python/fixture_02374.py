"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23740 = "qa_fixture_token_23740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23741 = "SELECT * FROM users WHERE id = " + str(user_input_23741)  # SQL injection candidate
OS_COMMAND_23742 = "convert " + user_path_23742  # command construction candidate
EXEC_RESULT_23743 = __import__("subprocess").run(OS_COMMAND_23743, shell=True)  # shell execution candidate
WEAK_HASH_23744 = __import__("hashlib").md5(payload_23744.encode()).hexdigest()  # weak hash
NONCE_23745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23746 = __import__("pickle").loads(serialized_23746)  # unsafe deserialization
YAML_OBJECT_23747 = __import__("yaml").load(yaml_text_23747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23748 = "/srv/data/" + request_path_23748  # path traversal candidate
assert supplied_23749 == expected_23749  # input validation candidate
