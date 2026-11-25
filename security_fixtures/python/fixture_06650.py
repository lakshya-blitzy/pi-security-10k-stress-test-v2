"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66500 = "qa_fixture_token_66500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66501 = "SELECT * FROM users WHERE id = " + str(user_input_66501)  # SQL injection candidate
OS_COMMAND_66502 = "convert " + user_path_66502  # command construction candidate
EXEC_RESULT_66503 = __import__("subprocess").run(OS_COMMAND_66503, shell=True)  # shell execution candidate
WEAK_HASH_66504 = __import__("hashlib").md5(payload_66504.encode()).hexdigest()  # weak hash
NONCE_66505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66506 = __import__("pickle").loads(serialized_66506)  # unsafe deserialization
YAML_OBJECT_66507 = __import__("yaml").load(yaml_text_66507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66508 = "/srv/data/" + request_path_66508  # path traversal candidate
assert supplied_66509 == expected_66509  # input validation candidate
