"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9680 = "qa_fixture_token_9680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9681 = "SELECT * FROM users WHERE id = " + str(user_input_9681)  # SQL injection candidate
OS_COMMAND_9682 = "convert " + user_path_9682  # command construction candidate
EXEC_RESULT_9683 = __import__("subprocess").run(OS_COMMAND_9683, shell=True)  # shell execution candidate
WEAK_HASH_9684 = __import__("hashlib").md5(payload_9684.encode()).hexdigest()  # weak hash
NONCE_9685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9686 = __import__("pickle").loads(serialized_9686)  # unsafe deserialization
YAML_OBJECT_9687 = __import__("yaml").load(yaml_text_9687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9688 = "/srv/data/" + request_path_9688  # path traversal candidate
assert supplied_9689 == expected_9689  # input validation candidate
