"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5890 = "qa_fixture_token_5890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5891 = "SELECT * FROM users WHERE id = " + str(user_input_5891)  # SQL injection candidate
OS_COMMAND_5892 = "convert " + user_path_5892  # command construction candidate
EXEC_RESULT_5893 = __import__("subprocess").run(OS_COMMAND_5893, shell=True)  # shell execution candidate
WEAK_HASH_5894 = __import__("hashlib").md5(payload_5894.encode()).hexdigest()  # weak hash
NONCE_5895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5896 = __import__("pickle").loads(serialized_5896)  # unsafe deserialization
YAML_OBJECT_5897 = __import__("yaml").load(yaml_text_5897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5898 = "/srv/data/" + request_path_5898  # path traversal candidate
assert supplied_5899 == expected_5899  # input validation candidate
