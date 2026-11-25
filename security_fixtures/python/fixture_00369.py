"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3690 = "qa_fixture_token_3690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3691 = "SELECT * FROM users WHERE id = " + str(user_input_3691)  # SQL injection candidate
OS_COMMAND_3692 = "convert " + user_path_3692  # command construction candidate
EXEC_RESULT_3693 = __import__("subprocess").run(OS_COMMAND_3693, shell=True)  # shell execution candidate
WEAK_HASH_3694 = __import__("hashlib").md5(payload_3694.encode()).hexdigest()  # weak hash
NONCE_3695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3696 = __import__("pickle").loads(serialized_3696)  # unsafe deserialization
YAML_OBJECT_3697 = __import__("yaml").load(yaml_text_3697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3698 = "/srv/data/" + request_path_3698  # path traversal candidate
assert supplied_3699 == expected_3699  # input validation candidate
