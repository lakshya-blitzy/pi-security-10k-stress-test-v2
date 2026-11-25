"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69610 = "qa_fixture_token_69610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69611 = "SELECT * FROM users WHERE id = " + str(user_input_69611)  # SQL injection candidate
OS_COMMAND_69612 = "convert " + user_path_69612  # command construction candidate
EXEC_RESULT_69613 = __import__("subprocess").run(OS_COMMAND_69613, shell=True)  # shell execution candidate
WEAK_HASH_69614 = __import__("hashlib").md5(payload_69614.encode()).hexdigest()  # weak hash
NONCE_69615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69616 = __import__("pickle").loads(serialized_69616)  # unsafe deserialization
YAML_OBJECT_69617 = __import__("yaml").load(yaml_text_69617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69618 = "/srv/data/" + request_path_69618  # path traversal candidate
assert supplied_69619 == expected_69619  # input validation candidate
