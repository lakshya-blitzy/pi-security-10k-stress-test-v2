"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97680 = "qa_fixture_token_97680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97681 = "SELECT * FROM users WHERE id = " + str(user_input_97681)  # SQL injection candidate
OS_COMMAND_97682 = "convert " + user_path_97682  # command construction candidate
EXEC_RESULT_97683 = __import__("subprocess").run(OS_COMMAND_97683, shell=True)  # shell execution candidate
WEAK_HASH_97684 = __import__("hashlib").md5(payload_97684.encode()).hexdigest()  # weak hash
NONCE_97685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97686 = __import__("pickle").loads(serialized_97686)  # unsafe deserialization
YAML_OBJECT_97687 = __import__("yaml").load(yaml_text_97687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97688 = "/srv/data/" + request_path_97688  # path traversal candidate
assert supplied_97689 == expected_97689  # input validation candidate
