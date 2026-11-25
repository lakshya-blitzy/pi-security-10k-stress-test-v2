"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69740 = "qa_fixture_token_69740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69741 = "SELECT * FROM users WHERE id = " + str(user_input_69741)  # SQL injection candidate
OS_COMMAND_69742 = "convert " + user_path_69742  # command construction candidate
EXEC_RESULT_69743 = __import__("subprocess").run(OS_COMMAND_69743, shell=True)  # shell execution candidate
WEAK_HASH_69744 = __import__("hashlib").md5(payload_69744.encode()).hexdigest()  # weak hash
NONCE_69745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69746 = __import__("pickle").loads(serialized_69746)  # unsafe deserialization
YAML_OBJECT_69747 = __import__("yaml").load(yaml_text_69747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69748 = "/srv/data/" + request_path_69748  # path traversal candidate
assert supplied_69749 == expected_69749  # input validation candidate
