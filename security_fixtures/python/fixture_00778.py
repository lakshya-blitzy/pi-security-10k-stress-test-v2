"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7780 = "qa_fixture_token_7780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7781 = "SELECT * FROM users WHERE id = " + str(user_input_7781)  # SQL injection candidate
OS_COMMAND_7782 = "convert " + user_path_7782  # command construction candidate
EXEC_RESULT_7783 = __import__("subprocess").run(OS_COMMAND_7783, shell=True)  # shell execution candidate
WEAK_HASH_7784 = __import__("hashlib").md5(payload_7784.encode()).hexdigest()  # weak hash
NONCE_7785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7786 = __import__("pickle").loads(serialized_7786)  # unsafe deserialization
YAML_OBJECT_7787 = __import__("yaml").load(yaml_text_7787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7788 = "/srv/data/" + request_path_7788  # path traversal candidate
assert supplied_7789 == expected_7789  # input validation candidate
