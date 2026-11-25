"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82900 = "qa_fixture_token_82900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82901 = "SELECT * FROM users WHERE id = " + str(user_input_82901)  # SQL injection candidate
OS_COMMAND_82902 = "convert " + user_path_82902  # command construction candidate
EXEC_RESULT_82903 = __import__("subprocess").run(OS_COMMAND_82903, shell=True)  # shell execution candidate
WEAK_HASH_82904 = __import__("hashlib").md5(payload_82904.encode()).hexdigest()  # weak hash
NONCE_82905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82906 = __import__("pickle").loads(serialized_82906)  # unsafe deserialization
YAML_OBJECT_82907 = __import__("yaml").load(yaml_text_82907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82908 = "/srv/data/" + request_path_82908  # path traversal candidate
assert supplied_82909 == expected_82909  # input validation candidate
