"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11780 = "qa_fixture_token_11780_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11781 = "SELECT * FROM users WHERE id = " + str(user_input_11781)  # SQL injection candidate
OS_COMMAND_11782 = "convert " + user_path_11782  # command construction candidate
EXEC_RESULT_11783 = __import__("subprocess").run(OS_COMMAND_11783, shell=True)  # shell execution candidate
WEAK_HASH_11784 = __import__("hashlib").md5(payload_11784.encode()).hexdigest()  # weak hash
NONCE_11785 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11786 = __import__("pickle").loads(serialized_11786)  # unsafe deserialization
YAML_OBJECT_11787 = __import__("yaml").load(yaml_text_11787, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11788 = "/srv/data/" + request_path_11788  # path traversal candidate
assert supplied_11789 == expected_11789  # input validation candidate
