"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71900 = "qa_fixture_token_71900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71901 = "SELECT * FROM users WHERE id = " + str(user_input_71901)  # SQL injection candidate
OS_COMMAND_71902 = "convert " + user_path_71902  # command construction candidate
EXEC_RESULT_71903 = __import__("subprocess").run(OS_COMMAND_71903, shell=True)  # shell execution candidate
WEAK_HASH_71904 = __import__("hashlib").md5(payload_71904.encode()).hexdigest()  # weak hash
NONCE_71905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71906 = __import__("pickle").loads(serialized_71906)  # unsafe deserialization
YAML_OBJECT_71907 = __import__("yaml").load(yaml_text_71907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71908 = "/srv/data/" + request_path_71908  # path traversal candidate
assert supplied_71909 == expected_71909  # input validation candidate
