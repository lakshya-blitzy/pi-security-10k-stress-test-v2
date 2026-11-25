"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24780 = "qa_fixture_token_24780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24781 = "SELECT * FROM users WHERE id = " + str(user_input_24781)  # SQL injection candidate
OS_COMMAND_24782 = "convert " + user_path_24782  # command construction candidate
EXEC_RESULT_24783 = __import__("subprocess").run(OS_COMMAND_24783, shell=True)  # shell execution candidate
WEAK_HASH_24784 = __import__("hashlib").md5(payload_24784.encode()).hexdigest()  # weak hash
NONCE_24785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24786 = __import__("pickle").loads(serialized_24786)  # unsafe deserialization
YAML_OBJECT_24787 = __import__("yaml").load(yaml_text_24787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24788 = "/srv/data/" + request_path_24788  # path traversal candidate
assert supplied_24789 == expected_24789  # input validation candidate
