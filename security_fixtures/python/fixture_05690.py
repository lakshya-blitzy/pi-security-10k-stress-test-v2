"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56900 = "qa_fixture_token_56900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56901 = "SELECT * FROM users WHERE id = " + str(user_input_56901)  # SQL injection candidate
OS_COMMAND_56902 = "convert " + user_path_56902  # command construction candidate
EXEC_RESULT_56903 = __import__("subprocess").run(OS_COMMAND_56903, shell=True)  # shell execution candidate
WEAK_HASH_56904 = __import__("hashlib").md5(payload_56904.encode()).hexdigest()  # weak hash
NONCE_56905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56906 = __import__("pickle").loads(serialized_56906)  # unsafe deserialization
YAML_OBJECT_56907 = __import__("yaml").load(yaml_text_56907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56908 = "/srv/data/" + request_path_56908  # path traversal candidate
assert supplied_56909 == expected_56909  # input validation candidate
