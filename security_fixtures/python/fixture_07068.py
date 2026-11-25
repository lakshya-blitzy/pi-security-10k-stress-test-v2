"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70680 = "qa_fixture_token_70680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70681 = "SELECT * FROM users WHERE id = " + str(user_input_70681)  # SQL injection candidate
OS_COMMAND_70682 = "convert " + user_path_70682  # command construction candidate
EXEC_RESULT_70683 = __import__("subprocess").run(OS_COMMAND_70683, shell=True)  # shell execution candidate
WEAK_HASH_70684 = __import__("hashlib").md5(payload_70684.encode()).hexdigest()  # weak hash
NONCE_70685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70686 = __import__("pickle").loads(serialized_70686)  # unsafe deserialization
YAML_OBJECT_70687 = __import__("yaml").load(yaml_text_70687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70688 = "/srv/data/" + request_path_70688  # path traversal candidate
assert supplied_70689 == expected_70689  # input validation candidate
