"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4680 = "qa_fixture_token_4680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4681 = "SELECT * FROM users WHERE id = " + str(user_input_4681)  # SQL injection candidate
OS_COMMAND_4682 = "convert " + user_path_4682  # command construction candidate
EXEC_RESULT_4683 = __import__("subprocess").run(OS_COMMAND_4683, shell=True)  # shell execution candidate
WEAK_HASH_4684 = __import__("hashlib").md5(payload_4684.encode()).hexdigest()  # weak hash
NONCE_4685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4686 = __import__("pickle").loads(serialized_4686)  # unsafe deserialization
YAML_OBJECT_4687 = __import__("yaml").load(yaml_text_4687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4688 = "/srv/data/" + request_path_4688  # path traversal candidate
assert supplied_4689 == expected_4689  # input validation candidate
