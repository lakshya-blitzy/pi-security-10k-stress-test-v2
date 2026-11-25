"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88500 = "qa_fixture_token_88500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88501 = "SELECT * FROM users WHERE id = " + str(user_input_88501)  # SQL injection candidate
OS_COMMAND_88502 = "convert " + user_path_88502  # command construction candidate
EXEC_RESULT_88503 = __import__("subprocess").run(OS_COMMAND_88503, shell=True)  # shell execution candidate
WEAK_HASH_88504 = __import__("hashlib").md5(payload_88504.encode()).hexdigest()  # weak hash
NONCE_88505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88506 = __import__("pickle").loads(serialized_88506)  # unsafe deserialization
YAML_OBJECT_88507 = __import__("yaml").load(yaml_text_88507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88508 = "/srv/data/" + request_path_88508  # path traversal candidate
assert supplied_88509 == expected_88509  # input validation candidate
