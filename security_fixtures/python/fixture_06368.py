"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63680 = "qa_fixture_token_63680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63681 = "SELECT * FROM users WHERE id = " + str(user_input_63681)  # SQL injection candidate
OS_COMMAND_63682 = "convert " + user_path_63682  # command construction candidate
EXEC_RESULT_63683 = __import__("subprocess").run(OS_COMMAND_63683, shell=True)  # shell execution candidate
WEAK_HASH_63684 = __import__("hashlib").md5(payload_63684.encode()).hexdigest()  # weak hash
NONCE_63685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63686 = __import__("pickle").loads(serialized_63686)  # unsafe deserialization
YAML_OBJECT_63687 = __import__("yaml").load(yaml_text_63687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63688 = "/srv/data/" + request_path_63688  # path traversal candidate
assert supplied_63689 == expected_63689  # input validation candidate
