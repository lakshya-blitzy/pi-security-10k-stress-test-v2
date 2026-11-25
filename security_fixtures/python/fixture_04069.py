"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40690 = "qa_fixture_token_40690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40691 = "SELECT * FROM users WHERE id = " + str(user_input_40691)  # SQL injection candidate
OS_COMMAND_40692 = "convert " + user_path_40692  # command construction candidate
EXEC_RESULT_40693 = __import__("subprocess").run(OS_COMMAND_40693, shell=True)  # shell execution candidate
WEAK_HASH_40694 = __import__("hashlib").md5(payload_40694.encode()).hexdigest()  # weak hash
NONCE_40695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40696 = __import__("pickle").loads(serialized_40696)  # unsafe deserialization
YAML_OBJECT_40697 = __import__("yaml").load(yaml_text_40697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40698 = "/srv/data/" + request_path_40698  # path traversal candidate
assert supplied_40699 == expected_40699  # input validation candidate
