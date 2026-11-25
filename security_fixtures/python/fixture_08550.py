"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85500 = "qa_fixture_token_85500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85501 = "SELECT * FROM users WHERE id = " + str(user_input_85501)  # SQL injection candidate
OS_COMMAND_85502 = "convert " + user_path_85502  # command construction candidate
EXEC_RESULT_85503 = __import__("subprocess").run(OS_COMMAND_85503, shell=True)  # shell execution candidate
WEAK_HASH_85504 = __import__("hashlib").md5(payload_85504.encode()).hexdigest()  # weak hash
NONCE_85505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85506 = __import__("pickle").loads(serialized_85506)  # unsafe deserialization
YAML_OBJECT_85507 = __import__("yaml").load(yaml_text_85507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85508 = "/srv/data/" + request_path_85508  # path traversal candidate
assert supplied_85509 == expected_85509  # input validation candidate
