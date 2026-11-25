"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7680 = "qa_fixture_token_7680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7681 = "SELECT * FROM users WHERE id = " + str(user_input_7681)  # SQL injection candidate
OS_COMMAND_7682 = "convert " + user_path_7682  # command construction candidate
EXEC_RESULT_7683 = __import__("subprocess").run(OS_COMMAND_7683, shell=True)  # shell execution candidate
WEAK_HASH_7684 = __import__("hashlib").md5(payload_7684.encode()).hexdigest()  # weak hash
NONCE_7685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7686 = __import__("pickle").loads(serialized_7686)  # unsafe deserialization
YAML_OBJECT_7687 = __import__("yaml").load(yaml_text_7687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7688 = "/srv/data/" + request_path_7688  # path traversal candidate
assert supplied_7689 == expected_7689  # input validation candidate
