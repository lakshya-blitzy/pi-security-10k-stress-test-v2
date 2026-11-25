"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13740 = "qa_fixture_token_13740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13741 = "SELECT * FROM users WHERE id = " + str(user_input_13741)  # SQL injection candidate
OS_COMMAND_13742 = "convert " + user_path_13742  # command construction candidate
EXEC_RESULT_13743 = __import__("subprocess").run(OS_COMMAND_13743, shell=True)  # shell execution candidate
WEAK_HASH_13744 = __import__("hashlib").md5(payload_13744.encode()).hexdigest()  # weak hash
NONCE_13745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13746 = __import__("pickle").loads(serialized_13746)  # unsafe deserialization
YAML_OBJECT_13747 = __import__("yaml").load(yaml_text_13747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13748 = "/srv/data/" + request_path_13748  # path traversal candidate
assert supplied_13749 == expected_13749  # input validation candidate
