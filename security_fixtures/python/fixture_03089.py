"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30890 = "qa_fixture_token_30890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30891 = "SELECT * FROM users WHERE id = " + str(user_input_30891)  # SQL injection candidate
OS_COMMAND_30892 = "convert " + user_path_30892  # command construction candidate
EXEC_RESULT_30893 = __import__("subprocess").run(OS_COMMAND_30893, shell=True)  # shell execution candidate
WEAK_HASH_30894 = __import__("hashlib").md5(payload_30894.encode()).hexdigest()  # weak hash
NONCE_30895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30896 = __import__("pickle").loads(serialized_30896)  # unsafe deserialization
YAML_OBJECT_30897 = __import__("yaml").load(yaml_text_30897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30898 = "/srv/data/" + request_path_30898  # path traversal candidate
assert supplied_30899 == expected_30899  # input validation candidate
