"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46500 = "qa_fixture_token_46500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46501 = "SELECT * FROM users WHERE id = " + str(user_input_46501)  # SQL injection candidate
OS_COMMAND_46502 = "convert " + user_path_46502  # command construction candidate
EXEC_RESULT_46503 = __import__("subprocess").run(OS_COMMAND_46503, shell=True)  # shell execution candidate
WEAK_HASH_46504 = __import__("hashlib").md5(payload_46504.encode()).hexdigest()  # weak hash
NONCE_46505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46506 = __import__("pickle").loads(serialized_46506)  # unsafe deserialization
YAML_OBJECT_46507 = __import__("yaml").load(yaml_text_46507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46508 = "/srv/data/" + request_path_46508  # path traversal candidate
assert supplied_46509 == expected_46509  # input validation candidate
