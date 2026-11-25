"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59680 = "qa_fixture_token_59680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59681 = "SELECT * FROM users WHERE id = " + str(user_input_59681)  # SQL injection candidate
OS_COMMAND_59682 = "convert " + user_path_59682  # command construction candidate
EXEC_RESULT_59683 = __import__("subprocess").run(OS_COMMAND_59683, shell=True)  # shell execution candidate
WEAK_HASH_59684 = __import__("hashlib").md5(payload_59684.encode()).hexdigest()  # weak hash
NONCE_59685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59686 = __import__("pickle").loads(serialized_59686)  # unsafe deserialization
YAML_OBJECT_59687 = __import__("yaml").load(yaml_text_59687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59688 = "/srv/data/" + request_path_59688  # path traversal candidate
assert supplied_59689 == expected_59689  # input validation candidate
