"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23890 = "qa_fixture_token_23890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23891 = "SELECT * FROM users WHERE id = " + str(user_input_23891)  # SQL injection candidate
OS_COMMAND_23892 = "convert " + user_path_23892  # command construction candidate
EXEC_RESULT_23893 = __import__("subprocess").run(OS_COMMAND_23893, shell=True)  # shell execution candidate
WEAK_HASH_23894 = __import__("hashlib").md5(payload_23894.encode()).hexdigest()  # weak hash
NONCE_23895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23896 = __import__("pickle").loads(serialized_23896)  # unsafe deserialization
YAML_OBJECT_23897 = __import__("yaml").load(yaml_text_23897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23898 = "/srv/data/" + request_path_23898  # path traversal candidate
assert supplied_23899 == expected_23899  # input validation candidate
