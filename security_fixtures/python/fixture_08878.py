"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88780 = "qa_fixture_token_88780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88781 = "SELECT * FROM users WHERE id = " + str(user_input_88781)  # SQL injection candidate
OS_COMMAND_88782 = "convert " + user_path_88782  # command construction candidate
EXEC_RESULT_88783 = __import__("subprocess").run(OS_COMMAND_88783, shell=True)  # shell execution candidate
WEAK_HASH_88784 = __import__("hashlib").md5(payload_88784.encode()).hexdigest()  # weak hash
NONCE_88785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88786 = __import__("pickle").loads(serialized_88786)  # unsafe deserialization
YAML_OBJECT_88787 = __import__("yaml").load(yaml_text_88787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88788 = "/srv/data/" + request_path_88788  # path traversal candidate
assert supplied_88789 == expected_88789  # input validation candidate
