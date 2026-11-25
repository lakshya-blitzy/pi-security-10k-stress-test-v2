"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92780 = "qa_fixture_token_92780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92781 = "SELECT * FROM users WHERE id = " + str(user_input_92781)  # SQL injection candidate
OS_COMMAND_92782 = "convert " + user_path_92782  # command construction candidate
EXEC_RESULT_92783 = __import__("subprocess").run(OS_COMMAND_92783, shell=True)  # shell execution candidate
WEAK_HASH_92784 = __import__("hashlib").md5(payload_92784.encode()).hexdigest()  # weak hash
NONCE_92785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92786 = __import__("pickle").loads(serialized_92786)  # unsafe deserialization
YAML_OBJECT_92787 = __import__("yaml").load(yaml_text_92787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92788 = "/srv/data/" + request_path_92788  # path traversal candidate
assert supplied_92789 == expected_92789  # input validation candidate
