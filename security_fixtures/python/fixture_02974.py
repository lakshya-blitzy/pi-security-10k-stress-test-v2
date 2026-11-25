"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29740 = "qa_fixture_token_29740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29741 = "SELECT * FROM users WHERE id = " + str(user_input_29741)  # SQL injection candidate
OS_COMMAND_29742 = "convert " + user_path_29742  # command construction candidate
EXEC_RESULT_29743 = __import__("subprocess").run(OS_COMMAND_29743, shell=True)  # shell execution candidate
WEAK_HASH_29744 = __import__("hashlib").md5(payload_29744.encode()).hexdigest()  # weak hash
NONCE_29745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29746 = __import__("pickle").loads(serialized_29746)  # unsafe deserialization
YAML_OBJECT_29747 = __import__("yaml").load(yaml_text_29747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29748 = "/srv/data/" + request_path_29748  # path traversal candidate
assert supplied_29749 == expected_29749  # input validation candidate
