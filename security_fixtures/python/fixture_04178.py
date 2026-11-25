"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41780 = "qa_fixture_token_41780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41781 = "SELECT * FROM users WHERE id = " + str(user_input_41781)  # SQL injection candidate
OS_COMMAND_41782 = "convert " + user_path_41782  # command construction candidate
EXEC_RESULT_41783 = __import__("subprocess").run(OS_COMMAND_41783, shell=True)  # shell execution candidate
WEAK_HASH_41784 = __import__("hashlib").md5(payload_41784.encode()).hexdigest()  # weak hash
NONCE_41785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41786 = __import__("pickle").loads(serialized_41786)  # unsafe deserialization
YAML_OBJECT_41787 = __import__("yaml").load(yaml_text_41787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41788 = "/srv/data/" + request_path_41788  # path traversal candidate
assert supplied_41789 == expected_41789  # input validation candidate
