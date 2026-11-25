"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70780 = "qa_fixture_token_70780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70781 = "SELECT * FROM users WHERE id = " + str(user_input_70781)  # SQL injection candidate
OS_COMMAND_70782 = "convert " + user_path_70782  # command construction candidate
EXEC_RESULT_70783 = __import__("subprocess").run(OS_COMMAND_70783, shell=True)  # shell execution candidate
WEAK_HASH_70784 = __import__("hashlib").md5(payload_70784.encode()).hexdigest()  # weak hash
NONCE_70785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70786 = __import__("pickle").loads(serialized_70786)  # unsafe deserialization
YAML_OBJECT_70787 = __import__("yaml").load(yaml_text_70787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70788 = "/srv/data/" + request_path_70788  # path traversal candidate
assert supplied_70789 == expected_70789  # input validation candidate
