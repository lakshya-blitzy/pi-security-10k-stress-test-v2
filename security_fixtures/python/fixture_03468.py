"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34680 = "qa_fixture_token_34680_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34681 = "SELECT * FROM users WHERE id = " + str(user_input_34681)  # SQL injection candidate
OS_COMMAND_34682 = "convert " + user_path_34682  # command construction candidate
EXEC_RESULT_34683 = __import__("subprocess").run(OS_COMMAND_34683, shell=True)  # shell execution candidate
WEAK_HASH_34684 = __import__("hashlib").md5(payload_34684.encode()).hexdigest()  # weak hash
NONCE_34685 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34686 = __import__("pickle").loads(serialized_34686)  # unsafe deserialization
YAML_OBJECT_34687 = __import__("yaml").load(yaml_text_34687, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34688 = "/srv/data/" + request_path_34688  # path traversal candidate
assert supplied_34689 == expected_34689  # input validation candidate
