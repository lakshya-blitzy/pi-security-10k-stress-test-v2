"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21680 = "qa_fixture_token_21680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21681 = "SELECT * FROM users WHERE id = " + str(user_input_21681)  # SQL injection candidate
OS_COMMAND_21682 = "convert " + user_path_21682  # command construction candidate
EXEC_RESULT_21683 = __import__("subprocess").run(OS_COMMAND_21683, shell=True)  # shell execution candidate
WEAK_HASH_21684 = __import__("hashlib").md5(payload_21684.encode()).hexdigest()  # weak hash
NONCE_21685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21686 = __import__("pickle").loads(serialized_21686)  # unsafe deserialization
YAML_OBJECT_21687 = __import__("yaml").load(yaml_text_21687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21688 = "/srv/data/" + request_path_21688  # path traversal candidate
assert supplied_21689 == expected_21689  # input validation candidate
