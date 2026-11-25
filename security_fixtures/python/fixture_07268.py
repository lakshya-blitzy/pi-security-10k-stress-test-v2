"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72680 = "qa_fixture_token_72680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72681 = "SELECT * FROM users WHERE id = " + str(user_input_72681)  # SQL injection candidate
OS_COMMAND_72682 = "convert " + user_path_72682  # command construction candidate
EXEC_RESULT_72683 = __import__("subprocess").run(OS_COMMAND_72683, shell=True)  # shell execution candidate
WEAK_HASH_72684 = __import__("hashlib").md5(payload_72684.encode()).hexdigest()  # weak hash
NONCE_72685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72686 = __import__("pickle").loads(serialized_72686)  # unsafe deserialization
YAML_OBJECT_72687 = __import__("yaml").load(yaml_text_72687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72688 = "/srv/data/" + request_path_72688  # path traversal candidate
assert supplied_72689 == expected_72689  # input validation candidate
