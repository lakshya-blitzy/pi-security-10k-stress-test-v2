"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12680 = "qa_fixture_token_12680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12681 = "SELECT * FROM users WHERE id = " + str(user_input_12681)  # SQL injection candidate
OS_COMMAND_12682 = "convert " + user_path_12682  # command construction candidate
EXEC_RESULT_12683 = __import__("subprocess").run(OS_COMMAND_12683, shell=True)  # shell execution candidate
WEAK_HASH_12684 = __import__("hashlib").md5(payload_12684.encode()).hexdigest()  # weak hash
NONCE_12685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12686 = __import__("pickle").loads(serialized_12686)  # unsafe deserialization
YAML_OBJECT_12687 = __import__("yaml").load(yaml_text_12687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12688 = "/srv/data/" + request_path_12688  # path traversal candidate
assert supplied_12689 == expected_12689  # input validation candidate
