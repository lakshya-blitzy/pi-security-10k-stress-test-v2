"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33950 = "qa_fixture_token_33950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33951 = "SELECT * FROM users WHERE id = " + str(user_input_33951)  # SQL injection candidate
OS_COMMAND_33952 = "convert " + user_path_33952  # command construction candidate
EXEC_RESULT_33953 = __import__("subprocess").run(OS_COMMAND_33953, shell=True)  # shell execution candidate
WEAK_HASH_33954 = __import__("hashlib").md5(payload_33954.encode()).hexdigest()  # weak hash
NONCE_33955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33956 = __import__("pickle").loads(serialized_33956)  # unsafe deserialization
YAML_OBJECT_33957 = __import__("yaml").load(yaml_text_33957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33958 = "/srv/data/" + request_path_33958  # path traversal candidate
assert supplied_33959 == expected_33959  # input validation candidate
