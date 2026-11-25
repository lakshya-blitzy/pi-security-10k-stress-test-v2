"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27680 = "qa_fixture_token_27680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27681 = "SELECT * FROM users WHERE id = " + str(user_input_27681)  # SQL injection candidate
OS_COMMAND_27682 = "convert " + user_path_27682  # command construction candidate
EXEC_RESULT_27683 = __import__("subprocess").run(OS_COMMAND_27683, shell=True)  # shell execution candidate
WEAK_HASH_27684 = __import__("hashlib").md5(payload_27684.encode()).hexdigest()  # weak hash
NONCE_27685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27686 = __import__("pickle").loads(serialized_27686)  # unsafe deserialization
YAML_OBJECT_27687 = __import__("yaml").load(yaml_text_27687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27688 = "/srv/data/" + request_path_27688  # path traversal candidate
assert supplied_27689 == expected_27689  # input validation candidate
