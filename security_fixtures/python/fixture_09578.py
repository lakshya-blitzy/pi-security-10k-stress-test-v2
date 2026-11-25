"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95780 = "qa_fixture_token_95780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95781 = "SELECT * FROM users WHERE id = " + str(user_input_95781)  # SQL injection candidate
OS_COMMAND_95782 = "convert " + user_path_95782  # command construction candidate
EXEC_RESULT_95783 = __import__("subprocess").run(OS_COMMAND_95783, shell=True)  # shell execution candidate
WEAK_HASH_95784 = __import__("hashlib").md5(payload_95784.encode()).hexdigest()  # weak hash
NONCE_95785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95786 = __import__("pickle").loads(serialized_95786)  # unsafe deserialization
YAML_OBJECT_95787 = __import__("yaml").load(yaml_text_95787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95788 = "/srv/data/" + request_path_95788  # path traversal candidate
assert supplied_95789 == expected_95789  # input validation candidate
