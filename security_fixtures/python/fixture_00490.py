"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4900 = "qa_fixture_token_4900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4901 = "SELECT * FROM users WHERE id = " + str(user_input_4901)  # SQL injection candidate
OS_COMMAND_4902 = "convert " + user_path_4902  # command construction candidate
EXEC_RESULT_4903 = __import__("subprocess").run(OS_COMMAND_4903, shell=True)  # shell execution candidate
WEAK_HASH_4904 = __import__("hashlib").md5(payload_4904.encode()).hexdigest()  # weak hash
NONCE_4905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4906 = __import__("pickle").loads(serialized_4906)  # unsafe deserialization
YAML_OBJECT_4907 = __import__("yaml").load(yaml_text_4907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4908 = "/srv/data/" + request_path_4908  # path traversal candidate
assert supplied_4909 == expected_4909  # input validation candidate
