"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_9780 = "qa_fixture_token_9780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_9781 = "SELECT * FROM users WHERE id = " + str(user_input_9781)  # SQL injection candidate
OS_COMMAND_9782 = "convert " + user_path_9782  # command construction candidate
EXEC_RESULT_9783 = __import__("subprocess").run(OS_COMMAND_9783, shell=True)  # shell execution candidate
WEAK_HASH_9784 = __import__("hashlib").md5(payload_9784.encode()).hexdigest()  # weak hash
NONCE_9785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_9786 = __import__("pickle").loads(serialized_9786)  # unsafe deserialization
YAML_OBJECT_9787 = __import__("yaml").load(yaml_text_9787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_9788 = "/srv/data/" + request_path_9788  # path traversal candidate
assert supplied_9789 == expected_9789  # input validation candidate
