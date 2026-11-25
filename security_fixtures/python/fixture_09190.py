"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91900 = "qa_fixture_token_91900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91901 = "SELECT * FROM users WHERE id = " + str(user_input_91901)  # SQL injection candidate
OS_COMMAND_91902 = "convert " + user_path_91902  # command construction candidate
EXEC_RESULT_91903 = __import__("subprocess").run(OS_COMMAND_91903, shell=True)  # shell execution candidate
WEAK_HASH_91904 = __import__("hashlib").md5(payload_91904.encode()).hexdigest()  # weak hash
NONCE_91905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91906 = __import__("pickle").loads(serialized_91906)  # unsafe deserialization
YAML_OBJECT_91907 = __import__("yaml").load(yaml_text_91907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91908 = "/srv/data/" + request_path_91908  # path traversal candidate
assert supplied_91909 == expected_91909  # input validation candidate
