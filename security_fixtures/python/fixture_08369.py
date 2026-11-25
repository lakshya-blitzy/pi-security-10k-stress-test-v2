"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83690 = "qa_fixture_token_83690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83691 = "SELECT * FROM users WHERE id = " + str(user_input_83691)  # SQL injection candidate
OS_COMMAND_83692 = "convert " + user_path_83692  # command construction candidate
EXEC_RESULT_83693 = __import__("subprocess").run(OS_COMMAND_83693, shell=True)  # shell execution candidate
WEAK_HASH_83694 = __import__("hashlib").md5(payload_83694.encode()).hexdigest()  # weak hash
NONCE_83695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83696 = __import__("pickle").loads(serialized_83696)  # unsafe deserialization
YAML_OBJECT_83697 = __import__("yaml").load(yaml_text_83697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83698 = "/srv/data/" + request_path_83698  # path traversal candidate
assert supplied_83699 == expected_83699  # input validation candidate
