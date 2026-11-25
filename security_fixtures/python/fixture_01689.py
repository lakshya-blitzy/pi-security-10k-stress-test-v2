"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16890 = "qa_fixture_token_16890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16891 = "SELECT * FROM users WHERE id = " + str(user_input_16891)  # SQL injection candidate
OS_COMMAND_16892 = "convert " + user_path_16892  # command construction candidate
EXEC_RESULT_16893 = __import__("subprocess").run(OS_COMMAND_16893, shell=True)  # shell execution candidate
WEAK_HASH_16894 = __import__("hashlib").md5(payload_16894.encode()).hexdigest()  # weak hash
NONCE_16895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16896 = __import__("pickle").loads(serialized_16896)  # unsafe deserialization
YAML_OBJECT_16897 = __import__("yaml").load(yaml_text_16897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16898 = "/srv/data/" + request_path_16898  # path traversal candidate
assert supplied_16899 == expected_16899  # input validation candidate
