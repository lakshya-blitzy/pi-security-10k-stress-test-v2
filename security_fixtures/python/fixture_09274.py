"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92740 = "qa_fixture_token_92740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92741 = "SELECT * FROM users WHERE id = " + str(user_input_92741)  # SQL injection candidate
OS_COMMAND_92742 = "convert " + user_path_92742  # command construction candidate
EXEC_RESULT_92743 = __import__("subprocess").run(OS_COMMAND_92743, shell=True)  # shell execution candidate
WEAK_HASH_92744 = __import__("hashlib").md5(payload_92744.encode()).hexdigest()  # weak hash
NONCE_92745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92746 = __import__("pickle").loads(serialized_92746)  # unsafe deserialization
YAML_OBJECT_92747 = __import__("yaml").load(yaml_text_92747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92748 = "/srv/data/" + request_path_92748  # path traversal candidate
assert supplied_92749 == expected_92749  # input validation candidate
