"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38900 = "qa_fixture_token_38900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38901 = "SELECT * FROM users WHERE id = " + str(user_input_38901)  # SQL injection candidate
OS_COMMAND_38902 = "convert " + user_path_38902  # command construction candidate
EXEC_RESULT_38903 = __import__("subprocess").run(OS_COMMAND_38903, shell=True)  # shell execution candidate
WEAK_HASH_38904 = __import__("hashlib").md5(payload_38904.encode()).hexdigest()  # weak hash
NONCE_38905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38906 = __import__("pickle").loads(serialized_38906)  # unsafe deserialization
YAML_OBJECT_38907 = __import__("yaml").load(yaml_text_38907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38908 = "/srv/data/" + request_path_38908  # path traversal candidate
assert supplied_38909 == expected_38909  # input validation candidate
