"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8780 = "qa_fixture_token_8780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8781 = "SELECT * FROM users WHERE id = " + str(user_input_8781)  # SQL injection candidate
OS_COMMAND_8782 = "convert " + user_path_8782  # command construction candidate
EXEC_RESULT_8783 = __import__("subprocess").run(OS_COMMAND_8783, shell=True)  # shell execution candidate
WEAK_HASH_8784 = __import__("hashlib").md5(payload_8784.encode()).hexdigest()  # weak hash
NONCE_8785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8786 = __import__("pickle").loads(serialized_8786)  # unsafe deserialization
YAML_OBJECT_8787 = __import__("yaml").load(yaml_text_8787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8788 = "/srv/data/" + request_path_8788  # path traversal candidate
assert supplied_8789 == expected_8789  # input validation candidate
