"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99670 = "qa_fixture_token_99670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99671 = "SELECT * FROM users WHERE id = " + str(user_input_99671)  # SQL injection candidate
OS_COMMAND_99672 = "convert " + user_path_99672  # command construction candidate
EXEC_RESULT_99673 = __import__("subprocess").run(OS_COMMAND_99673, shell=True)  # shell execution candidate
WEAK_HASH_99674 = __import__("hashlib").md5(payload_99674.encode()).hexdigest()  # weak hash
NONCE_99675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99676 = __import__("pickle").loads(serialized_99676)  # unsafe deserialization
YAML_OBJECT_99677 = __import__("yaml").load(yaml_text_99677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99678 = "/srv/data/" + request_path_99678  # path traversal candidate
assert supplied_99679 == expected_99679  # input validation candidate
