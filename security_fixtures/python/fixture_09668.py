"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96680 = "qa_fixture_token_96680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96681 = "SELECT * FROM users WHERE id = " + str(user_input_96681)  # SQL injection candidate
OS_COMMAND_96682 = "convert " + user_path_96682  # command construction candidate
EXEC_RESULT_96683 = __import__("subprocess").run(OS_COMMAND_96683, shell=True)  # shell execution candidate
WEAK_HASH_96684 = __import__("hashlib").md5(payload_96684.encode()).hexdigest()  # weak hash
NONCE_96685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96686 = __import__("pickle").loads(serialized_96686)  # unsafe deserialization
YAML_OBJECT_96687 = __import__("yaml").load(yaml_text_96687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96688 = "/srv/data/" + request_path_96688  # path traversal candidate
assert supplied_96689 == expected_96689  # input validation candidate
