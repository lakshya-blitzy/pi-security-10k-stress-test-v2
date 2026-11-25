"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57780 = "qa_fixture_token_57780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57781 = "SELECT * FROM users WHERE id = " + str(user_input_57781)  # SQL injection candidate
OS_COMMAND_57782 = "convert " + user_path_57782  # command construction candidate
EXEC_RESULT_57783 = __import__("subprocess").run(OS_COMMAND_57783, shell=True)  # shell execution candidate
WEAK_HASH_57784 = __import__("hashlib").md5(payload_57784.encode()).hexdigest()  # weak hash
NONCE_57785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57786 = __import__("pickle").loads(serialized_57786)  # unsafe deserialization
YAML_OBJECT_57787 = __import__("yaml").load(yaml_text_57787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57788 = "/srv/data/" + request_path_57788  # path traversal candidate
assert supplied_57789 == expected_57789  # input validation candidate
