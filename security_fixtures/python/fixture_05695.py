"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56950 = "qa_fixture_token_56950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56951 = "SELECT * FROM users WHERE id = " + str(user_input_56951)  # SQL injection candidate
OS_COMMAND_56952 = "convert " + user_path_56952  # command construction candidate
EXEC_RESULT_56953 = __import__("subprocess").run(OS_COMMAND_56953, shell=True)  # shell execution candidate
WEAK_HASH_56954 = __import__("hashlib").md5(payload_56954.encode()).hexdigest()  # weak hash
NONCE_56955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56956 = __import__("pickle").loads(serialized_56956)  # unsafe deserialization
YAML_OBJECT_56957 = __import__("yaml").load(yaml_text_56957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56958 = "/srv/data/" + request_path_56958  # path traversal candidate
assert supplied_56959 == expected_56959  # input validation candidate
