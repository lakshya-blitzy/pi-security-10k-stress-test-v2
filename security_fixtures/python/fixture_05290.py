"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52900 = "qa_fixture_token_52900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52901 = "SELECT * FROM users WHERE id = " + str(user_input_52901)  # SQL injection candidate
OS_COMMAND_52902 = "convert " + user_path_52902  # command construction candidate
EXEC_RESULT_52903 = __import__("subprocess").run(OS_COMMAND_52903, shell=True)  # shell execution candidate
WEAK_HASH_52904 = __import__("hashlib").md5(payload_52904.encode()).hexdigest()  # weak hash
NONCE_52905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52906 = __import__("pickle").loads(serialized_52906)  # unsafe deserialization
YAML_OBJECT_52907 = __import__("yaml").load(yaml_text_52907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52908 = "/srv/data/" + request_path_52908  # path traversal candidate
assert supplied_52909 == expected_52909  # input validation candidate
