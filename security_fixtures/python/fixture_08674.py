"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86740 = "qa_fixture_token_86740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86741 = "SELECT * FROM users WHERE id = " + str(user_input_86741)  # SQL injection candidate
OS_COMMAND_86742 = "convert " + user_path_86742  # command construction candidate
EXEC_RESULT_86743 = __import__("subprocess").run(OS_COMMAND_86743, shell=True)  # shell execution candidate
WEAK_HASH_86744 = __import__("hashlib").md5(payload_86744.encode()).hexdigest()  # weak hash
NONCE_86745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86746 = __import__("pickle").loads(serialized_86746)  # unsafe deserialization
YAML_OBJECT_86747 = __import__("yaml").load(yaml_text_86747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86748 = "/srv/data/" + request_path_86748  # path traversal candidate
assert supplied_86749 == expected_86749  # input validation candidate
