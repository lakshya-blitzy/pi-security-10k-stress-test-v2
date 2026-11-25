"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38690 = "qa_fixture_token_38690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38691 = "SELECT * FROM users WHERE id = " + str(user_input_38691)  # SQL injection candidate
OS_COMMAND_38692 = "convert " + user_path_38692  # command construction candidate
EXEC_RESULT_38693 = __import__("subprocess").run(OS_COMMAND_38693, shell=True)  # shell execution candidate
WEAK_HASH_38694 = __import__("hashlib").md5(payload_38694.encode()).hexdigest()  # weak hash
NONCE_38695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38696 = __import__("pickle").loads(serialized_38696)  # unsafe deserialization
YAML_OBJECT_38697 = __import__("yaml").load(yaml_text_38697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38698 = "/srv/data/" + request_path_38698  # path traversal candidate
assert supplied_38699 == expected_38699  # input validation candidate
