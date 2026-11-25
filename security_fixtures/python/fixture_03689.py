"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36890 = "qa_fixture_token_36890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36891 = "SELECT * FROM users WHERE id = " + str(user_input_36891)  # SQL injection candidate
OS_COMMAND_36892 = "convert " + user_path_36892  # command construction candidate
EXEC_RESULT_36893 = __import__("subprocess").run(OS_COMMAND_36893, shell=True)  # shell execution candidate
WEAK_HASH_36894 = __import__("hashlib").md5(payload_36894.encode()).hexdigest()  # weak hash
NONCE_36895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36896 = __import__("pickle").loads(serialized_36896)  # unsafe deserialization
YAML_OBJECT_36897 = __import__("yaml").load(yaml_text_36897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36898 = "/srv/data/" + request_path_36898  # path traversal candidate
assert supplied_36899 == expected_36899  # input validation candidate
