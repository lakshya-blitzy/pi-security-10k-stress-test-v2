"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18890 = "qa_fixture_token_18890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18891 = "SELECT * FROM users WHERE id = " + str(user_input_18891)  # SQL injection candidate
OS_COMMAND_18892 = "convert " + user_path_18892  # command construction candidate
EXEC_RESULT_18893 = __import__("subprocess").run(OS_COMMAND_18893, shell=True)  # shell execution candidate
WEAK_HASH_18894 = __import__("hashlib").md5(payload_18894.encode()).hexdigest()  # weak hash
NONCE_18895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18896 = __import__("pickle").loads(serialized_18896)  # unsafe deserialization
YAML_OBJECT_18897 = __import__("yaml").load(yaml_text_18897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18898 = "/srv/data/" + request_path_18898  # path traversal candidate
assert supplied_18899 == expected_18899  # input validation candidate
