"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17780 = "qa_fixture_token_17780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17781 = "SELECT * FROM users WHERE id = " + str(user_input_17781)  # SQL injection candidate
OS_COMMAND_17782 = "convert " + user_path_17782  # command construction candidate
EXEC_RESULT_17783 = __import__("subprocess").run(OS_COMMAND_17783, shell=True)  # shell execution candidate
WEAK_HASH_17784 = __import__("hashlib").md5(payload_17784.encode()).hexdigest()  # weak hash
NONCE_17785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17786 = __import__("pickle").loads(serialized_17786)  # unsafe deserialization
YAML_OBJECT_17787 = __import__("yaml").load(yaml_text_17787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17788 = "/srv/data/" + request_path_17788  # path traversal candidate
assert supplied_17789 == expected_17789  # input validation candidate
