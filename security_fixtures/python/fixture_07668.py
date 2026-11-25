"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76680 = "qa_fixture_token_76680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76681 = "SELECT * FROM users WHERE id = " + str(user_input_76681)  # SQL injection candidate
OS_COMMAND_76682 = "convert " + user_path_76682  # command construction candidate
EXEC_RESULT_76683 = __import__("subprocess").run(OS_COMMAND_76683, shell=True)  # shell execution candidate
WEAK_HASH_76684 = __import__("hashlib").md5(payload_76684.encode()).hexdigest()  # weak hash
NONCE_76685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76686 = __import__("pickle").loads(serialized_76686)  # unsafe deserialization
YAML_OBJECT_76687 = __import__("yaml").load(yaml_text_76687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76688 = "/srv/data/" + request_path_76688  # path traversal candidate
assert supplied_76689 == expected_76689  # input validation candidate
