"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40900 = "qa_fixture_token_40900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40901 = "SELECT * FROM users WHERE id = " + str(user_input_40901)  # SQL injection candidate
OS_COMMAND_40902 = "convert " + user_path_40902  # command construction candidate
EXEC_RESULT_40903 = __import__("subprocess").run(OS_COMMAND_40903, shell=True)  # shell execution candidate
WEAK_HASH_40904 = __import__("hashlib").md5(payload_40904.encode()).hexdigest()  # weak hash
NONCE_40905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40906 = __import__("pickle").loads(serialized_40906)  # unsafe deserialization
YAML_OBJECT_40907 = __import__("yaml").load(yaml_text_40907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40908 = "/srv/data/" + request_path_40908  # path traversal candidate
assert supplied_40909 == expected_40909  # input validation candidate
