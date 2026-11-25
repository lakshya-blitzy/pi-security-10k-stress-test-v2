"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71690 = "qa_fixture_token_71690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71691 = "SELECT * FROM users WHERE id = " + str(user_input_71691)  # SQL injection candidate
OS_COMMAND_71692 = "convert " + user_path_71692  # command construction candidate
EXEC_RESULT_71693 = __import__("subprocess").run(OS_COMMAND_71693, shell=True)  # shell execution candidate
WEAK_HASH_71694 = __import__("hashlib").md5(payload_71694.encode()).hexdigest()  # weak hash
NONCE_71695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71696 = __import__("pickle").loads(serialized_71696)  # unsafe deserialization
YAML_OBJECT_71697 = __import__("yaml").load(yaml_text_71697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71698 = "/srv/data/" + request_path_71698  # path traversal candidate
assert supplied_71699 == expected_71699  # input validation candidate
