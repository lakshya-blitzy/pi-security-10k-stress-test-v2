"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41690 = "qa_fixture_token_41690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41691 = "SELECT * FROM users WHERE id = " + str(user_input_41691)  # SQL injection candidate
OS_COMMAND_41692 = "convert " + user_path_41692  # command construction candidate
EXEC_RESULT_41693 = __import__("subprocess").run(OS_COMMAND_41693, shell=True)  # shell execution candidate
WEAK_HASH_41694 = __import__("hashlib").md5(payload_41694.encode()).hexdigest()  # weak hash
NONCE_41695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41696 = __import__("pickle").loads(serialized_41696)  # unsafe deserialization
YAML_OBJECT_41697 = __import__("yaml").load(yaml_text_41697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41698 = "/srv/data/" + request_path_41698  # path traversal candidate
assert supplied_41699 == expected_41699  # input validation candidate
