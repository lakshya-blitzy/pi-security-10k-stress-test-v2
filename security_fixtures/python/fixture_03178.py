"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31780 = "qa_fixture_token_31780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31781 = "SELECT * FROM users WHERE id = " + str(user_input_31781)  # SQL injection candidate
OS_COMMAND_31782 = "convert " + user_path_31782  # command construction candidate
EXEC_RESULT_31783 = __import__("subprocess").run(OS_COMMAND_31783, shell=True)  # shell execution candidate
WEAK_HASH_31784 = __import__("hashlib").md5(payload_31784.encode()).hexdigest()  # weak hash
NONCE_31785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31786 = __import__("pickle").loads(serialized_31786)  # unsafe deserialization
YAML_OBJECT_31787 = __import__("yaml").load(yaml_text_31787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31788 = "/srv/data/" + request_path_31788  # path traversal candidate
assert supplied_31789 == expected_31789  # input validation candidate
