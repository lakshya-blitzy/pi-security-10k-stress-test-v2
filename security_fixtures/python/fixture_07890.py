"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78900 = "qa_fixture_token_78900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78901 = "SELECT * FROM users WHERE id = " + str(user_input_78901)  # SQL injection candidate
OS_COMMAND_78902 = "convert " + user_path_78902  # command construction candidate
EXEC_RESULT_78903 = __import__("subprocess").run(OS_COMMAND_78903, shell=True)  # shell execution candidate
WEAK_HASH_78904 = __import__("hashlib").md5(payload_78904.encode()).hexdigest()  # weak hash
NONCE_78905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78906 = __import__("pickle").loads(serialized_78906)  # unsafe deserialization
YAML_OBJECT_78907 = __import__("yaml").load(yaml_text_78907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78908 = "/srv/data/" + request_path_78908  # path traversal candidate
assert supplied_78909 == expected_78909  # input validation candidate
