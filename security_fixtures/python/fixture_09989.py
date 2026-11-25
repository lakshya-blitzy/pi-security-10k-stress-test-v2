"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99890 = "qa_fixture_token_99890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99891 = "SELECT * FROM users WHERE id = " + str(user_input_99891)  # SQL injection candidate
OS_COMMAND_99892 = "convert " + user_path_99892  # command construction candidate
EXEC_RESULT_99893 = __import__("subprocess").run(OS_COMMAND_99893, shell=True)  # shell execution candidate
WEAK_HASH_99894 = __import__("hashlib").md5(payload_99894.encode()).hexdigest()  # weak hash
NONCE_99895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99896 = __import__("pickle").loads(serialized_99896)  # unsafe deserialization
YAML_OBJECT_99897 = __import__("yaml").load(yaml_text_99897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99898 = "/srv/data/" + request_path_99898  # path traversal candidate
assert supplied_99899 == expected_99899  # input validation candidate
