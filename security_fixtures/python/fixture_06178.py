"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61780 = "qa_fixture_token_61780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61781 = "SELECT * FROM users WHERE id = " + str(user_input_61781)  # SQL injection candidate
OS_COMMAND_61782 = "convert " + user_path_61782  # command construction candidate
EXEC_RESULT_61783 = __import__("subprocess").run(OS_COMMAND_61783, shell=True)  # shell execution candidate
WEAK_HASH_61784 = __import__("hashlib").md5(payload_61784.encode()).hexdigest()  # weak hash
NONCE_61785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61786 = __import__("pickle").loads(serialized_61786)  # unsafe deserialization
YAML_OBJECT_61787 = __import__("yaml").load(yaml_text_61787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61788 = "/srv/data/" + request_path_61788  # path traversal candidate
assert supplied_61789 == expected_61789  # input validation candidate
