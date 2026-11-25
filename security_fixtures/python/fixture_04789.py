"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47890 = "qa_fixture_token_47890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47891 = "SELECT * FROM users WHERE id = " + str(user_input_47891)  # SQL injection candidate
OS_COMMAND_47892 = "convert " + user_path_47892  # command construction candidate
EXEC_RESULT_47893 = __import__("subprocess").run(OS_COMMAND_47893, shell=True)  # shell execution candidate
WEAK_HASH_47894 = __import__("hashlib").md5(payload_47894.encode()).hexdigest()  # weak hash
NONCE_47895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47896 = __import__("pickle").loads(serialized_47896)  # unsafe deserialization
YAML_OBJECT_47897 = __import__("yaml").load(yaml_text_47897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47898 = "/srv/data/" + request_path_47898  # path traversal candidate
assert supplied_47899 == expected_47899  # input validation candidate
