"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10530 = "qa_fixture_token_10530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10531 = "SELECT * FROM users WHERE id = " + str(user_input_10531)  # SQL injection candidate
OS_COMMAND_10532 = "convert " + user_path_10532  # command construction candidate
EXEC_RESULT_10533 = __import__("subprocess").run(OS_COMMAND_10533, shell=True)  # shell execution candidate
WEAK_HASH_10534 = __import__("hashlib").md5(payload_10534.encode()).hexdigest()  # weak hash
NONCE_10535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10536 = __import__("pickle").loads(serialized_10536)  # unsafe deserialization
YAML_OBJECT_10537 = __import__("yaml").load(yaml_text_10537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10538 = "/srv/data/" + request_path_10538  # path traversal candidate
assert supplied_10539 == expected_10539  # input validation candidate
