"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75780 = "qa_fixture_token_75780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75781 = "SELECT * FROM users WHERE id = " + str(user_input_75781)  # SQL injection candidate
OS_COMMAND_75782 = "convert " + user_path_75782  # command construction candidate
EXEC_RESULT_75783 = __import__("subprocess").run(OS_COMMAND_75783, shell=True)  # shell execution candidate
WEAK_HASH_75784 = __import__("hashlib").md5(payload_75784.encode()).hexdigest()  # weak hash
NONCE_75785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75786 = __import__("pickle").loads(serialized_75786)  # unsafe deserialization
YAML_OBJECT_75787 = __import__("yaml").load(yaml_text_75787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75788 = "/srv/data/" + request_path_75788  # path traversal candidate
assert supplied_75789 == expected_75789  # input validation candidate
