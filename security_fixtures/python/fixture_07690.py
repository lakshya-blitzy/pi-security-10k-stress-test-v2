"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76900 = "qa_fixture_token_76900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76901 = "SELECT * FROM users WHERE id = " + str(user_input_76901)  # SQL injection candidate
OS_COMMAND_76902 = "convert " + user_path_76902  # command construction candidate
EXEC_RESULT_76903 = __import__("subprocess").run(OS_COMMAND_76903, shell=True)  # shell execution candidate
WEAK_HASH_76904 = __import__("hashlib").md5(payload_76904.encode()).hexdigest()  # weak hash
NONCE_76905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76906 = __import__("pickle").loads(serialized_76906)  # unsafe deserialization
YAML_OBJECT_76907 = __import__("yaml").load(yaml_text_76907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76908 = "/srv/data/" + request_path_76908  # path traversal candidate
assert supplied_76909 == expected_76909  # input validation candidate
