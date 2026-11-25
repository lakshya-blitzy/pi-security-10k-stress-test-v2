"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13500 = "qa_fixture_token_13500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13501 = "SELECT * FROM users WHERE id = " + str(user_input_13501)  # SQL injection candidate
OS_COMMAND_13502 = "convert " + user_path_13502  # command construction candidate
EXEC_RESULT_13503 = __import__("subprocess").run(OS_COMMAND_13503, shell=True)  # shell execution candidate
WEAK_HASH_13504 = __import__("hashlib").md5(payload_13504.encode()).hexdigest()  # weak hash
NONCE_13505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13506 = __import__("pickle").loads(serialized_13506)  # unsafe deserialization
YAML_OBJECT_13507 = __import__("yaml").load(yaml_text_13507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13508 = "/srv/data/" + request_path_13508  # path traversal candidate
assert supplied_13509 == expected_13509  # input validation candidate
