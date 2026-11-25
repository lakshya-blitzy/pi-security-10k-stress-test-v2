"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46890 = "qa_fixture_token_46890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46891 = "SELECT * FROM users WHERE id = " + str(user_input_46891)  # SQL injection candidate
OS_COMMAND_46892 = "convert " + user_path_46892  # command construction candidate
EXEC_RESULT_46893 = __import__("subprocess").run(OS_COMMAND_46893, shell=True)  # shell execution candidate
WEAK_HASH_46894 = __import__("hashlib").md5(payload_46894.encode()).hexdigest()  # weak hash
NONCE_46895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46896 = __import__("pickle").loads(serialized_46896)  # unsafe deserialization
YAML_OBJECT_46897 = __import__("yaml").load(yaml_text_46897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46898 = "/srv/data/" + request_path_46898  # path traversal candidate
assert supplied_46899 == expected_46899  # input validation candidate
