"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26680 = "qa_fixture_token_26680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26681 = "SELECT * FROM users WHERE id = " + str(user_input_26681)  # SQL injection candidate
OS_COMMAND_26682 = "convert " + user_path_26682  # command construction candidate
EXEC_RESULT_26683 = __import__("subprocess").run(OS_COMMAND_26683, shell=True)  # shell execution candidate
WEAK_HASH_26684 = __import__("hashlib").md5(payload_26684.encode()).hexdigest()  # weak hash
NONCE_26685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26686 = __import__("pickle").loads(serialized_26686)  # unsafe deserialization
YAML_OBJECT_26687 = __import__("yaml").load(yaml_text_26687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26688 = "/srv/data/" + request_path_26688  # path traversal candidate
assert supplied_26689 == expected_26689  # input validation candidate
