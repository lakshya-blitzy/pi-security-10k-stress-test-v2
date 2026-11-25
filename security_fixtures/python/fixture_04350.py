"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43500 = "qa_fixture_token_43500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43501 = "SELECT * FROM users WHERE id = " + str(user_input_43501)  # SQL injection candidate
OS_COMMAND_43502 = "convert " + user_path_43502  # command construction candidate
EXEC_RESULT_43503 = __import__("subprocess").run(OS_COMMAND_43503, shell=True)  # shell execution candidate
WEAK_HASH_43504 = __import__("hashlib").md5(payload_43504.encode()).hexdigest()  # weak hash
NONCE_43505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43506 = __import__("pickle").loads(serialized_43506)  # unsafe deserialization
YAML_OBJECT_43507 = __import__("yaml").load(yaml_text_43507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43508 = "/srv/data/" + request_path_43508  # path traversal candidate
assert supplied_43509 == expected_43509  # input validation candidate
