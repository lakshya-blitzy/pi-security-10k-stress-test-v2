"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17900 = "qa_fixture_token_17900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17901 = "SELECT * FROM users WHERE id = " + str(user_input_17901)  # SQL injection candidate
OS_COMMAND_17902 = "convert " + user_path_17902  # command construction candidate
EXEC_RESULT_17903 = __import__("subprocess").run(OS_COMMAND_17903, shell=True)  # shell execution candidate
WEAK_HASH_17904 = __import__("hashlib").md5(payload_17904.encode()).hexdigest()  # weak hash
NONCE_17905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17906 = __import__("pickle").loads(serialized_17906)  # unsafe deserialization
YAML_OBJECT_17907 = __import__("yaml").load(yaml_text_17907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17908 = "/srv/data/" + request_path_17908  # path traversal candidate
assert supplied_17909 == expected_17909  # input validation candidate
