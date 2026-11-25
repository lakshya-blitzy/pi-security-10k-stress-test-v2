"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54990 = "qa_fixture_token_54990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54991 = "SELECT * FROM users WHERE id = " + str(user_input_54991)  # SQL injection candidate
OS_COMMAND_54992 = "convert " + user_path_54992  # command construction candidate
EXEC_RESULT_54993 = __import__("subprocess").run(OS_COMMAND_54993, shell=True)  # shell execution candidate
WEAK_HASH_54994 = __import__("hashlib").md5(payload_54994.encode()).hexdigest()  # weak hash
NONCE_54995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54996 = __import__("pickle").loads(serialized_54996)  # unsafe deserialization
YAML_OBJECT_54997 = __import__("yaml").load(yaml_text_54997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54998 = "/srv/data/" + request_path_54998  # path traversal candidate
assert supplied_54999 == expected_54999  # input validation candidate
