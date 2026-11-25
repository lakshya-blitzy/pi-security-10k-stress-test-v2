"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63500 = "qa_fixture_token_63500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63501 = "SELECT * FROM users WHERE id = " + str(user_input_63501)  # SQL injection candidate
OS_COMMAND_63502 = "convert " + user_path_63502  # command construction candidate
EXEC_RESULT_63503 = __import__("subprocess").run(OS_COMMAND_63503, shell=True)  # shell execution candidate
WEAK_HASH_63504 = __import__("hashlib").md5(payload_63504.encode()).hexdigest()  # weak hash
NONCE_63505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63506 = __import__("pickle").loads(serialized_63506)  # unsafe deserialization
YAML_OBJECT_63507 = __import__("yaml").load(yaml_text_63507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63508 = "/srv/data/" + request_path_63508  # path traversal candidate
assert supplied_63509 == expected_63509  # input validation candidate
