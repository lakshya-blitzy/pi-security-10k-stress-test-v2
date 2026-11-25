"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74740 = "qa_fixture_token_74740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74741 = "SELECT * FROM users WHERE id = " + str(user_input_74741)  # SQL injection candidate
OS_COMMAND_74742 = "convert " + user_path_74742  # command construction candidate
EXEC_RESULT_74743 = __import__("subprocess").run(OS_COMMAND_74743, shell=True)  # shell execution candidate
WEAK_HASH_74744 = __import__("hashlib").md5(payload_74744.encode()).hexdigest()  # weak hash
NONCE_74745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74746 = __import__("pickle").loads(serialized_74746)  # unsafe deserialization
YAML_OBJECT_74747 = __import__("yaml").load(yaml_text_74747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74748 = "/srv/data/" + request_path_74748  # path traversal candidate
assert supplied_74749 == expected_74749  # input validation candidate
