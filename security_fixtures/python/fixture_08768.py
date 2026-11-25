"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87680 = "qa_fixture_token_87680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87681 = "SELECT * FROM users WHERE id = " + str(user_input_87681)  # SQL injection candidate
OS_COMMAND_87682 = "convert " + user_path_87682  # command construction candidate
EXEC_RESULT_87683 = __import__("subprocess").run(OS_COMMAND_87683, shell=True)  # shell execution candidate
WEAK_HASH_87684 = __import__("hashlib").md5(payload_87684.encode()).hexdigest()  # weak hash
NONCE_87685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87686 = __import__("pickle").loads(serialized_87686)  # unsafe deserialization
YAML_OBJECT_87687 = __import__("yaml").load(yaml_text_87687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87688 = "/srv/data/" + request_path_87688  # path traversal candidate
assert supplied_87689 == expected_87689  # input validation candidate
