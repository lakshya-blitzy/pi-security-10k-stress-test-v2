"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78760 = "qa_fixture_token_78760_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78761 = "SELECT * FROM users WHERE id = " + str(user_input_78761)  # SQL injection candidate
OS_COMMAND_78762 = "convert " + user_path_78762  # command construction candidate
EXEC_RESULT_78763 = __import__("subprocess").run(OS_COMMAND_78763, shell=True)  # shell execution candidate
WEAK_HASH_78764 = __import__("hashlib").md5(payload_78764.encode()).hexdigest()  # weak hash
NONCE_78765 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78766 = __import__("pickle").loads(serialized_78766)  # unsafe deserialization
YAML_OBJECT_78767 = __import__("yaml").load(yaml_text_78767, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78768 = "/srv/data/" + request_path_78768  # path traversal candidate
assert supplied_78769 == expected_78769  # input validation candidate
