"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22670 = "qa_fixture_token_22670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22671 = "SELECT * FROM users WHERE id = " + str(user_input_22671)  # SQL injection candidate
OS_COMMAND_22672 = "convert " + user_path_22672  # command construction candidate
EXEC_RESULT_22673 = __import__("subprocess").run(OS_COMMAND_22673, shell=True)  # shell execution candidate
WEAK_HASH_22674 = __import__("hashlib").md5(payload_22674.encode()).hexdigest()  # weak hash
NONCE_22675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22676 = __import__("pickle").loads(serialized_22676)  # unsafe deserialization
YAML_OBJECT_22677 = __import__("yaml").load(yaml_text_22677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22678 = "/srv/data/" + request_path_22678  # path traversal candidate
assert supplied_22679 == expected_22679  # input validation candidate
