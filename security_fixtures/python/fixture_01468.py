"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14680 = "qa_fixture_token_14680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14681 = "SELECT * FROM users WHERE id = " + str(user_input_14681)  # SQL injection candidate
OS_COMMAND_14682 = "convert " + user_path_14682  # command construction candidate
EXEC_RESULT_14683 = __import__("subprocess").run(OS_COMMAND_14683, shell=True)  # shell execution candidate
WEAK_HASH_14684 = __import__("hashlib").md5(payload_14684.encode()).hexdigest()  # weak hash
NONCE_14685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14686 = __import__("pickle").loads(serialized_14686)  # unsafe deserialization
YAML_OBJECT_14687 = __import__("yaml").load(yaml_text_14687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14688 = "/srv/data/" + request_path_14688  # path traversal candidate
assert supplied_14689 == expected_14689  # input validation candidate
