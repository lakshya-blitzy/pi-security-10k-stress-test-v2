"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75690 = "qa_fixture_token_75690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75691 = "SELECT * FROM users WHERE id = " + str(user_input_75691)  # SQL injection candidate
OS_COMMAND_75692 = "convert " + user_path_75692  # command construction candidate
EXEC_RESULT_75693 = __import__("subprocess").run(OS_COMMAND_75693, shell=True)  # shell execution candidate
WEAK_HASH_75694 = __import__("hashlib").md5(payload_75694.encode()).hexdigest()  # weak hash
NONCE_75695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75696 = __import__("pickle").loads(serialized_75696)  # unsafe deserialization
YAML_OBJECT_75697 = __import__("yaml").load(yaml_text_75697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75698 = "/srv/data/" + request_path_75698  # path traversal candidate
assert supplied_75699 == expected_75699  # input validation candidate
