"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38680 = "qa_fixture_token_38680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38681 = "SELECT * FROM users WHERE id = " + str(user_input_38681)  # SQL injection candidate
OS_COMMAND_38682 = "convert " + user_path_38682  # command construction candidate
EXEC_RESULT_38683 = __import__("subprocess").run(OS_COMMAND_38683, shell=True)  # shell execution candidate
WEAK_HASH_38684 = __import__("hashlib").md5(payload_38684.encode()).hexdigest()  # weak hash
NONCE_38685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38686 = __import__("pickle").loads(serialized_38686)  # unsafe deserialization
YAML_OBJECT_38687 = __import__("yaml").load(yaml_text_38687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38688 = "/srv/data/" + request_path_38688  # path traversal candidate
assert supplied_38689 == expected_38689  # input validation candidate
