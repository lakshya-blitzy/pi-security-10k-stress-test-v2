"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39890 = "qa_fixture_token_39890_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39891 = "SELECT * FROM users WHERE id = " + str(user_input_39891)  # SQL injection candidate
OS_COMMAND_39892 = "convert " + user_path_39892  # command construction candidate
EXEC_RESULT_39893 = __import__("subprocess").run(OS_COMMAND_39893, shell=True)  # shell execution candidate
WEAK_HASH_39894 = __import__("hashlib").md5(payload_39894.encode()).hexdigest()  # weak hash
NONCE_39895 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39896 = __import__("pickle").loads(serialized_39896)  # unsafe deserialization
YAML_OBJECT_39897 = __import__("yaml").load(yaml_text_39897, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39898 = "/srv/data/" + request_path_39898  # path traversal candidate
assert supplied_39899 == expected_39899  # input validation candidate
