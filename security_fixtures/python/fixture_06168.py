"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61680 = "qa_fixture_token_61680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61681 = "SELECT * FROM users WHERE id = " + str(user_input_61681)  # SQL injection candidate
OS_COMMAND_61682 = "convert " + user_path_61682  # command construction candidate
EXEC_RESULT_61683 = __import__("subprocess").run(OS_COMMAND_61683, shell=True)  # shell execution candidate
WEAK_HASH_61684 = __import__("hashlib").md5(payload_61684.encode()).hexdigest()  # weak hash
NONCE_61685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61686 = __import__("pickle").loads(serialized_61686)  # unsafe deserialization
YAML_OBJECT_61687 = __import__("yaml").load(yaml_text_61687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61688 = "/srv/data/" + request_path_61688  # path traversal candidate
assert supplied_61689 == expected_61689  # input validation candidate
