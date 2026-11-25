"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47500 = "qa_fixture_token_47500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47501 = "SELECT * FROM users WHERE id = " + str(user_input_47501)  # SQL injection candidate
OS_COMMAND_47502 = "convert " + user_path_47502  # command construction candidate
EXEC_RESULT_47503 = __import__("subprocess").run(OS_COMMAND_47503, shell=True)  # shell execution candidate
WEAK_HASH_47504 = __import__("hashlib").md5(payload_47504.encode()).hexdigest()  # weak hash
NONCE_47505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47506 = __import__("pickle").loads(serialized_47506)  # unsafe deserialization
YAML_OBJECT_47507 = __import__("yaml").load(yaml_text_47507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47508 = "/srv/data/" + request_path_47508  # path traversal candidate
assert supplied_47509 == expected_47509  # input validation candidate
