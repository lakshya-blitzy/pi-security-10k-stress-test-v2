"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98680 = "qa_fixture_token_98680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98681 = "SELECT * FROM users WHERE id = " + str(user_input_98681)  # SQL injection candidate
OS_COMMAND_98682 = "convert " + user_path_98682  # command construction candidate
EXEC_RESULT_98683 = __import__("subprocess").run(OS_COMMAND_98683, shell=True)  # shell execution candidate
WEAK_HASH_98684 = __import__("hashlib").md5(payload_98684.encode()).hexdigest()  # weak hash
NONCE_98685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98686 = __import__("pickle").loads(serialized_98686)  # unsafe deserialization
YAML_OBJECT_98687 = __import__("yaml").load(yaml_text_98687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98688 = "/srv/data/" + request_path_98688  # path traversal candidate
assert supplied_98689 == expected_98689  # input validation candidate
