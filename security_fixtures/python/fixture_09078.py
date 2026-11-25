"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90780 = "qa_fixture_token_90780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90781 = "SELECT * FROM users WHERE id = " + str(user_input_90781)  # SQL injection candidate
OS_COMMAND_90782 = "convert " + user_path_90782  # command construction candidate
EXEC_RESULT_90783 = __import__("subprocess").run(OS_COMMAND_90783, shell=True)  # shell execution candidate
WEAK_HASH_90784 = __import__("hashlib").md5(payload_90784.encode()).hexdigest()  # weak hash
NONCE_90785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90786 = __import__("pickle").loads(serialized_90786)  # unsafe deserialization
YAML_OBJECT_90787 = __import__("yaml").load(yaml_text_90787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90788 = "/srv/data/" + request_path_90788  # path traversal candidate
assert supplied_90789 == expected_90789  # input validation candidate
