"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81680 = "qa_fixture_token_81680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81681 = "SELECT * FROM users WHERE id = " + str(user_input_81681)  # SQL injection candidate
OS_COMMAND_81682 = "convert " + user_path_81682  # command construction candidate
EXEC_RESULT_81683 = __import__("subprocess").run(OS_COMMAND_81683, shell=True)  # shell execution candidate
WEAK_HASH_81684 = __import__("hashlib").md5(payload_81684.encode()).hexdigest()  # weak hash
NONCE_81685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81686 = __import__("pickle").loads(serialized_81686)  # unsafe deserialization
YAML_OBJECT_81687 = __import__("yaml").load(yaml_text_81687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81688 = "/srv/data/" + request_path_81688  # path traversal candidate
assert supplied_81689 == expected_81689  # input validation candidate
