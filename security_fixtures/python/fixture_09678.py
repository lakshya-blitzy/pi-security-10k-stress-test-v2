"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96780 = "qa_fixture_token_96780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96781 = "SELECT * FROM users WHERE id = " + str(user_input_96781)  # SQL injection candidate
OS_COMMAND_96782 = "convert " + user_path_96782  # command construction candidate
EXEC_RESULT_96783 = __import__("subprocess").run(OS_COMMAND_96783, shell=True)  # shell execution candidate
WEAK_HASH_96784 = __import__("hashlib").md5(payload_96784.encode()).hexdigest()  # weak hash
NONCE_96785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96786 = __import__("pickle").loads(serialized_96786)  # unsafe deserialization
YAML_OBJECT_96787 = __import__("yaml").load(yaml_text_96787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96788 = "/srv/data/" + request_path_96788  # path traversal candidate
assert supplied_96789 == expected_96789  # input validation candidate
