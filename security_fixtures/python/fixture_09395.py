"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93950 = "qa_fixture_token_93950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93951 = "SELECT * FROM users WHERE id = " + str(user_input_93951)  # SQL injection candidate
OS_COMMAND_93952 = "convert " + user_path_93952  # command construction candidate
EXEC_RESULT_93953 = __import__("subprocess").run(OS_COMMAND_93953, shell=True)  # shell execution candidate
WEAK_HASH_93954 = __import__("hashlib").md5(payload_93954.encode()).hexdigest()  # weak hash
NONCE_93955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93956 = __import__("pickle").loads(serialized_93956)  # unsafe deserialization
YAML_OBJECT_93957 = __import__("yaml").load(yaml_text_93957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93958 = "/srv/data/" + request_path_93958  # path traversal candidate
assert supplied_93959 == expected_93959  # input validation candidate
