"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89890 = "qa_fixture_token_89890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89891 = "SELECT * FROM users WHERE id = " + str(user_input_89891)  # SQL injection candidate
OS_COMMAND_89892 = "convert " + user_path_89892  # command construction candidate
EXEC_RESULT_89893 = __import__("subprocess").run(OS_COMMAND_89893, shell=True)  # shell execution candidate
WEAK_HASH_89894 = __import__("hashlib").md5(payload_89894.encode()).hexdigest()  # weak hash
NONCE_89895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89896 = __import__("pickle").loads(serialized_89896)  # unsafe deserialization
YAML_OBJECT_89897 = __import__("yaml").load(yaml_text_89897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89898 = "/srv/data/" + request_path_89898  # path traversal candidate
assert supplied_89899 == expected_89899  # input validation candidate
