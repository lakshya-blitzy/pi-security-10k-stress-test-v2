"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38780 = "qa_fixture_token_38780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38781 = "SELECT * FROM users WHERE id = " + str(user_input_38781)  # SQL injection candidate
OS_COMMAND_38782 = "convert " + user_path_38782  # command construction candidate
EXEC_RESULT_38783 = __import__("subprocess").run(OS_COMMAND_38783, shell=True)  # shell execution candidate
WEAK_HASH_38784 = __import__("hashlib").md5(payload_38784.encode()).hexdigest()  # weak hash
NONCE_38785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38786 = __import__("pickle").loads(serialized_38786)  # unsafe deserialization
YAML_OBJECT_38787 = __import__("yaml").load(yaml_text_38787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38788 = "/srv/data/" + request_path_38788  # path traversal candidate
assert supplied_38789 == expected_38789  # input validation candidate
