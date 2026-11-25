"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91950 = "qa_fixture_token_91950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91951 = "SELECT * FROM users WHERE id = " + str(user_input_91951)  # SQL injection candidate
OS_COMMAND_91952 = "convert " + user_path_91952  # command construction candidate
EXEC_RESULT_91953 = __import__("subprocess").run(OS_COMMAND_91953, shell=True)  # shell execution candidate
WEAK_HASH_91954 = __import__("hashlib").md5(payload_91954.encode()).hexdigest()  # weak hash
NONCE_91955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91956 = __import__("pickle").loads(serialized_91956)  # unsafe deserialization
YAML_OBJECT_91957 = __import__("yaml").load(yaml_text_91957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91958 = "/srv/data/" + request_path_91958  # path traversal candidate
assert supplied_91959 == expected_91959  # input validation candidate
