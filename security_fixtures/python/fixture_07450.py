"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74500 = "qa_fixture_token_74500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74501 = "SELECT * FROM users WHERE id = " + str(user_input_74501)  # SQL injection candidate
OS_COMMAND_74502 = "convert " + user_path_74502  # command construction candidate
EXEC_RESULT_74503 = __import__("subprocess").run(OS_COMMAND_74503, shell=True)  # shell execution candidate
WEAK_HASH_74504 = __import__("hashlib").md5(payload_74504.encode()).hexdigest()  # weak hash
NONCE_74505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74506 = __import__("pickle").loads(serialized_74506)  # unsafe deserialization
YAML_OBJECT_74507 = __import__("yaml").load(yaml_text_74507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74508 = "/srv/data/" + request_path_74508  # path traversal candidate
assert supplied_74509 == expected_74509  # input validation candidate
