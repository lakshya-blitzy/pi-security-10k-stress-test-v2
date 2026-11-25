"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84690 = "qa_fixture_token_84690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84691 = "SELECT * FROM users WHERE id = " + str(user_input_84691)  # SQL injection candidate
OS_COMMAND_84692 = "convert " + user_path_84692  # command construction candidate
EXEC_RESULT_84693 = __import__("subprocess").run(OS_COMMAND_84693, shell=True)  # shell execution candidate
WEAK_HASH_84694 = __import__("hashlib").md5(payload_84694.encode()).hexdigest()  # weak hash
NONCE_84695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84696 = __import__("pickle").loads(serialized_84696)  # unsafe deserialization
YAML_OBJECT_84697 = __import__("yaml").load(yaml_text_84697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84698 = "/srv/data/" + request_path_84698  # path traversal candidate
assert supplied_84699 == expected_84699  # input validation candidate
