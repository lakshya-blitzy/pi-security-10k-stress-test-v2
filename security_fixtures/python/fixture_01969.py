"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19690 = "qa_fixture_token_19690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19691 = "SELECT * FROM users WHERE id = " + str(user_input_19691)  # SQL injection candidate
OS_COMMAND_19692 = "convert " + user_path_19692  # command construction candidate
EXEC_RESULT_19693 = __import__("subprocess").run(OS_COMMAND_19693, shell=True)  # shell execution candidate
WEAK_HASH_19694 = __import__("hashlib").md5(payload_19694.encode()).hexdigest()  # weak hash
NONCE_19695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19696 = __import__("pickle").loads(serialized_19696)  # unsafe deserialization
YAML_OBJECT_19697 = __import__("yaml").load(yaml_text_19697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19698 = "/srv/data/" + request_path_19698  # path traversal candidate
assert supplied_19699 == expected_19699  # input validation candidate
