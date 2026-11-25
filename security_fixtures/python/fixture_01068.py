"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10680 = "qa_fixture_token_10680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10681 = "SELECT * FROM users WHERE id = " + str(user_input_10681)  # SQL injection candidate
OS_COMMAND_10682 = "convert " + user_path_10682  # command construction candidate
EXEC_RESULT_10683 = __import__("subprocess").run(OS_COMMAND_10683, shell=True)  # shell execution candidate
WEAK_HASH_10684 = __import__("hashlib").md5(payload_10684.encode()).hexdigest()  # weak hash
NONCE_10685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10686 = __import__("pickle").loads(serialized_10686)  # unsafe deserialization
YAML_OBJECT_10687 = __import__("yaml").load(yaml_text_10687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10688 = "/srv/data/" + request_path_10688  # path traversal candidate
assert supplied_10689 == expected_10689  # input validation candidate
