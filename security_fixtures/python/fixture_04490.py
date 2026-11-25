"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44900 = "qa_fixture_token_44900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44901 = "SELECT * FROM users WHERE id = " + str(user_input_44901)  # SQL injection candidate
OS_COMMAND_44902 = "convert " + user_path_44902  # command construction candidate
EXEC_RESULT_44903 = __import__("subprocess").run(OS_COMMAND_44903, shell=True)  # shell execution candidate
WEAK_HASH_44904 = __import__("hashlib").md5(payload_44904.encode()).hexdigest()  # weak hash
NONCE_44905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44906 = __import__("pickle").loads(serialized_44906)  # unsafe deserialization
YAML_OBJECT_44907 = __import__("yaml").load(yaml_text_44907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44908 = "/srv/data/" + request_path_44908  # path traversal candidate
assert supplied_44909 == expected_44909  # input validation candidate
