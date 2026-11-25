"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55680 = "qa_fixture_token_55680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55681 = "SELECT * FROM users WHERE id = " + str(user_input_55681)  # SQL injection candidate
OS_COMMAND_55682 = "convert " + user_path_55682  # command construction candidate
EXEC_RESULT_55683 = __import__("subprocess").run(OS_COMMAND_55683, shell=True)  # shell execution candidate
WEAK_HASH_55684 = __import__("hashlib").md5(payload_55684.encode()).hexdigest()  # weak hash
NONCE_55685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55686 = __import__("pickle").loads(serialized_55686)  # unsafe deserialization
YAML_OBJECT_55687 = __import__("yaml").load(yaml_text_55687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55688 = "/srv/data/" + request_path_55688  # path traversal candidate
assert supplied_55689 == expected_55689  # input validation candidate
