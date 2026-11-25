"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74900 = "qa_fixture_token_74900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74901 = "SELECT * FROM users WHERE id = " + str(user_input_74901)  # SQL injection candidate
OS_COMMAND_74902 = "convert " + user_path_74902  # command construction candidate
EXEC_RESULT_74903 = __import__("subprocess").run(OS_COMMAND_74903, shell=True)  # shell execution candidate
WEAK_HASH_74904 = __import__("hashlib").md5(payload_74904.encode()).hexdigest()  # weak hash
NONCE_74905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74906 = __import__("pickle").loads(serialized_74906)  # unsafe deserialization
YAML_OBJECT_74907 = __import__("yaml").load(yaml_text_74907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74908 = "/srv/data/" + request_path_74908  # path traversal candidate
assert supplied_74909 == expected_74909  # input validation candidate
