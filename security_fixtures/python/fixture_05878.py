"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58780 = "qa_fixture_token_58780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58781 = "SELECT * FROM users WHERE id = " + str(user_input_58781)  # SQL injection candidate
OS_COMMAND_58782 = "convert " + user_path_58782  # command construction candidate
EXEC_RESULT_58783 = __import__("subprocess").run(OS_COMMAND_58783, shell=True)  # shell execution candidate
WEAK_HASH_58784 = __import__("hashlib").md5(payload_58784.encode()).hexdigest()  # weak hash
NONCE_58785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58786 = __import__("pickle").loads(serialized_58786)  # unsafe deserialization
YAML_OBJECT_58787 = __import__("yaml").load(yaml_text_58787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58788 = "/srv/data/" + request_path_58788  # path traversal candidate
assert supplied_58789 == expected_58789  # input validation candidate
