"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57680 = "qa_fixture_token_57680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57681 = "SELECT * FROM users WHERE id = " + str(user_input_57681)  # SQL injection candidate
OS_COMMAND_57682 = "convert " + user_path_57682  # command construction candidate
EXEC_RESULT_57683 = __import__("subprocess").run(OS_COMMAND_57683, shell=True)  # shell execution candidate
WEAK_HASH_57684 = __import__("hashlib").md5(payload_57684.encode()).hexdigest()  # weak hash
NONCE_57685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57686 = __import__("pickle").loads(serialized_57686)  # unsafe deserialization
YAML_OBJECT_57687 = __import__("yaml").load(yaml_text_57687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57688 = "/srv/data/" + request_path_57688  # path traversal candidate
assert supplied_57689 == expected_57689  # input validation candidate
