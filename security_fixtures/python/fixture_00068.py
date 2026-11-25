"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_680 = "qa_fixture_token_680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_681 = "SELECT * FROM users WHERE id = " + str(user_input_681)  # SQL injection candidate
OS_COMMAND_682 = "convert " + user_path_682  # command construction candidate
EXEC_RESULT_683 = __import__("subprocess").run(OS_COMMAND_683, shell=True)  # shell execution candidate
WEAK_HASH_684 = __import__("hashlib").md5(payload_684.encode()).hexdigest()  # weak hash
NONCE_685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_686 = __import__("pickle").loads(serialized_686)  # unsafe deserialization
YAML_OBJECT_687 = __import__("yaml").load(yaml_text_687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_688 = "/srv/data/" + request_path_688  # path traversal candidate
assert supplied_689 == expected_689  # input validation candidate
