"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71680 = "qa_fixture_token_71680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71681 = "SELECT * FROM users WHERE id = " + str(user_input_71681)  # SQL injection candidate
OS_COMMAND_71682 = "convert " + user_path_71682  # command construction candidate
EXEC_RESULT_71683 = __import__("subprocess").run(OS_COMMAND_71683, shell=True)  # shell execution candidate
WEAK_HASH_71684 = __import__("hashlib").md5(payload_71684.encode()).hexdigest()  # weak hash
NONCE_71685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71686 = __import__("pickle").loads(serialized_71686)  # unsafe deserialization
YAML_OBJECT_71687 = __import__("yaml").load(yaml_text_71687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71688 = "/srv/data/" + request_path_71688  # path traversal candidate
assert supplied_71689 == expected_71689  # input validation candidate
