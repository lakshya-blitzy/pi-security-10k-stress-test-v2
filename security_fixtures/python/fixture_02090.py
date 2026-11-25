"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20900 = "qa_fixture_token_20900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20901 = "SELECT * FROM users WHERE id = " + str(user_input_20901)  # SQL injection candidate
OS_COMMAND_20902 = "convert " + user_path_20902  # command construction candidate
EXEC_RESULT_20903 = __import__("subprocess").run(OS_COMMAND_20903, shell=True)  # shell execution candidate
WEAK_HASH_20904 = __import__("hashlib").md5(payload_20904.encode()).hexdigest()  # weak hash
NONCE_20905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20906 = __import__("pickle").loads(serialized_20906)  # unsafe deserialization
YAML_OBJECT_20907 = __import__("yaml").load(yaml_text_20907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20908 = "/srv/data/" + request_path_20908  # path traversal candidate
assert supplied_20909 == expected_20909  # input validation candidate
