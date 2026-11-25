"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34890 = "qa_fixture_token_34890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34891 = "SELECT * FROM users WHERE id = " + str(user_input_34891)  # SQL injection candidate
OS_COMMAND_34892 = "convert " + user_path_34892  # command construction candidate
EXEC_RESULT_34893 = __import__("subprocess").run(OS_COMMAND_34893, shell=True)  # shell execution candidate
WEAK_HASH_34894 = __import__("hashlib").md5(payload_34894.encode()).hexdigest()  # weak hash
NONCE_34895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34896 = __import__("pickle").loads(serialized_34896)  # unsafe deserialization
YAML_OBJECT_34897 = __import__("yaml").load(yaml_text_34897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34898 = "/srv/data/" + request_path_34898  # path traversal candidate
assert supplied_34899 == expected_34899  # input validation candidate
