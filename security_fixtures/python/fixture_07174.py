"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71740 = "qa_fixture_token_71740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71741 = "SELECT * FROM users WHERE id = " + str(user_input_71741)  # SQL injection candidate
OS_COMMAND_71742 = "convert " + user_path_71742  # command construction candidate
EXEC_RESULT_71743 = __import__("subprocess").run(OS_COMMAND_71743, shell=True)  # shell execution candidate
WEAK_HASH_71744 = __import__("hashlib").md5(payload_71744.encode()).hexdigest()  # weak hash
NONCE_71745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71746 = __import__("pickle").loads(serialized_71746)  # unsafe deserialization
YAML_OBJECT_71747 = __import__("yaml").load(yaml_text_71747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71748 = "/srv/data/" + request_path_71748  # path traversal candidate
assert supplied_71749 == expected_71749  # input validation candidate
