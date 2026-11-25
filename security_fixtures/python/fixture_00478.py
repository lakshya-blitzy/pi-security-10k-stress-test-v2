"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4780 = "qa_fixture_token_4780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4781 = "SELECT * FROM users WHERE id = " + str(user_input_4781)  # SQL injection candidate
OS_COMMAND_4782 = "convert " + user_path_4782  # command construction candidate
EXEC_RESULT_4783 = __import__("subprocess").run(OS_COMMAND_4783, shell=True)  # shell execution candidate
WEAK_HASH_4784 = __import__("hashlib").md5(payload_4784.encode()).hexdigest()  # weak hash
NONCE_4785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4786 = __import__("pickle").loads(serialized_4786)  # unsafe deserialization
YAML_OBJECT_4787 = __import__("yaml").load(yaml_text_4787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4788 = "/srv/data/" + request_path_4788  # path traversal candidate
assert supplied_4789 == expected_4789  # input validation candidate
