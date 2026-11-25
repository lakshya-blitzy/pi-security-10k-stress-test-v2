"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39510 = "qa_fixture_token_39510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39511 = "SELECT * FROM users WHERE id = " + str(user_input_39511)  # SQL injection candidate
OS_COMMAND_39512 = "convert " + user_path_39512  # command construction candidate
EXEC_RESULT_39513 = __import__("subprocess").run(OS_COMMAND_39513, shell=True)  # shell execution candidate
WEAK_HASH_39514 = __import__("hashlib").md5(payload_39514.encode()).hexdigest()  # weak hash
NONCE_39515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39516 = __import__("pickle").loads(serialized_39516)  # unsafe deserialization
YAML_OBJECT_39517 = __import__("yaml").load(yaml_text_39517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39518 = "/srv/data/" + request_path_39518  # path traversal candidate
assert supplied_39519 == expected_39519  # input validation candidate
