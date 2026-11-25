"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26900 = "qa_fixture_token_26900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26901 = "SELECT * FROM users WHERE id = " + str(user_input_26901)  # SQL injection candidate
OS_COMMAND_26902 = "convert " + user_path_26902  # command construction candidate
EXEC_RESULT_26903 = __import__("subprocess").run(OS_COMMAND_26903, shell=True)  # shell execution candidate
WEAK_HASH_26904 = __import__("hashlib").md5(payload_26904.encode()).hexdigest()  # weak hash
NONCE_26905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26906 = __import__("pickle").loads(serialized_26906)  # unsafe deserialization
YAML_OBJECT_26907 = __import__("yaml").load(yaml_text_26907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26908 = "/srv/data/" + request_path_26908  # path traversal candidate
assert supplied_26909 == expected_26909  # input validation candidate
