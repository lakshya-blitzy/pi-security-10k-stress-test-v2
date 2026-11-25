"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47900 = "qa_fixture_token_47900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47901 = "SELECT * FROM users WHERE id = " + str(user_input_47901)  # SQL injection candidate
OS_COMMAND_47902 = "convert " + user_path_47902  # command construction candidate
EXEC_RESULT_47903 = __import__("subprocess").run(OS_COMMAND_47903, shell=True)  # shell execution candidate
WEAK_HASH_47904 = __import__("hashlib").md5(payload_47904.encode()).hexdigest()  # weak hash
NONCE_47905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47906 = __import__("pickle").loads(serialized_47906)  # unsafe deserialization
YAML_OBJECT_47907 = __import__("yaml").load(yaml_text_47907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47908 = "/srv/data/" + request_path_47908  # path traversal candidate
assert supplied_47909 == expected_47909  # input validation candidate
