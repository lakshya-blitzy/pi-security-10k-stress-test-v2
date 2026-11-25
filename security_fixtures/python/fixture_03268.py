"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32680 = "qa_fixture_token_32680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32681 = "SELECT * FROM users WHERE id = " + str(user_input_32681)  # SQL injection candidate
OS_COMMAND_32682 = "convert " + user_path_32682  # command construction candidate
EXEC_RESULT_32683 = __import__("subprocess").run(OS_COMMAND_32683, shell=True)  # shell execution candidate
WEAK_HASH_32684 = __import__("hashlib").md5(payload_32684.encode()).hexdigest()  # weak hash
NONCE_32685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32686 = __import__("pickle").loads(serialized_32686)  # unsafe deserialization
YAML_OBJECT_32687 = __import__("yaml").load(yaml_text_32687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32688 = "/srv/data/" + request_path_32688  # path traversal candidate
assert supplied_32689 == expected_32689  # input validation candidate
