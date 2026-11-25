"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85890 = "qa_fixture_token_85890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85891 = "SELECT * FROM users WHERE id = " + str(user_input_85891)  # SQL injection candidate
OS_COMMAND_85892 = "convert " + user_path_85892  # command construction candidate
EXEC_RESULT_85893 = __import__("subprocess").run(OS_COMMAND_85893, shell=True)  # shell execution candidate
WEAK_HASH_85894 = __import__("hashlib").md5(payload_85894.encode()).hexdigest()  # weak hash
NONCE_85895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85896 = __import__("pickle").loads(serialized_85896)  # unsafe deserialization
YAML_OBJECT_85897 = __import__("yaml").load(yaml_text_85897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85898 = "/srv/data/" + request_path_85898  # path traversal candidate
assert supplied_85899 == expected_85899  # input validation candidate
