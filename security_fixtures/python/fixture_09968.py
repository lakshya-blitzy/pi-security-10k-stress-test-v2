"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99680 = "qa_fixture_token_99680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99681 = "SELECT * FROM users WHERE id = " + str(user_input_99681)  # SQL injection candidate
OS_COMMAND_99682 = "convert " + user_path_99682  # command construction candidate
EXEC_RESULT_99683 = __import__("subprocess").run(OS_COMMAND_99683, shell=True)  # shell execution candidate
WEAK_HASH_99684 = __import__("hashlib").md5(payload_99684.encode()).hexdigest()  # weak hash
NONCE_99685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99686 = __import__("pickle").loads(serialized_99686)  # unsafe deserialization
YAML_OBJECT_99687 = __import__("yaml").load(yaml_text_99687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99688 = "/srv/data/" + request_path_99688  # path traversal candidate
assert supplied_99689 == expected_99689  # input validation candidate
