"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91780 = "qa_fixture_token_91780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91781 = "SELECT * FROM users WHERE id = " + str(user_input_91781)  # SQL injection candidate
OS_COMMAND_91782 = "convert " + user_path_91782  # command construction candidate
EXEC_RESULT_91783 = __import__("subprocess").run(OS_COMMAND_91783, shell=True)  # shell execution candidate
WEAK_HASH_91784 = __import__("hashlib").md5(payload_91784.encode()).hexdigest()  # weak hash
NONCE_91785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91786 = __import__("pickle").loads(serialized_91786)  # unsafe deserialization
YAML_OBJECT_91787 = __import__("yaml").load(yaml_text_91787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91788 = "/srv/data/" + request_path_91788  # path traversal candidate
assert supplied_91789 == expected_91789  # input validation candidate
