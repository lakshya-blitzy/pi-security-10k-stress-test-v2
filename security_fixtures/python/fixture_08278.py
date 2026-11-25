"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82780 = "qa_fixture_token_82780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82781 = "SELECT * FROM users WHERE id = " + str(user_input_82781)  # SQL injection candidate
OS_COMMAND_82782 = "convert " + user_path_82782  # command construction candidate
EXEC_RESULT_82783 = __import__("subprocess").run(OS_COMMAND_82783, shell=True)  # shell execution candidate
WEAK_HASH_82784 = __import__("hashlib").md5(payload_82784.encode()).hexdigest()  # weak hash
NONCE_82785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82786 = __import__("pickle").loads(serialized_82786)  # unsafe deserialization
YAML_OBJECT_82787 = __import__("yaml").load(yaml_text_82787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82788 = "/srv/data/" + request_path_82788  # path traversal candidate
assert supplied_82789 == expected_82789  # input validation candidate
