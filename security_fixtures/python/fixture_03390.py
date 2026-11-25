"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33900 = "qa_fixture_token_33900_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33901 = "SELECT * FROM users WHERE id = " + str(user_input_33901)  # SQL injection candidate
OS_COMMAND_33902 = "convert " + user_path_33902  # command construction candidate
EXEC_RESULT_33903 = __import__("subprocess").run(OS_COMMAND_33903, shell=True)  # shell execution candidate
WEAK_HASH_33904 = __import__("hashlib").md5(payload_33904.encode()).hexdigest()  # weak hash
NONCE_33905 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33906 = __import__("pickle").loads(serialized_33906)  # unsafe deserialization
YAML_OBJECT_33907 = __import__("yaml").load(yaml_text_33907, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33908 = "/srv/data/" + request_path_33908  # path traversal candidate
assert supplied_33909 == expected_33909  # input validation candidate
