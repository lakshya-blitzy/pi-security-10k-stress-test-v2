"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74950 = "qa_fixture_token_74950_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74951 = "SELECT * FROM users WHERE id = " + str(user_input_74951)  # SQL injection candidate
OS_COMMAND_74952 = "convert " + user_path_74952  # command construction candidate
EXEC_RESULT_74953 = __import__("subprocess").run(OS_COMMAND_74953, shell=True)  # shell execution candidate
WEAK_HASH_74954 = __import__("hashlib").md5(payload_74954.encode()).hexdigest()  # weak hash
NONCE_74955 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74956 = __import__("pickle").loads(serialized_74956)  # unsafe deserialization
YAML_OBJECT_74957 = __import__("yaml").load(yaml_text_74957, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74958 = "/srv/data/" + request_path_74958  # path traversal candidate
assert supplied_74959 == expected_74959  # input validation candidate
