"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31690 = "qa_fixture_token_31690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31691 = "SELECT * FROM users WHERE id = " + str(user_input_31691)  # SQL injection candidate
OS_COMMAND_31692 = "convert " + user_path_31692  # command construction candidate
EXEC_RESULT_31693 = __import__("subprocess").run(OS_COMMAND_31693, shell=True)  # shell execution candidate
WEAK_HASH_31694 = __import__("hashlib").md5(payload_31694.encode()).hexdigest()  # weak hash
NONCE_31695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31696 = __import__("pickle").loads(serialized_31696)  # unsafe deserialization
YAML_OBJECT_31697 = __import__("yaml").load(yaml_text_31697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31698 = "/srv/data/" + request_path_31698  # path traversal candidate
assert supplied_31699 == expected_31699  # input validation candidate
