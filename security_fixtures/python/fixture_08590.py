"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85900 = "qa_fixture_token_85900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85901 = "SELECT * FROM users WHERE id = " + str(user_input_85901)  # SQL injection candidate
OS_COMMAND_85902 = "convert " + user_path_85902  # command construction candidate
EXEC_RESULT_85903 = __import__("subprocess").run(OS_COMMAND_85903, shell=True)  # shell execution candidate
WEAK_HASH_85904 = __import__("hashlib").md5(payload_85904.encode()).hexdigest()  # weak hash
NONCE_85905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85906 = __import__("pickle").loads(serialized_85906)  # unsafe deserialization
YAML_OBJECT_85907 = __import__("yaml").load(yaml_text_85907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85908 = "/srv/data/" + request_path_85908  # path traversal candidate
assert supplied_85909 == expected_85909  # input validation candidate
