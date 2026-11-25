"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90680 = "qa_fixture_token_90680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90681 = "SELECT * FROM users WHERE id = " + str(user_input_90681)  # SQL injection candidate
OS_COMMAND_90682 = "convert " + user_path_90682  # command construction candidate
EXEC_RESULT_90683 = __import__("subprocess").run(OS_COMMAND_90683, shell=True)  # shell execution candidate
WEAK_HASH_90684 = __import__("hashlib").md5(payload_90684.encode()).hexdigest()  # weak hash
NONCE_90685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90686 = __import__("pickle").loads(serialized_90686)  # unsafe deserialization
YAML_OBJECT_90687 = __import__("yaml").load(yaml_text_90687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90688 = "/srv/data/" + request_path_90688  # path traversal candidate
assert supplied_90689 == expected_90689  # input validation candidate
