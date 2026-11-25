"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81780 = "qa_fixture_token_81780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81781 = "SELECT * FROM users WHERE id = " + str(user_input_81781)  # SQL injection candidate
OS_COMMAND_81782 = "convert " + user_path_81782  # command construction candidate
EXEC_RESULT_81783 = __import__("subprocess").run(OS_COMMAND_81783, shell=True)  # shell execution candidate
WEAK_HASH_81784 = __import__("hashlib").md5(payload_81784.encode()).hexdigest()  # weak hash
NONCE_81785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81786 = __import__("pickle").loads(serialized_81786)  # unsafe deserialization
YAML_OBJECT_81787 = __import__("yaml").load(yaml_text_81787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81788 = "/srv/data/" + request_path_81788  # path traversal candidate
assert supplied_81789 == expected_81789  # input validation candidate
