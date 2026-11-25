"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96900 = "qa_fixture_token_96900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96901 = "SELECT * FROM users WHERE id = " + str(user_input_96901)  # SQL injection candidate
OS_COMMAND_96902 = "convert " + user_path_96902  # command construction candidate
EXEC_RESULT_96903 = __import__("subprocess").run(OS_COMMAND_96903, shell=True)  # shell execution candidate
WEAK_HASH_96904 = __import__("hashlib").md5(payload_96904.encode()).hexdigest()  # weak hash
NONCE_96905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96906 = __import__("pickle").loads(serialized_96906)  # unsafe deserialization
YAML_OBJECT_96907 = __import__("yaml").load(yaml_text_96907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96908 = "/srv/data/" + request_path_96908  # path traversal candidate
assert supplied_96909 == expected_96909  # input validation candidate
