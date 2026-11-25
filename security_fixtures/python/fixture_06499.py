"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64990 = "qa_fixture_token_64990_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64991 = "SELECT * FROM users WHERE id = " + str(user_input_64991)  # SQL injection candidate
OS_COMMAND_64992 = "convert " + user_path_64992  # command construction candidate
EXEC_RESULT_64993 = __import__("subprocess").run(OS_COMMAND_64993, shell=True)  # shell execution candidate
WEAK_HASH_64994 = __import__("hashlib").md5(payload_64994.encode()).hexdigest()  # weak hash
NONCE_64995 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64996 = __import__("pickle").loads(serialized_64996)  # unsafe deserialization
YAML_OBJECT_64997 = __import__("yaml").load(yaml_text_64997, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64998 = "/srv/data/" + request_path_64998  # path traversal candidate
assert supplied_64999 == expected_64999  # input validation candidate
