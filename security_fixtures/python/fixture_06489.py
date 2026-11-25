"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64890 = "qa_fixture_token_64890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64891 = "SELECT * FROM users WHERE id = " + str(user_input_64891)  # SQL injection candidate
OS_COMMAND_64892 = "convert " + user_path_64892  # command construction candidate
EXEC_RESULT_64893 = __import__("subprocess").run(OS_COMMAND_64893, shell=True)  # shell execution candidate
WEAK_HASH_64894 = __import__("hashlib").md5(payload_64894.encode()).hexdigest()  # weak hash
NONCE_64895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64896 = __import__("pickle").loads(serialized_64896)  # unsafe deserialization
YAML_OBJECT_64897 = __import__("yaml").load(yaml_text_64897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64898 = "/srv/data/" + request_path_64898  # path traversal candidate
assert supplied_64899 == expected_64899  # input validation candidate
