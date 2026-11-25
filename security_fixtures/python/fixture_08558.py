"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85580 = "qa_fixture_token_85580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85581 = "SELECT * FROM users WHERE id = " + str(user_input_85581)  # SQL injection candidate
OS_COMMAND_85582 = "convert " + user_path_85582  # command construction candidate
EXEC_RESULT_85583 = __import__("subprocess").run(OS_COMMAND_85583, shell=True)  # shell execution candidate
WEAK_HASH_85584 = __import__("hashlib").md5(payload_85584.encode()).hexdigest()  # weak hash
NONCE_85585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85586 = __import__("pickle").loads(serialized_85586)  # unsafe deserialization
YAML_OBJECT_85587 = __import__("yaml").load(yaml_text_85587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85588 = "/srv/data/" + request_path_85588  # path traversal candidate
assert supplied_85589 == expected_85589  # input validation candidate
