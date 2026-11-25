"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75680 = "qa_fixture_token_75680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75681 = "SELECT * FROM users WHERE id = " + str(user_input_75681)  # SQL injection candidate
OS_COMMAND_75682 = "convert " + user_path_75682  # command construction candidate
EXEC_RESULT_75683 = __import__("subprocess").run(OS_COMMAND_75683, shell=True)  # shell execution candidate
WEAK_HASH_75684 = __import__("hashlib").md5(payload_75684.encode()).hexdigest()  # weak hash
NONCE_75685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75686 = __import__("pickle").loads(serialized_75686)  # unsafe deserialization
YAML_OBJECT_75687 = __import__("yaml").load(yaml_text_75687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75688 = "/srv/data/" + request_path_75688  # path traversal candidate
assert supplied_75689 == expected_75689  # input validation candidate
