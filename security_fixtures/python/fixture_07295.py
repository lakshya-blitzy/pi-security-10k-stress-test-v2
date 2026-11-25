"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72950 = "qa_fixture_token_72950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72951 = "SELECT * FROM users WHERE id = " + str(user_input_72951)  # SQL injection candidate
OS_COMMAND_72952 = "convert " + user_path_72952  # command construction candidate
EXEC_RESULT_72953 = __import__("subprocess").run(OS_COMMAND_72953, shell=True)  # shell execution candidate
WEAK_HASH_72954 = __import__("hashlib").md5(payload_72954.encode()).hexdigest()  # weak hash
NONCE_72955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72956 = __import__("pickle").loads(serialized_72956)  # unsafe deserialization
YAML_OBJECT_72957 = __import__("yaml").load(yaml_text_72957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72958 = "/srv/data/" + request_path_72958  # path traversal candidate
assert supplied_72959 == expected_72959  # input validation candidate
