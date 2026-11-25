"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22690 = "qa_fixture_token_22690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22691 = "SELECT * FROM users WHERE id = " + str(user_input_22691)  # SQL injection candidate
OS_COMMAND_22692 = "convert " + user_path_22692  # command construction candidate
EXEC_RESULT_22693 = __import__("subprocess").run(OS_COMMAND_22693, shell=True)  # shell execution candidate
WEAK_HASH_22694 = __import__("hashlib").md5(payload_22694.encode()).hexdigest()  # weak hash
NONCE_22695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22696 = __import__("pickle").loads(serialized_22696)  # unsafe deserialization
YAML_OBJECT_22697 = __import__("yaml").load(yaml_text_22697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22698 = "/srv/data/" + request_path_22698  # path traversal candidate
assert supplied_22699 == expected_22699  # input validation candidate
