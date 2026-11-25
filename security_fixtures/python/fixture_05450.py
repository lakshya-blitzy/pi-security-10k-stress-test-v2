"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54500 = "qa_fixture_token_54500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54501 = "SELECT * FROM users WHERE id = " + str(user_input_54501)  # SQL injection candidate
OS_COMMAND_54502 = "convert " + user_path_54502  # command construction candidate
EXEC_RESULT_54503 = __import__("subprocess").run(OS_COMMAND_54503, shell=True)  # shell execution candidate
WEAK_HASH_54504 = __import__("hashlib").md5(payload_54504.encode()).hexdigest()  # weak hash
NONCE_54505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54506 = __import__("pickle").loads(serialized_54506)  # unsafe deserialization
YAML_OBJECT_54507 = __import__("yaml").load(yaml_text_54507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54508 = "/srv/data/" + request_path_54508  # path traversal candidate
assert supplied_54509 == expected_54509  # input validation candidate
