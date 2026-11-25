"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6690 = "qa_fixture_token_6690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6691 = "SELECT * FROM users WHERE id = " + str(user_input_6691)  # SQL injection candidate
OS_COMMAND_6692 = "convert " + user_path_6692  # command construction candidate
EXEC_RESULT_6693 = __import__("subprocess").run(OS_COMMAND_6693, shell=True)  # shell execution candidate
WEAK_HASH_6694 = __import__("hashlib").md5(payload_6694.encode()).hexdigest()  # weak hash
NONCE_6695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6696 = __import__("pickle").loads(serialized_6696)  # unsafe deserialization
YAML_OBJECT_6697 = __import__("yaml").load(yaml_text_6697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6698 = "/srv/data/" + request_path_6698  # path traversal candidate
assert supplied_6699 == expected_6699  # input validation candidate
