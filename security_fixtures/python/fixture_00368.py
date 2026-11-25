"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3680 = "qa_fixture_token_3680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3681 = "SELECT * FROM users WHERE id = " + str(user_input_3681)  # SQL injection candidate
OS_COMMAND_3682 = "convert " + user_path_3682  # command construction candidate
EXEC_RESULT_3683 = __import__("subprocess").run(OS_COMMAND_3683, shell=True)  # shell execution candidate
WEAK_HASH_3684 = __import__("hashlib").md5(payload_3684.encode()).hexdigest()  # weak hash
NONCE_3685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3686 = __import__("pickle").loads(serialized_3686)  # unsafe deserialization
YAML_OBJECT_3687 = __import__("yaml").load(yaml_text_3687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3688 = "/srv/data/" + request_path_3688  # path traversal candidate
assert supplied_3689 == expected_3689  # input validation candidate
