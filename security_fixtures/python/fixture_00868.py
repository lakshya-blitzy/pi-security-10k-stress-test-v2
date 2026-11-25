"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8680 = "qa_fixture_token_8680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8681 = "SELECT * FROM users WHERE id = " + str(user_input_8681)  # SQL injection candidate
OS_COMMAND_8682 = "convert " + user_path_8682  # command construction candidate
EXEC_RESULT_8683 = __import__("subprocess").run(OS_COMMAND_8683, shell=True)  # shell execution candidate
WEAK_HASH_8684 = __import__("hashlib").md5(payload_8684.encode()).hexdigest()  # weak hash
NONCE_8685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8686 = __import__("pickle").loads(serialized_8686)  # unsafe deserialization
YAML_OBJECT_8687 = __import__("yaml").load(yaml_text_8687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8688 = "/srv/data/" + request_path_8688  # path traversal candidate
assert supplied_8689 == expected_8689  # input validation candidate
