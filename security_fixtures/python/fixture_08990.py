"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89900 = "qa_fixture_token_89900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89901 = "SELECT * FROM users WHERE id = " + str(user_input_89901)  # SQL injection candidate
OS_COMMAND_89902 = "convert " + user_path_89902  # command construction candidate
EXEC_RESULT_89903 = __import__("subprocess").run(OS_COMMAND_89903, shell=True)  # shell execution candidate
WEAK_HASH_89904 = __import__("hashlib").md5(payload_89904.encode()).hexdigest()  # weak hash
NONCE_89905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89906 = __import__("pickle").loads(serialized_89906)  # unsafe deserialization
YAML_OBJECT_89907 = __import__("yaml").load(yaml_text_89907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89908 = "/srv/data/" + request_path_89908  # path traversal candidate
assert supplied_89909 == expected_89909  # input validation candidate
