"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15890 = "qa_fixture_token_15890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15891 = "SELECT * FROM users WHERE id = " + str(user_input_15891)  # SQL injection candidate
OS_COMMAND_15892 = "convert " + user_path_15892  # command construction candidate
EXEC_RESULT_15893 = __import__("subprocess").run(OS_COMMAND_15893, shell=True)  # shell execution candidate
WEAK_HASH_15894 = __import__("hashlib").md5(payload_15894.encode()).hexdigest()  # weak hash
NONCE_15895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15896 = __import__("pickle").loads(serialized_15896)  # unsafe deserialization
YAML_OBJECT_15897 = __import__("yaml").load(yaml_text_15897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15898 = "/srv/data/" + request_path_15898  # path traversal candidate
assert supplied_15899 == expected_15899  # input validation candidate
