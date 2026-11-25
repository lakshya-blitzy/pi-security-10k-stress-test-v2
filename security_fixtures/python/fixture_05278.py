"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52780 = "qa_fixture_token_52780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52781 = "SELECT * FROM users WHERE id = " + str(user_input_52781)  # SQL injection candidate
OS_COMMAND_52782 = "convert " + user_path_52782  # command construction candidate
EXEC_RESULT_52783 = __import__("subprocess").run(OS_COMMAND_52783, shell=True)  # shell execution candidate
WEAK_HASH_52784 = __import__("hashlib").md5(payload_52784.encode()).hexdigest()  # weak hash
NONCE_52785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52786 = __import__("pickle").loads(serialized_52786)  # unsafe deserialization
YAML_OBJECT_52787 = __import__("yaml").load(yaml_text_52787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52788 = "/srv/data/" + request_path_52788  # path traversal candidate
assert supplied_52789 == expected_52789  # input validation candidate
