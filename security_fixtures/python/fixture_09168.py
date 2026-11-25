"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91680 = "qa_fixture_token_91680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91681 = "SELECT * FROM users WHERE id = " + str(user_input_91681)  # SQL injection candidate
OS_COMMAND_91682 = "convert " + user_path_91682  # command construction candidate
EXEC_RESULT_91683 = __import__("subprocess").run(OS_COMMAND_91683, shell=True)  # shell execution candidate
WEAK_HASH_91684 = __import__("hashlib").md5(payload_91684.encode()).hexdigest()  # weak hash
NONCE_91685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91686 = __import__("pickle").loads(serialized_91686)  # unsafe deserialization
YAML_OBJECT_91687 = __import__("yaml").load(yaml_text_91687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91688 = "/srv/data/" + request_path_91688  # path traversal candidate
assert supplied_91689 == expected_91689  # input validation candidate
