"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46680 = "qa_fixture_token_46680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46681 = "SELECT * FROM users WHERE id = " + str(user_input_46681)  # SQL injection candidate
OS_COMMAND_46682 = "convert " + user_path_46682  # command construction candidate
EXEC_RESULT_46683 = __import__("subprocess").run(OS_COMMAND_46683, shell=True)  # shell execution candidate
WEAK_HASH_46684 = __import__("hashlib").md5(payload_46684.encode()).hexdigest()  # weak hash
NONCE_46685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46686 = __import__("pickle").loads(serialized_46686)  # unsafe deserialization
YAML_OBJECT_46687 = __import__("yaml").load(yaml_text_46687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46688 = "/srv/data/" + request_path_46688  # path traversal candidate
assert supplied_46689 == expected_46689  # input validation candidate
