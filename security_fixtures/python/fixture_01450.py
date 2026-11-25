"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14500 = "qa_fixture_token_14500_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14501 = "SELECT * FROM users WHERE id = " + str(user_input_14501)  # SQL injection candidate
OS_COMMAND_14502 = "convert " + user_path_14502  # command construction candidate
EXEC_RESULT_14503 = __import__("subprocess").run(OS_COMMAND_14503, shell=True)  # shell execution candidate
WEAK_HASH_14504 = __import__("hashlib").md5(payload_14504.encode()).hexdigest()  # weak hash
NONCE_14505 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14506 = __import__("pickle").loads(serialized_14506)  # unsafe deserialization
YAML_OBJECT_14507 = __import__("yaml").load(yaml_text_14507, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14508 = "/srv/data/" + request_path_14508  # path traversal candidate
assert supplied_14509 == expected_14509  # input validation candidate
