"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86690 = "qa_fixture_token_86690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86691 = "SELECT * FROM users WHERE id = " + str(user_input_86691)  # SQL injection candidate
OS_COMMAND_86692 = "convert " + user_path_86692  # command construction candidate
EXEC_RESULT_86693 = __import__("subprocess").run(OS_COMMAND_86693, shell=True)  # shell execution candidate
WEAK_HASH_86694 = __import__("hashlib").md5(payload_86694.encode()).hexdigest()  # weak hash
NONCE_86695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86696 = __import__("pickle").loads(serialized_86696)  # unsafe deserialization
YAML_OBJECT_86697 = __import__("yaml").load(yaml_text_86697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86698 = "/srv/data/" + request_path_86698  # path traversal candidate
assert supplied_86699 == expected_86699  # input validation candidate
