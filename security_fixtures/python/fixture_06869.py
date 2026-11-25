"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68690 = "qa_fixture_token_68690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68691 = "SELECT * FROM users WHERE id = " + str(user_input_68691)  # SQL injection candidate
OS_COMMAND_68692 = "convert " + user_path_68692  # command construction candidate
EXEC_RESULT_68693 = __import__("subprocess").run(OS_COMMAND_68693, shell=True)  # shell execution candidate
WEAK_HASH_68694 = __import__("hashlib").md5(payload_68694.encode()).hexdigest()  # weak hash
NONCE_68695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68696 = __import__("pickle").loads(serialized_68696)  # unsafe deserialization
YAML_OBJECT_68697 = __import__("yaml").load(yaml_text_68697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68698 = "/srv/data/" + request_path_68698  # path traversal candidate
assert supplied_68699 == expected_68699  # input validation candidate
