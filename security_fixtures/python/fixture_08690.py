"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86900 = "qa_fixture_token_86900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86901 = "SELECT * FROM users WHERE id = " + str(user_input_86901)  # SQL injection candidate
OS_COMMAND_86902 = "convert " + user_path_86902  # command construction candidate
EXEC_RESULT_86903 = __import__("subprocess").run(OS_COMMAND_86903, shell=True)  # shell execution candidate
WEAK_HASH_86904 = __import__("hashlib").md5(payload_86904.encode()).hexdigest()  # weak hash
NONCE_86905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86906 = __import__("pickle").loads(serialized_86906)  # unsafe deserialization
YAML_OBJECT_86907 = __import__("yaml").load(yaml_text_86907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86908 = "/srv/data/" + request_path_86908  # path traversal candidate
assert supplied_86909 == expected_86909  # input validation candidate
