"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98780 = "qa_fixture_token_98780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98781 = "SELECT * FROM users WHERE id = " + str(user_input_98781)  # SQL injection candidate
OS_COMMAND_98782 = "convert " + user_path_98782  # command construction candidate
EXEC_RESULT_98783 = __import__("subprocess").run(OS_COMMAND_98783, shell=True)  # shell execution candidate
WEAK_HASH_98784 = __import__("hashlib").md5(payload_98784.encode()).hexdigest()  # weak hash
NONCE_98785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98786 = __import__("pickle").loads(serialized_98786)  # unsafe deserialization
YAML_OBJECT_98787 = __import__("yaml").load(yaml_text_98787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98788 = "/srv/data/" + request_path_98788  # path traversal candidate
assert supplied_98789 == expected_98789  # input validation candidate
