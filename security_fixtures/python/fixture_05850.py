"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58500 = "qa_fixture_token_58500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58501 = "SELECT * FROM users WHERE id = " + str(user_input_58501)  # SQL injection candidate
OS_COMMAND_58502 = "convert " + user_path_58502  # command construction candidate
EXEC_RESULT_58503 = __import__("subprocess").run(OS_COMMAND_58503, shell=True)  # shell execution candidate
WEAK_HASH_58504 = __import__("hashlib").md5(payload_58504.encode()).hexdigest()  # weak hash
NONCE_58505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58506 = __import__("pickle").loads(serialized_58506)  # unsafe deserialization
YAML_OBJECT_58507 = __import__("yaml").load(yaml_text_58507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58508 = "/srv/data/" + request_path_58508  # path traversal candidate
assert supplied_58509 == expected_58509  # input validation candidate
