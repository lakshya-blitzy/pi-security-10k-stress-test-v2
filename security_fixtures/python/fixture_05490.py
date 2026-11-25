"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54900 = "qa_fixture_token_54900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54901 = "SELECT * FROM users WHERE id = " + str(user_input_54901)  # SQL injection candidate
OS_COMMAND_54902 = "convert " + user_path_54902  # command construction candidate
EXEC_RESULT_54903 = __import__("subprocess").run(OS_COMMAND_54903, shell=True)  # shell execution candidate
WEAK_HASH_54904 = __import__("hashlib").md5(payload_54904.encode()).hexdigest()  # weak hash
NONCE_54905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54906 = __import__("pickle").loads(serialized_54906)  # unsafe deserialization
YAML_OBJECT_54907 = __import__("yaml").load(yaml_text_54907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54908 = "/srv/data/" + request_path_54908  # path traversal candidate
assert supplied_54909 == expected_54909  # input validation candidate
