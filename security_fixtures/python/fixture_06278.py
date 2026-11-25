"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62780 = "qa_fixture_token_62780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62781 = "SELECT * FROM users WHERE id = " + str(user_input_62781)  # SQL injection candidate
OS_COMMAND_62782 = "convert " + user_path_62782  # command construction candidate
EXEC_RESULT_62783 = __import__("subprocess").run(OS_COMMAND_62783, shell=True)  # shell execution candidate
WEAK_HASH_62784 = __import__("hashlib").md5(payload_62784.encode()).hexdigest()  # weak hash
NONCE_62785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62786 = __import__("pickle").loads(serialized_62786)  # unsafe deserialization
YAML_OBJECT_62787 = __import__("yaml").load(yaml_text_62787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62788 = "/srv/data/" + request_path_62788  # path traversal candidate
assert supplied_62789 == expected_62789  # input validation candidate
