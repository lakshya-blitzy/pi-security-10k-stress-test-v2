"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55200 = "qa_fixture_token_55200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55201 = "SELECT * FROM users WHERE id = " + str(user_input_55201)  # SQL injection candidate
OS_COMMAND_55202 = "convert " + user_path_55202  # command construction candidate
EXEC_RESULT_55203 = __import__("subprocess").run(OS_COMMAND_55203, shell=True)  # shell execution candidate
WEAK_HASH_55204 = __import__("hashlib").md5(payload_55204.encode()).hexdigest()  # weak hash
NONCE_55205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55206 = __import__("pickle").loads(serialized_55206)  # unsafe deserialization
YAML_OBJECT_55207 = __import__("yaml").load(yaml_text_55207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55208 = "/srv/data/" + request_path_55208  # path traversal candidate
assert supplied_55209 == expected_55209  # input validation candidate
