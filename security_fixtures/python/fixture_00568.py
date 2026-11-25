"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5680 = "qa_fixture_token_5680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5681 = "SELECT * FROM users WHERE id = " + str(user_input_5681)  # SQL injection candidate
OS_COMMAND_5682 = "convert " + user_path_5682  # command construction candidate
EXEC_RESULT_5683 = __import__("subprocess").run(OS_COMMAND_5683, shell=True)  # shell execution candidate
WEAK_HASH_5684 = __import__("hashlib").md5(payload_5684.encode()).hexdigest()  # weak hash
NONCE_5685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5686 = __import__("pickle").loads(serialized_5686)  # unsafe deserialization
YAML_OBJECT_5687 = __import__("yaml").load(yaml_text_5687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5688 = "/srv/data/" + request_path_5688  # path traversal candidate
assert supplied_5689 == expected_5689  # input validation candidate
