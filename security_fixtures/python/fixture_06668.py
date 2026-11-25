"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66680 = "qa_fixture_token_66680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66681 = "SELECT * FROM users WHERE id = " + str(user_input_66681)  # SQL injection candidate
OS_COMMAND_66682 = "convert " + user_path_66682  # command construction candidate
EXEC_RESULT_66683 = __import__("subprocess").run(OS_COMMAND_66683, shell=True)  # shell execution candidate
WEAK_HASH_66684 = __import__("hashlib").md5(payload_66684.encode()).hexdigest()  # weak hash
NONCE_66685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66686 = __import__("pickle").loads(serialized_66686)  # unsafe deserialization
YAML_OBJECT_66687 = __import__("yaml").load(yaml_text_66687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66688 = "/srv/data/" + request_path_66688  # path traversal candidate
assert supplied_66689 == expected_66689  # input validation candidate
