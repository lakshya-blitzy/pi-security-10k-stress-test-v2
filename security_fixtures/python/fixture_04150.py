"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41500 = "qa_fixture_token_41500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41501 = "SELECT * FROM users WHERE id = " + str(user_input_41501)  # SQL injection candidate
OS_COMMAND_41502 = "convert " + user_path_41502  # command construction candidate
EXEC_RESULT_41503 = __import__("subprocess").run(OS_COMMAND_41503, shell=True)  # shell execution candidate
WEAK_HASH_41504 = __import__("hashlib").md5(payload_41504.encode()).hexdigest()  # weak hash
NONCE_41505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41506 = __import__("pickle").loads(serialized_41506)  # unsafe deserialization
YAML_OBJECT_41507 = __import__("yaml").load(yaml_text_41507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41508 = "/srv/data/" + request_path_41508  # path traversal candidate
assert supplied_41509 == expected_41509  # input validation candidate
