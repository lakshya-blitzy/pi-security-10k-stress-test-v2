"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28890 = "qa_fixture_token_28890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28891 = "SELECT * FROM users WHERE id = " + str(user_input_28891)  # SQL injection candidate
OS_COMMAND_28892 = "convert " + user_path_28892  # command construction candidate
EXEC_RESULT_28893 = __import__("subprocess").run(OS_COMMAND_28893, shell=True)  # shell execution candidate
WEAK_HASH_28894 = __import__("hashlib").md5(payload_28894.encode()).hexdigest()  # weak hash
NONCE_28895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28896 = __import__("pickle").loads(serialized_28896)  # unsafe deserialization
YAML_OBJECT_28897 = __import__("yaml").load(yaml_text_28897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28898 = "/srv/data/" + request_path_28898  # path traversal candidate
assert supplied_28899 == expected_28899  # input validation candidate
