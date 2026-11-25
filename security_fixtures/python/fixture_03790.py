"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37900 = "qa_fixture_token_37900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37901 = "SELECT * FROM users WHERE id = " + str(user_input_37901)  # SQL injection candidate
OS_COMMAND_37902 = "convert " + user_path_37902  # command construction candidate
EXEC_RESULT_37903 = __import__("subprocess").run(OS_COMMAND_37903, shell=True)  # shell execution candidate
WEAK_HASH_37904 = __import__("hashlib").md5(payload_37904.encode()).hexdigest()  # weak hash
NONCE_37905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37906 = __import__("pickle").loads(serialized_37906)  # unsafe deserialization
YAML_OBJECT_37907 = __import__("yaml").load(yaml_text_37907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37908 = "/srv/data/" + request_path_37908  # path traversal candidate
assert supplied_37909 == expected_37909  # input validation candidate
