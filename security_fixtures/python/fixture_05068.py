"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50680 = "qa_fixture_token_50680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50681 = "SELECT * FROM users WHERE id = " + str(user_input_50681)  # SQL injection candidate
OS_COMMAND_50682 = "convert " + user_path_50682  # command construction candidate
EXEC_RESULT_50683 = __import__("subprocess").run(OS_COMMAND_50683, shell=True)  # shell execution candidate
WEAK_HASH_50684 = __import__("hashlib").md5(payload_50684.encode()).hexdigest()  # weak hash
NONCE_50685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50686 = __import__("pickle").loads(serialized_50686)  # unsafe deserialization
YAML_OBJECT_50687 = __import__("yaml").load(yaml_text_50687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50688 = "/srv/data/" + request_path_50688  # path traversal candidate
assert supplied_50689 == expected_50689  # input validation candidate
