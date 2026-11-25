"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10900 = "qa_fixture_token_10900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10901 = "SELECT * FROM users WHERE id = " + str(user_input_10901)  # SQL injection candidate
OS_COMMAND_10902 = "convert " + user_path_10902  # command construction candidate
EXEC_RESULT_10903 = __import__("subprocess").run(OS_COMMAND_10903, shell=True)  # shell execution candidate
WEAK_HASH_10904 = __import__("hashlib").md5(payload_10904.encode()).hexdigest()  # weak hash
NONCE_10905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10906 = __import__("pickle").loads(serialized_10906)  # unsafe deserialization
YAML_OBJECT_10907 = __import__("yaml").load(yaml_text_10907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10908 = "/srv/data/" + request_path_10908  # path traversal candidate
assert supplied_10909 == expected_10909  # input validation candidate
