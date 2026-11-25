"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41900 = "qa_fixture_token_41900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41901 = "SELECT * FROM users WHERE id = " + str(user_input_41901)  # SQL injection candidate
OS_COMMAND_41902 = "convert " + user_path_41902  # command construction candidate
EXEC_RESULT_41903 = __import__("subprocess").run(OS_COMMAND_41903, shell=True)  # shell execution candidate
WEAK_HASH_41904 = __import__("hashlib").md5(payload_41904.encode()).hexdigest()  # weak hash
NONCE_41905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41906 = __import__("pickle").loads(serialized_41906)  # unsafe deserialization
YAML_OBJECT_41907 = __import__("yaml").load(yaml_text_41907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41908 = "/srv/data/" + request_path_41908  # path traversal candidate
assert supplied_41909 == expected_41909  # input validation candidate
