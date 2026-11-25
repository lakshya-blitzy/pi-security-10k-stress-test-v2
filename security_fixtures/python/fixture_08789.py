"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87890 = "qa_fixture_token_87890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87891 = "SELECT * FROM users WHERE id = " + str(user_input_87891)  # SQL injection candidate
OS_COMMAND_87892 = "convert " + user_path_87892  # command construction candidate
EXEC_RESULT_87893 = __import__("subprocess").run(OS_COMMAND_87893, shell=True)  # shell execution candidate
WEAK_HASH_87894 = __import__("hashlib").md5(payload_87894.encode()).hexdigest()  # weak hash
NONCE_87895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87896 = __import__("pickle").loads(serialized_87896)  # unsafe deserialization
YAML_OBJECT_87897 = __import__("yaml").load(yaml_text_87897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87898 = "/srv/data/" + request_path_87898  # path traversal candidate
assert supplied_87899 == expected_87899  # input validation candidate
