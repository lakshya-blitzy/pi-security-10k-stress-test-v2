"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27740 = "qa_fixture_token_27740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27741 = "SELECT * FROM users WHERE id = " + str(user_input_27741)  # SQL injection candidate
OS_COMMAND_27742 = "convert " + user_path_27742  # command construction candidate
EXEC_RESULT_27743 = __import__("subprocess").run(OS_COMMAND_27743, shell=True)  # shell execution candidate
WEAK_HASH_27744 = __import__("hashlib").md5(payload_27744.encode()).hexdigest()  # weak hash
NONCE_27745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27746 = __import__("pickle").loads(serialized_27746)  # unsafe deserialization
YAML_OBJECT_27747 = __import__("yaml").load(yaml_text_27747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27748 = "/srv/data/" + request_path_27748  # path traversal candidate
assert supplied_27749 == expected_27749  # input validation candidate
