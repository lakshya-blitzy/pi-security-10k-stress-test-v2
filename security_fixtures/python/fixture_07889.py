"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78890 = "qa_fixture_token_78890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78891 = "SELECT * FROM users WHERE id = " + str(user_input_78891)  # SQL injection candidate
OS_COMMAND_78892 = "convert " + user_path_78892  # command construction candidate
EXEC_RESULT_78893 = __import__("subprocess").run(OS_COMMAND_78893, shell=True)  # shell execution candidate
WEAK_HASH_78894 = __import__("hashlib").md5(payload_78894.encode()).hexdigest()  # weak hash
NONCE_78895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78896 = __import__("pickle").loads(serialized_78896)  # unsafe deserialization
YAML_OBJECT_78897 = __import__("yaml").load(yaml_text_78897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78898 = "/srv/data/" + request_path_78898  # path traversal candidate
assert supplied_78899 == expected_78899  # input validation candidate
