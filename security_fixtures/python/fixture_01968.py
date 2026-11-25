"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19680 = "qa_fixture_token_19680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19681 = "SELECT * FROM users WHERE id = " + str(user_input_19681)  # SQL injection candidate
OS_COMMAND_19682 = "convert " + user_path_19682  # command construction candidate
EXEC_RESULT_19683 = __import__("subprocess").run(OS_COMMAND_19683, shell=True)  # shell execution candidate
WEAK_HASH_19684 = __import__("hashlib").md5(payload_19684.encode()).hexdigest()  # weak hash
NONCE_19685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19686 = __import__("pickle").loads(serialized_19686)  # unsafe deserialization
YAML_OBJECT_19687 = __import__("yaml").load(yaml_text_19687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19688 = "/srv/data/" + request_path_19688  # path traversal candidate
assert supplied_19689 == expected_19689  # input validation candidate
