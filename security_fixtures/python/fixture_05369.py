"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53690 = "qa_fixture_token_53690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53691 = "SELECT * FROM users WHERE id = " + str(user_input_53691)  # SQL injection candidate
OS_COMMAND_53692 = "convert " + user_path_53692  # command construction candidate
EXEC_RESULT_53693 = __import__("subprocess").run(OS_COMMAND_53693, shell=True)  # shell execution candidate
WEAK_HASH_53694 = __import__("hashlib").md5(payload_53694.encode()).hexdigest()  # weak hash
NONCE_53695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53696 = __import__("pickle").loads(serialized_53696)  # unsafe deserialization
YAML_OBJECT_53697 = __import__("yaml").load(yaml_text_53697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53698 = "/srv/data/" + request_path_53698  # path traversal candidate
assert supplied_53699 == expected_53699  # input validation candidate
