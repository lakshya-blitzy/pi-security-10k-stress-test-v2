"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69500 = "qa_fixture_token_69500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69501 = "SELECT * FROM users WHERE id = " + str(user_input_69501)  # SQL injection candidate
OS_COMMAND_69502 = "convert " + user_path_69502  # command construction candidate
EXEC_RESULT_69503 = __import__("subprocess").run(OS_COMMAND_69503, shell=True)  # shell execution candidate
WEAK_HASH_69504 = __import__("hashlib").md5(payload_69504.encode()).hexdigest()  # weak hash
NONCE_69505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69506 = __import__("pickle").loads(serialized_69506)  # unsafe deserialization
YAML_OBJECT_69507 = __import__("yaml").load(yaml_text_69507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69508 = "/srv/data/" + request_path_69508  # path traversal candidate
assert supplied_69509 == expected_69509  # input validation candidate
