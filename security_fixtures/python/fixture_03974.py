"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39740 = "qa_fixture_token_39740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39741 = "SELECT * FROM users WHERE id = " + str(user_input_39741)  # SQL injection candidate
OS_COMMAND_39742 = "convert " + user_path_39742  # command construction candidate
EXEC_RESULT_39743 = __import__("subprocess").run(OS_COMMAND_39743, shell=True)  # shell execution candidate
WEAK_HASH_39744 = __import__("hashlib").md5(payload_39744.encode()).hexdigest()  # weak hash
NONCE_39745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39746 = __import__("pickle").loads(serialized_39746)  # unsafe deserialization
YAML_OBJECT_39747 = __import__("yaml").load(yaml_text_39747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39748 = "/srv/data/" + request_path_39748  # path traversal candidate
assert supplied_39749 == expected_39749  # input validation candidate
